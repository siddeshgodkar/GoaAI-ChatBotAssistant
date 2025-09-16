import requests
from app.api.core.config import GROQ_API_KEY, LLAMA_API_URL


def get_chatbot_reply(user_message: str) -> str:
    """
    Sends the user message to the LLM API (Groq/OpenAI compatible)
    and returns the model's reply.
    """

    if not GROQ_API_KEY or not LLAMA_API_URL:
        return "⚠️ Chatbot not configured properly. Missing API key or URL."

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "llama-3.1-8b-instant",   # adjust to the model you want
        "messages": [
            {"role": "system", "content": "You are a helpful chatbot assistant."},
            {"role": "user", "content": user_message}
        ],
        "temperature": 0.7
    }

    try:
        response = requests.post(LLAMA_API_URL, headers=headers, json=payload)
        response.raise_for_status()
        data = response.json()

        # Extract the reply from the API response
        reply = data["choices"][0]["message"]["content"]
        return reply.strip()

    except requests.exceptions.RequestException as e:
        return f"⚠️ API Request failed: {str(e)}"
    except Exception as e:
        return f"⚠️ Error parsing response: {str(e)}"

# def get_chatbot_reply(user_message):
#     headers = {
#         "Authorization": f"Bearer {GROQ_API_KEY}",
#         "Content-Type": "application/json",
      
#     }
     
#     payload = {
#         "model": "llama-3.1-8b-instant",
#         "messages": [{"role": "user", "content": user_message}],
#         "temperature": 1
#     }

#     try:
#         response = requests.post(LLAMA_API_URL, headers=headers, json=payload)
#         response.raise_for_status()
#         data = response.json()
#         return data["choices"][0]["message"]["content"]
#     except Exception as e:
#         return f"Error: {str(e)}"
    
# def get_chatbot_reply(user_message: str) -> str:
#     # TEMPORARY: just echo back
#     return f"🤖 Bot: I heard you say '{user_message}'"
