"""Tests for server wrapper."""

from unittest.mock import patch

from skeleton.config import Config
from skeleton.server import run_server


def test_run_server_default_params(config: Config) -> None:
    """Test run_server with default parameters."""
    with patch("skeleton.server.uvicorn.run") as mock_run:
        run_server(config)
        mock_run.assert_called_once()
        _args, kwargs = mock_run.call_args
        assert kwargs["host"] == "0.0.0.0"
        assert kwargs["port"] == 8080


def test_run_server_custom_params(config: Config) -> None:
    """Test run_server with custom parameters."""
    with patch("skeleton.server.uvicorn.run") as mock_run:
        run_server(config, host="127.0.0.1", port=9000)
        mock_run.assert_called_once()
        _args, kwargs = mock_run.call_args
        assert kwargs["host"] == "127.0.0.1"
        assert kwargs["port"] == 9000


def test_run_server_creates_app(config: Config) -> None:
    """Test that run_server creates the FastAPI app."""
    with (
        patch("skeleton.server.uvicorn.run") as mock_run,
        patch("skeleton.server.create_app") as mock_create_app,
    ):
        run_server(config)
        mock_create_app.assert_called_once_with(config)
        # Verify the app is passed to uvicorn.run
        args = mock_run.call_args[0]
        assert args[0] == mock_create_app.return_value
