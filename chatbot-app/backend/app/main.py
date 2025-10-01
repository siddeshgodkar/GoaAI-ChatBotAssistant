from fastapi import FastAPI, Response, Request
from fastapi.middleware.cors import CORSMiddleware
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
from app.api.route import router
from prometheus_fastapi_instrumentator import Instrumentator


# Allowed origins
origins = [
    "http://13.204.193.171",    # backend IP (example)
    "http://35.154.28.24",      # frontend IP (example)
    "http://localhost:5173",    # local dev
    "*"                         # only for dev/testing
]

app = FastAPI()

# Prometheus Counter
REQUEST_COUNT = Counter("http_requests_total", "Total HTTP requests", ["method", "endpoint"])


@app.on_event("startup")
async def startup():
    Instrumentator().instrument(app).expose(app)
# Middleware to count requests
@app.middleware("http")
async def count_requests(request: Request, call_next):
    response = await call_next(request)
    REQUEST_COUNT.labels(method=request.method, endpoint=request.url.path).inc()
    return response

@app.get("/health")
def health():
    return {"status": "ok"}
# Metrics endpoint for Prometheus
@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)

# Health check
@app.get("/ping")
def ping():
    return {"msg": "pong"}

# Root
@app.get("/")
def root():
    return {"msg": "FastAPI chatbot running 🚀"}

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register chatbot routes
app.include_router(router, prefix="/api")
