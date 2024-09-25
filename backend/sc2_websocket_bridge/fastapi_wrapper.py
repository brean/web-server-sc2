import logging
from fastapi import FastAPI, WebSocket
from uvicorn import Config, Server
from starlette.websockets import WebSocketDisconnect

from .utils import WebSocketConnectionManager


default_logger = logging.getLogger(__name__)


def init_app(app: FastAPI, logger, sc_con, browser_con):
    async def handle_data_sc(websocket, data, game_id):
        """New data from StarCraft 2."""
        if 'type' not in data:
            logger.error('[sc] 😖 Error: type not set for data')
            return
        data['game_id'] = game_id
        if data['type'] == 'new_game':
            logger.error('add new game')
            sc_con.games[game_id] = data
        await browser_con.broadcast_json(data)
        # logger.info(str(data))

    async def handle_data_browser(websocket, data):
        """New data from Web Browser."""
        # todo: start/pause game
        if data['type'] == 'start_game':
            game_id = data['game_id']
            if game_id in sc_con.games:
                await sc_con.send_json(game_id, data)
                await websocket.send_json({
                    'type': 'game_started',
                    'game_id': game_id
                })

    @app.websocket('/sc_client')
    async def websocket_sc_client(websocket: WebSocket):
        """Connection form StarCraft 2 to the Web Server."""
        await websocket.accept()
        game_id = sc_con.add(websocket)
        # TODO: force user to Login with token
        try:
            while True:
                data = await websocket.receive_json()
                await handle_data_sc(websocket, data, game_id)
        except WebSocketDisconnect as wsd:
            logger.error('[sc] 😖 Error: %s', wsd)
        finally:
            if game_id in sc_con.games:
                del sc_con.games[game_id]
            sc_con.disconnect(game_id)

    @app.websocket('/web_client')
    async def websocket_control_ros(websocket: WebSocket):
        """Connection form Browser to the Web Server."""
        await websocket.accept()
        user_id = browser_con.add(websocket)
        # TODO: force user to Login with token
        try:
            for game_id in sc_con.games.keys():
                await websocket.send_json(sc_con.games[game_id])
            while True:
                data = await websocket.receive_json()
                await handle_data_browser(websocket, data)
        except WebSocketDisconnect as wsd:
            logger.error('[web] 😖 Error: %s', wsd)
        finally:
            browser_con.disconnect(user_id)

    # TODO get replay via app.get...


def init_fastapi(logger, loop, host, port, production=True):
    """run FastAPI server."""
    logger = logger if logger else default_logger
    logger.info('⚡ Provide WebSocket interface using fastapi')

    sc_con = WebSocketConnectionManager(logger)
    browser_con = WebSocketConnectionManager(logger)
    sc_con.games = {}

    if production:
        app = FastAPI(docs_url=None, redoc_url=None)
    else:
        app = FastAPI()
    init_app(app, logger, sc_con, browser_con)
    config = Config(app=app, loop=loop, host=host, port=port)
    server = Server(config)
    return server
