"""Tests for metrics endpoint."""

from fastapi.testclient import TestClient


def test_metrics_returns_prometheus_format(app: TestClient) -> None:
    """Test that /metrics returns Prometheus format."""
    response = app.get("/metrics")
    assert response.status_code == 200
    assert "text/plain" in response.headers["content-type"]
