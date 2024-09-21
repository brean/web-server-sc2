#!/usr/bin/env python3

# PYTHON_ARGCOMPLETE_OK

"""command line tool to start FastAPI-Wrapper."""
import asyncio
import argparse
import logging
from uvicorn import Config, Server

from .fastapi_wrapper import init_websocket

LOG_LEVEL = {
    'critical': logging.CRITICAL,
    'error': logging.ERROR,
    'info': logging.INFO,
    'warn': logging.WARN,
    'debug': logging.DEBUG
}


def setup_logging(log_level):
    """Configure Logging."""
    logging.basicConfig(level=LOG_LEVEL[log_level])
    return logging.getLogger(__name__)


def setup_argparse():
    """Configure argument parser."""
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('-p', '--port', type=int, default=8080)
    parser.add_argument('-l', '--log_level', type=str, default='info')
    return parser


def init_fastapi(logger, loop, args):
    """run FastAPI server."""
    logger.info('⚡ Provide WebSocket interface using fastapi')
    app = init_websocket()
    config = Config(app=app, loop=loop, host='0.0.0.0', port=8000)
    server = Server(config)
    return server


def setup():
    """parse data and create websocket."""
    args = setup_argparse().parse_args()
    logger = setup_logging(log_level=args.log_level)
    loop = asyncio.get_event_loop()
    return logger, loop, args


def main():
    logger, loop, args = setup()
    server = init_fastapi(logger, loop, args)
    loop.run_until_complete(server.serve())
    logger.info('exiting')
