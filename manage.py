import uvicorn

from src.main import app

if __name__ == "__main__":
    uvicorn.run(app=app, host="0.0.0.0", port=6969, log_level="info")
