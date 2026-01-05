"""Tests for HTTP endpoints."""

from fastapi.testclient import TestClient


def test_healthz_returns_ok(app: TestClient) -> None:
    """Test that /healthz returns ok status."""
    response = app.get("/healthz")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_readiness_returns_ready(app: TestClient) -> None:
    """Test that /readiness returns ready status."""
    response = app.get("/readiness")
    assert response.status_code == 200
    assert response.json() == {"status": "ready"}


def test_metrics_returns_prometheus_format(app: TestClient) -> None:
    """Test that /metrics returns Prometheus format."""
    response = app.get("/metrics")
    assert response.status_code == 200
    assert "text/plain" in response.headers["content-type"]
