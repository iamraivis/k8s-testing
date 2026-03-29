import os
from fastapi import FastAPI, HTTPException
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()
Instrumentator().instrument(app).expose(app)

# Chaos Variable
IS_BROKEN = os.getenv("IS_BROKEN", "false").lower() == "true"

@app.get("/")
def read_root():
    if IS_BROKEN:
        # Simulate a server crash / error
        raise HTTPException(status_code=500, detail="Chaos Monkey hit the server!")
    return {"status": "healthy", "version": "v3-stable"}