from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()

# This single line instruments the app and exposes the /metrics endpoint
Instrumentator().instrument(app).expose(app)

@app.get("/")
def read_root():
    return {"Hello": "GitOps World"}