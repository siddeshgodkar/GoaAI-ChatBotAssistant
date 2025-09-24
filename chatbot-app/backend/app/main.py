# from flask import Flask, render_template
# from routes.chatbot import chatbot_bp
from flask_cors import CORS
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from app.api.route import router

# from routes.maps import maps_bp

# app = Flask(__name__)

origins = [
    "http://35.154.196.104",     # your frontend
    "http://localhost:5173",    # useful for local testing
    "*"                         # allow all (temporary, not recommended for prod)
]

app = FastAPI()

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
