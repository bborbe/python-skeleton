"""FastAPI server configuration."""

import uvicorn

from skeleton.config import Config
from skeleton.factory import create_app


def run_server(config: Config, host: str = "0.0.0.0", port: int = 8080) -> None:
    """Run the HTTP server.

    Args:
        config: Application configuration
        host: Host to bind to
        port: Port to bind to
    """
    app = create_app(config)
    uvicorn.run(app, host=host, port=port)
