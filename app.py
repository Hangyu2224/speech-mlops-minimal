import time

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Speech Minimal Service", version="0.1.0")

class InferRequest(BaseModel):
    text: str

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/infer")
def infer(req: InferRequest):
    # 占位推理逻辑。模拟耗时 + 返回结果
    t0 = time.time()
    time.sleep(0.05)
    return {
        "input": req.text,
        "result": req.text.upper(),
        "lantency_ms": int((time.time() - t0) * 1000),
        "model_version": "dummy_v0"
    }       