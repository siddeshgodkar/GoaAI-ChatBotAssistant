# from flask import Blueprint, request, jsonify
# from services.llm_services import get_chatbot_reply

# chatbot_bp = Blueprint("chatbot", __name__)

# @chatbot_bp.route("/chat", methods=["POST"])
# def chat():
#     user_message = request.json.get("message")
#     reply = get_chatbot_reply(user_message)
#     return jsonify({"reply": reply})
