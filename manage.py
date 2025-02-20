import uvicorn

if __name__ == "__main__":
    uvicorn.run(app='src.main:app', host="0.0.0.0", port=6969, log_level="info", reload=True)
