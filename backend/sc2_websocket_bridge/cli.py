#!/usr/bin/env python3

# PYTHON_ARGCOMPLETE_OK

"""command line tool to start FastAPI-Wrapper."""
import asyncio
import argparse
import logging

from .fastapi_wrapper import init_fastapi


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
    parser.add_argument('--port', type=int, default=8000)
    parser.add_argument('--host', type=str, default='localhost')
    parser.add_argument('--log', type=str, default='info')
    parser.add_argument('--production', type=bool, default=True)
    return parser


def setup():
    """parse data and create websocket."""
    args = setup_argparse().parse_args()
    logger = setup_logging(log_level=args.log)
    loop = asyncio.get_event_loop()
    return logger, loop, args


def main():
    logger, loop, args = setup()
    server = init_fastapi(
        logger=logger,
        loop=loop,
        host=args.host,
        production=str(args.production).lower() in ['true', 'yes'],
        port=int(args.port))
    loop.run_until_complete(server.serve())
    logger.info('exiting')


if __name__ == '__main__':
    main()
