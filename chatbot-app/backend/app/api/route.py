from fastapi import APIRouter
from pydantic import BaseModel
from app.services.llm_services import get_chatbot_reply

router = APIRouter()

class ChatRequest(BaseModel):
    message: str

@router.post("/chat")
async def chat(request: ChatRequest):
    reply = get_chatbot_reply(request.message)
    return {"reply": reply}
