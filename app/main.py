import os

from fastapi import FastAPI, Response, status

app = FastAPI(title="capstone-app")


@app.get("/")
def root():
    return {
        "app": "capstone-app",
        "version": os.getenv("APP_VERSION", "dev"),
        "message": "Hello from capstone-app",
    }


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/ready")
def ready(response: Response):
    if os.getenv("FAIL_READINESS", "false").lower() == "true":
        response.status_code = status.HTTP_503_SERVICE_UNAVAILABLE
        return {"status": "not ready"}
    return {"status": "ready"}
