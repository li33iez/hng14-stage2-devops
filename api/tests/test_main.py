from fastapi.testclient import TestClient
from unittest.mock import patch
from main import app

client = TestClient(app)

def test_root_endpoint():
    res = client.get("/")
    assert res.status_code == 200

def test_health_endpoint():
    res = client.get("/health")
    assert res.status_code == 200
    assert res.json() == {"status": "ok"}

@patch("main.r")
def test_submit_endpoint(mock_redis):
    mock_redis.lpush.return_value = 1
    mock_redis.hset.return_value = True
    res = client.post("/submit")
    assert res.status_code == 200
    assert "job_id" in res.json()
    mock_redis.lpush.assert_called_once()
