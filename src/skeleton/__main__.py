"""Entry point for the skeleton application."""

import argparse
import logging
import os
import signal
import sys
from typing import NoReturn

import sentry_sdk
import uvicorn

from skeleton import __version__
from skeleton.config import Config
from skeleton.factory import create_app
from skeleton.logging_setup import configure_logging

logger = logging.getLogger(__name__)


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments with environment variable defaults."""
    parser = argparse.ArgumentParser(
        description="Python skeleton application",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # serve subcommand
    serve_parser = subparsers.add_parser("serve", help="Start the HTTP server")
    serve_parser.add_argument(
        "--host",
        default=os.getenv("HOST", "0.0.0.0"),
        help="Host to bind to",
    )
    serve_parser.add_argument(
        "--port",
        type=int,
        default=int(os.getenv("PORT", "8080")),
        help="Port to bind to",
    )
    serve_parser.add_argument(
        "--log-level",
        default=os.getenv("LOG_LEVEL", "INFO"),
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        help="Logging level",
    )

    # version subcommand
    subparsers.add_parser("version", help="Show version information")

    return parser.parse_args()


def setup_signal_handlers() -> None:
    """Set up signal handlers for graceful shutdown."""

    def handle_signal(signum: int, _frame: object) -> NoReturn:
        logger.info(f"Received signal {signum}, shutting down")
        sys.exit(0)

    signal.signal(signal.SIGTERM, handle_signal)
    signal.signal(signal.SIGINT, handle_signal)


def cmd_serve(args: argparse.Namespace) -> None:
    """Run the HTTP server."""
    configure_logging(args.log_level)
    setup_signal_handlers()

    config = Config()

    if config.sentry_dsn:
        sentry_sdk.init(dsn=config.sentry_dsn)
        logger.info("Sentry initialized")

    logger.info(f"Starting server: host={args.host}, port={args.port}")
    logger.info(f"Build: version={config.build_version}, commit={config.build_commit}")

    app = create_app(config)
    uvicorn.run(app, host=args.host, port=args.port, log_level=args.log_level.lower())


def cmd_version() -> None:
    """Print version information."""
    config = Config()
    print(f"skeleton {__version__}")
    print(f"  build version: {config.build_version}")
    print(f"  build commit:  {config.build_commit}")
    print(f"  build date:    {config.build_date}")


def main() -> None:
    """Main entry point."""
    args = parse_args()

    if args.command == "serve":
        cmd_serve(args)
    elif args.command == "version":
        cmd_version()


if __name__ == "__main__":
    main()
