from fastapi import FastAPI, Request
from pydantic import BaseModel
import os
import requests
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# Allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, restrict this to your frontend IP/domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

HF_TOKEN = os.getenv("HF_TOKEN")
API_URL = "https://router.huggingface.co/featherless-ai/v1/chat/completions"
headers = {
    "Authorization": f"Bearer {HF_TOKEN}",
}

class TopicRequest(BaseModel):
    topic: str

@app.post("/get_tips")
async def get_tips(request: TopicRequest):
    topic = request.topic
    payload = {
        "messages": [
            {
                "role": "user",
                "content": f"Give exactly three short, concise, and separate tips on how to improve mental health for the topic: {topic}. Number them as 1., 2., and 3. Do not include any additional messages, explanations, or user/assistant tags. Just return the 3 tips."

            }
        ],
        "model": "HuggingFaceH4/zephyr-7b-beta"
    }

    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        data = response.json()

        if "choices" in data and len(data["choices"]) > 0:
            reply = data["choices"][0]["message"]["content"].strip()
            return {"tips": reply}
        else:
            return {"tips": "Sorry, no tips could be generated."}
    except Exception as e:
        return {"tips": f"Error occurred: {str(e)}"}
