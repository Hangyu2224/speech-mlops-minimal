from fastapi.testclient import TestClient

import sys
import os

# 将上一级目录添加到模块搜索路径
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app


client = TestClient(app)

def test_health_ok():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}

def test_infer_uppercase_and_has_latency():
    r = client.post("/infer", json={"text": "hello docker"})
    assert r.status_code == 200
    data = r.json()
    assert data["input"] == "hello docker"
    assert data["result"] == "HELLO DOCKER"
    assert 'lantency_ms' in data # 按你当前输出字段名写
    assert isinstance(data['lantency_ms'], int)
    assert "model_version" in data