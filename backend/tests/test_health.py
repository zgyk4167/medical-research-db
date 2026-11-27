"""Tests for app shell: health endpoint and loopback-only binding."""


def test_health_returns_200(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_server_binds_loopback_only():
    from backend.app.main import HOST

    assert HOST == "127.0.0.1", "Server must bind to 127.0.0.1 only (security invariant)"


def test_db_fixture_works(db_session):
    from sqlalchemy import text

    result = db_session.execute(text("SELECT 1")).scalar()
    assert result == 1
