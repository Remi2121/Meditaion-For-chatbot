# Chatbot
# To "run uvicorn api_server:app --host 0.0.0.0 --port 8000 --reload "

# Un friend side-la steps

🔹 Step 1: Repo clone panna
git clone https://github.com/Remi2121/Meditaion-For-chatbot.git

cd Meditaion-For-chatbot   e

🔹 Step 2: Virtual env create + dependencies install

Windows:
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt



🔹 Step 3: .env create panna


LANGCHAIN_API_KEY="..."
LANGCHAIN_PROJECT="..."
GROQ_API_KEY="..."
HF_TOKEN="..."
HF_INFERENCE_PROVIDER=auto
TELEGRAM_API_KEY="..."
