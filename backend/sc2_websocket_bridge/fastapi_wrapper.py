import logging
from fastapi import FastAPI, WebSocket

from .utils import WebSocketConnectionManager


logger = logging.getLogger(__name__)
sc_con = WebSocketConnectionManager(logger)
browser_con = WebSocketConnectionManager(logger)


async def handle_data_sc(websocket, data, game_id):
    """New data from StarCraft 2."""
    if 'type' not in data:
        logger.error('[sc] 😖 Error: type not set for data')
        return
    data['game_id'] = game_id
    await browser_con.broadcast_json(data)
    # logger.info(str(data))


async def handle_data_browser(websocket, data):
    """New data from Web Browser."""
    # todo: start/pause game
    return


def init_fastapi(app: FastAPI):
    @app.websocket('/sc_client')
    async def websocket_sc_client(websocket: WebSocket):
        """Connection form StarCraft 2 to the Web Server."""
        await websocket.accept()
        game_id = sc_con.add(websocket)
        # TODO: force user to Login with token
        try:
            await browser_con.broadcast_json({
                'type': 'new_game',
                'game_id': game_id
            })
            while True:
                data = await websocket.receive_json()
                await handle_data_sc(websocket, data, game_id)
        except Exception as e:
            logger.error('[sc] 😖 Error: %s', e)
        finally:
            sc_con.disconnect(game_id)

    @app.websocket('/web_client')
    async def websocket_control_ros(websocket: WebSocket):
        """Connection form Browser to the Web Server."""
        await websocket.accept()
        user_id = browser_con.add(websocket)
        # TODO: force user to Login with token
        try:
            for game_id in sc_con.named_connections.keys():
                await websocket.send_json({
                    'type': 'new_game',
                    'game_id': game_id
                })
            while True:
                data = await websocket.receive_json()
                await handle_data_browser(websocket, data)
        except Exception as e:
            logger.error('[sc] 😖 Error: %s', e)
        finally:
            browser_con.disconnect(user_id)

    # TODO get replay via app.get...


def init_websocket(production=True):
    """Setup WebSocket endpoints."""
    if production:
        app = FastAPI(docs_url=None, redoc_url=None)
    else:
        app = FastAPI()

    init_fastapi(app)
    return app
