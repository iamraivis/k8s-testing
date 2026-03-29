from fastapi import FastAPI, Response
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = FastAPI()

# Create a custom metric to track how many times the root endpoint is hit
REQUEST_COUNT = Counter(
    'app_request_count', 
    'Total app HTTP request count', 
    ['method', 'endpoint']
)

@app.get("/")
def read_root():
    # Increment the counter every time someone visits this page
    REQUEST_COUNT.labels(method='GET', endpoint='/').inc()
    return {"message": "Hello from your modern K8s app!"}

@app.get("/metrics")
def metrics():
    # Expose the metrics in a format Prometheus understands
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)