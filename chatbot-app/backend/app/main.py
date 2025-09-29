# from flask import Flask, render_template
# from routes.chatbot import chatbot_bp
from flask_cors import CORS
from fastapi import FastAPI, Response, Request
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from app.api.route import router
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

# from routes.maps import maps_bp

# app = Flask(__name__)




origins = [
    "http://13.204.193.171",
    "http://35.154.28.24",     # your frontend
    "http://localhost:5173",    # useful for local testing
    "*"                         # allow all (temporary, not recommended for prod)
]

app = FastAPI()

# Example counter for total requests
REQUEST_COUNT = Counter("http_requests_total", "Total HTTP requests", ["method", "endpoint"])


# Middleware to count requests
@app.middleware("http")
async def count_requests(request: Request, call_next):
    response = await call_next(request)
    REQUEST_COUNT.labels(method=request.method, endpoint=request.url.path).inc()
    return response


# Metrics endpoint for Prometheus
@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)


# Example test endpoint
@app.get("/ping")
def ping():
    return {"msg": "pong"}

# Allow frontend to connect (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# class Message(BaseModel):
#     message: str

# Register routes
app.include_router(router, prefix="/api")
# app.register_blueprint(chatbot_bp)


# @app.route("/")
# def index():
#     return render_template("index.html")

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run("backend.app.main:app", host="127.0.0.1", port=8000, reload=True)


@app.get("/")
def root():
    return {"msg": "FastAPI chatbot running 🚀"}
