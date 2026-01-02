# Speech Minimal Service (Dockerized)

## Run locally
```bash
pip install -r requirements.txt
uvicorn app:app --host 0.0.0.0 --port 8000
```
## Run with Docker
```bash
docker build -t speech-api:dev
docker run --rm -p 8000:8000 speech-api:dev

docker-compose up -d
```

## Test
```bash
curl htttp://localhost:8000/health
curl -X POST http://localhost:8000/infer -H "Content-Type: application/json" -d "{\"text\":\"hello\"}"
```

# Day 2: Run the full stack with Docker Compose
## 1) One-command startup
In project root (where docker-compose.yml lives):
```bash
docker compose up -d --build
```
This will start:
- FastAPI API (port ${API_PORT:-8000})
- MinIO (ports ${MINIO_PORT:-9000}, console ${MINIO_CONSOLE_PORT:-9001})
- (Optional) MLflow (port ${MLFLOW_PORT:-5000}) if enabled in docker-compose.yml

## 2) Configuration (.env)
Copy .env.example to .env and adjust values if needed:
```bash
# Windows PowerShell
copy .env.example .env
```
Compose will auto-load .env in the same directory.
## 3) Directory layout (data/models/logs)
Create the following directories (once):
```bash
mkdir data\raw, data\processed, models, logs
```
## 4) Data manifest (minimal traceability)
Create data/manifest.json to record data version/source/timestamp:
```json
{
  "data_version": "1.0",
  "data_source": "https://dataset-source.com",
  "data_hash": "abc123xyz456",
  "timestamp": "2025-12-27T15:00:00Z"
}
```
### 5) Verify
API:
```bash
curl http://localhost:${API_PORT:-8000}/health
curl -X POST http://localhost:${API_PORT:-8000}/infer -H "Content-Type: application/json" -d "{\"text\":\"hello compose\"}"
```
MinIO:
API: http://localhost:${MINIO_PORT:-9000}
Console: http://localhost:${MINIO_CONSOLE_PORT:-9001}

# Day 3: CI (GitHub Actions)
## Local commands (same as CI)
```bash
python -m pip install -r requirements.txt
python -m pip install -r requirements-dev.txt
ruff check .
pytest -q
docker build -t speech-api:dev .
```

## What CI does
On every push / pull request, CI will:
1) Install dependencies
2) Run lint (ruff)
3) Run tests (pytest)
4) Build Docker image with tag = short git sha 

## How to trigger CI
- Push commits to main/master, or open a Pull Request.
```bash
git add .
git commit -m "day3: add minimal CI"
git branch -M main
git remote add origin git@github.com:Hangyu2224/speech-mlops-minimal.git
git push -u origin main
```

- CI will automatically run in GitHub Actions.
