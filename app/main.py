from fastapi import FastAPI

app = FastAPI(title="capstone-app")


@app.get("/")
def root():
    return {"app": "capstone-app", "message": "Hello from capstone-app"}
