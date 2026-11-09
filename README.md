# Title: Design and Implementation of an Automated CI/CD and GitOps Deployment Platform Using Kubernetes

# Research Question: How can CI/CD automation and GitOps practices improve the reliability, consistency, and efficiency of application deployment?

# Project Goal: Design, implement, and evaluate an automated deployment platform that integrates continuous integration, containerization, Kubernetes orchestration, GitOps-based delivery, and infrastructure monitoring.



# capstone-app

Sample FastAPI service for the capstone project
"Automated CI/CD and GitOps Deployment Platform Using Kubernetes".

## Endpoints

| Endpoint  | Purpose                                   |
|-----------|-------------------------------------------|
| `/`       | App info and version                      |
| `/health` | Liveness probe                            |
| `/ready`  | Readiness probe (`FAIL_READINESS=true` → 503) |

## Run locally

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
uvicorn app.main:app --reload --port 8000
```

## Tests

```bash
pytest -v
```

## Docker

```bash
docker build -t capstone-app:0.1.0 --build-arg APP_VERSION=0.1.0 .
docker run -d -p 8001:8000 capstone-app:0.1.0
```
