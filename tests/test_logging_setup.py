"""Tests for logging configuration."""

import logging
from unittest.mock import patch

from skeleton.logging_setup import configure_logging


def test_configure_logging_calls_basicconfig_with_debug() -> None:
    """Test that configure_logging calls basicConfig with DEBUG level."""
    with patch("logging.basicConfig") as mock_basicconfig:
        configure_logging("DEBUG")
        mock_basicconfig.assert_called_once()
        call_kwargs = mock_basicconfig.call_args[1]
        assert call_kwargs["level"] == logging.DEBUG


def test_configure_logging_calls_basicconfig_with_default() -> None:
    """Test that configure_logging calls basicConfig with INFO default."""
    with patch("logging.basicConfig") as mock_basicconfig:
        configure_logging()
        mock_basicconfig.assert_called_once()
        call_kwargs = mock_basicconfig.call_args[1]
        assert call_kwargs["level"] == logging.INFO


def test_configure_logging_case_insensitive() -> None:
    """Test that configure_logging accepts lowercase level."""
    with patch("logging.basicConfig") as mock_basicconfig:
        configure_logging("warning")
        mock_basicconfig.assert_called_once()
        call_kwargs = mock_basicconfig.call_args[1]
        assert call_kwargs["level"] == logging.WARNING


def test_configure_logging_sets_format() -> None:
    """Test that configure_logging sets the expected format."""
    with patch("logging.basicConfig") as mock_basicconfig:
        configure_logging()
        mock_basicconfig.assert_called_once()
        call_kwargs = mock_basicconfig.call_args[1]
        format_str = call_kwargs["format"]
        assert "%(asctime)s" in format_str
        assert "%(levelname)" in format_str
        assert "%(name)s" in format_str
        assert "%(message)s" in format_str
        assert "%(lineno)d" in format_str


def test_configure_logging_sets_datefmt() -> None:
    """Test that configure_logging sets date format."""
    with patch("logging.basicConfig") as mock_basicconfig:
        configure_logging()
        mock_basicconfig.assert_called_once()
        call_kwargs = mock_basicconfig.call_args[1]
        assert call_kwargs["datefmt"] == "%Y-%m-%d %H:%M:%S"
