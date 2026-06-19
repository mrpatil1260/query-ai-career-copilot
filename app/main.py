from fastapi import FastAPI

app = FastAPI(
    title="AI Knowledge Assistant",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "message": "Welcome to the AI Knowledge Assistant!"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }