from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_root():
    r = client.get("/")
    assert r.status_code == 200
    assert r.json()["message"] == "Hello from capstone-app"


def test_version_from_env(monkeypatch):
    monkeypatch.setenv("APP_VERSION", "1.2.3")
    assert client.get("/").json()["version"] == "1.2.3"


def test_health():
    r = client.get("/health")
    assert r.status_code == 200


def test_ready_by_default(monkeypatch):
    monkeypatch.delenv("FAIL_READINESS", raising=False)
    assert client.get("/ready").status_code == 200


def test_ready_fails_when_injected(monkeypatch):
    monkeypatch.setenv("FAIL_READINESS", "true")
    assert client.get("/ready").status_code == 503
    assert client.get("/health").status_code == 200
