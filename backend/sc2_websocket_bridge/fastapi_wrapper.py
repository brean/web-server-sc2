import logging
from fastapi import FastAPI, WebSocket

from .utils import WebSocketConnectionManager


logger = logging.getLogger(__name__)
sc_con = WebSocketConnectionManager(logger)
browser_con = WebSocketConnectionManager(logger)


async def handle_data_sc(websocket, data):
    """New data from StarCraft 2."""
    return


async def handle_data_browser(websocket, data):
    """New data from Web Browser."""
    return


def init_fastapi(app: FastAPI):
    @app.websocket('/sc_client')
    async def websocket_sc_client(websocket: WebSocket):
        """Connection form StarCraft 2 to the Web Server."""
        await websocket.accept()
        user_id = sc_con.add(websocket)
        # TODO: force user to Login with token
        try:
            while True:
                data = await websocket.receive_json()
                await handle_data_sc(websocket, data)
        except Exception as e:
            logger.error('[sc] 😖 Error: %s', e)
        finally:
            sc_con.disconnect(user_id)
    
    @app.websocket('/web_client')
    async def websocket_control_ros(websocket: WebSocket):
        """Connection form Browser to the Web Server."""
        await websocket.accept()
        user_id = browser_con.add(websocket)
        # TODO: force user to Login with token
        try:
            while True:
                data = await websocket.receive_json()
                await handle_data_browser(websocket, data)
        except Exception as e:
            logger.error('[sc] 😖 Error: %s', e)
        finally:
            browser_con.disconnect(user_id)


def init_websocket(production=True):
    """Setup WebSocket endpoints."""
    if production:
        app = FastAPI(docs_url=None, redoc_url=None)
    else:
        app = FastAPI()

    init_fastapi(app)
    return app
