# bankmind-[IshanviMahendraChavan]

# Bank Deposit Prediction Engine & Live Explanation Routing Pipeline

This repository hosts an end-to-end machine learning inference pipeline built using an optimized scikit-learn Random Forest model integrated with an enterprise FastAPI gateway and live Llama-3.3 natural language generation layers via Groq.

---

## PART 1: How to Set Up and Run the Project

Follow these consecutive deployment steps to clear your environment cache, extract assets, and launch the local production server kernel.

### Step 1: Install System Dependencies

> ⚠️ **IMPORTANT REQUIRED STEP:** Due to GitHub file size limitations, you must download the trained model binary `bank_model.pkl` from [This Google Drive Link](https://drive.google.com/file/d/1XE2-j9askzmLlOLuMKE7EojMTNbyFoLM/view?usp=sharing) and place it directly into the **root directory** of this project repository before starting the Uvicorn application server.

Ensure you have **Python** installed on your local machine. Open your terminal inside your local project directory and execute:

```bash
pip install -r requirements.txt

Step 2: Configure System Environment Credentials

To allow live Llama-3.3 evaluation narrative compilation, pass your Groq developer key to your environment variables matrix:

* **On Git Bash / Linux / macOS:**
```bash
  export GROQ_API_KEY="your_actual_api_key_here"

On Windows (Command Prompt - cmd):
$env:GROQ_API_KEY="your_actual_api_key_here"

(Note: If no explicit key configuration occurs, the core prediction models will automatically fallback gracefully to baseline internal text parameters).

Step 3: Boot the Live Uvicorn Application Server

Start up your local gateway application by running the executable module flag directly inside your terminal session (ensuring your path is set to the project root):

python -m uvicorn main:app --reload

Once your console logs initialize successfully, you can view the fully dynamic and interactive GUI OpenAPI system dashboard by navigating to: http://127.0.0.1:8000/docs

PART 2: System API Endpoints & Working cURL Usage Examples
Keep your primary server terminal window running and open a brand-new secondary command line window to fire and validate these backend operations using standard curl formatting requests.

1. System Health & Diagnostic Verification (GET /health)
Verifies if your application layer is active and checks whether the machine learning binary array has been safely loaded into memory.

Bash
curl -X 'GET' '[http://127.0.0.1:8000/health](http://127.0.0.1:8000/health)' -H 'accept: application/json'
Expected JSON Output Response:

JSON
{
  "status": "ok",
  "model": "RandomForestClassifier-TrackC"
}
2. High-Velocity Acquisition Prediction (POST /predict)
Processes a validated consumer data profile payload and returns localized probabilities, conversion state flags, and primary driving customer features.

Bash
curl -X 'POST' \
  '[http://127.0.0.1:8000/predict](http://127.0.0.1:8000/predict)' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "age": 42,
  "job": "management",
  "marital": "married",
  "education": "tertiary",
  "default": "no",
  "balance": 3500,
  "housing": "no",
  "loan": "no",
  "contact": "cellular",
  "day": 12,
  "month": "jun",
  "duration": 480,
  "campaign": 1,
  "pdays": -1,
  "previous": 0,
  "poutcome": "unknown"
}'
Expected JSON Output Response:

JSON
{
  "will_subscribe": true,
  "probability": 0.83,
  "top_factors": [
    "extended communication conversation length",
    "absence of active housing debt obligations"
  ]
}
3. Generative Conversational Pitch Briefings (POST /explain)
Routes numerical baseline insights directly through a Llama-3.3 LLM instance on the Groq platform to synthesize plain-text conversation strategies for bank personnel.

Bash
curl -X 'POST' \
  '[http://127.0.0.1:8000/explain](http://127.0.0.1:8000/explain)' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "age": 42,
  "job": "management",
  "marital": "married",
  "education": "tertiary",
  "default": "no",
  "balance": 3500,
  "housing": "no",
  "loan": "no",
  "contact": "cellular",
  "day": 12,
  "month": "jun",
  "duration": 480,
  "campaign": 1,
  "pdays": -1,
  "previous": 0,
  "poutcome": "unknown"
}'
Expected JSON Output Response (With Active Key Configured):

JSON
{
  "prediction_metrics": {
    "will_subscribe": true,
    "probability": 0.83,
    "top_factors": [
      "extended communication conversation length",
      "absence of active housing debt obligations"
    ]
  },
  "llm_explanation": "This customer shows high conversion intent due to an extensive phone conversation duration and a strong cash reserve balance ($3500). The Relationship Manager should pitch by emphasizing safety and premium asset allocation, highlighting the absolute absence of conflicting debt obligations."
}


