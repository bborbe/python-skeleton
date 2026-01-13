"""Tests for CLI entry point."""

import sys
from io import StringIO
from unittest.mock import patch

import pytest

from skeleton.__main__ import cmd_version, parse_args


def test_parse_args_serve_defaults() -> None:
    """Test parse_args with serve command and defaults."""
    with patch.object(sys, "argv", ["skeleton", "serve"]):
        args = parse_args()
        assert args.command == "serve"
        assert args.host == "0.0.0.0"
        assert args.port == 8080
        assert args.log_level == "INFO"


def test_parse_args_serve_custom_values() -> None:
    """Test parse_args with serve command and custom values."""
    with patch.object(
        sys,
        "argv",
        ["skeleton", "serve", "--host", "127.0.0.1", "--port", "9000", "--log-level", "DEBUG"],
    ):
        args = parse_args()
        assert args.command == "serve"
        assert args.host == "127.0.0.1"
        assert args.port == 9000
        assert args.log_level == "DEBUG"


def test_parse_args_version() -> None:
    """Test parse_args with version command."""
    with patch.object(sys, "argv", ["skeleton", "version"]):
        args = parse_args()
        assert args.command == "version"


def test_parse_args_missing_command() -> None:
    """Test parse_args fails when no command is provided."""
    with patch.object(sys, "argv", ["skeleton"]), pytest.raises(SystemExit):
        parse_args()


def test_cmd_version_output() -> None:
    """Test cmd_version prints expected information."""
    output = StringIO()
    with patch("sys.stdout", output):
        cmd_version()

    output_text = output.getvalue()
    assert "skeleton" in output_text
    assert "build version:" in output_text
    assert "build commit:" in output_text
    assert "build date:" in output_text
