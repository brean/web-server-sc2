from fastapi import FastAPI


def init_fastapi(app: FastAPI):
    return


def init_websocket(production=True):
    """Setup WebSocket endpoints."""
    if production:
        app = FastAPI(docs_url=None, redoc_url=None)
    else:
        app = FastAPI()

    init_fastapi(app)
    return app
