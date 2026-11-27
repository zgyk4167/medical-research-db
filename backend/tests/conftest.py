"""Shared test fixtures: test database and FastAPI test client."""

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from backend.app.main import app, HOST


@pytest.fixture()
def db_engine():
    """In-memory SQLite engine for tests."""
    engine = create_engine(
        "sqlite+pysqlite:///:memory:",
        connect_args={"check_same_thread": False},
    )
    yield engine
    engine.dispose()


@pytest.fixture()
def db_session(db_engine):
    """Session bound to the test database."""
    factory = sessionmaker(bind=db_engine, autoflush=False, expire_on_commit=False)
    session = factory()
    yield session
    session.close()


@pytest.fixture()
def client():
    """Synchronous test client for the FastAPI app."""
    with TestClient(app) as c:
        yield c
