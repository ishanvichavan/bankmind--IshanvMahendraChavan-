# bankmind-[IshanviMahendraChavan]

## Bank Deposit Prediction Engine & Live Explanation Routing Pipeline

This repository hosts an end-to-end machine learning inference pipeline built using an optimized scikit-learn Random Forest model integrated with an enterprise FastAPI gateway and live Llama-3.3 natural language generation layers via Groq.

---

## Part 1: How to Set Up and Run the Project

Follow these steps to install dependencies, configure credentials, and launch the local server.

### Step 1: Install Dependencies

> ⚠️ **Required:** Due to GitHub file size limits, download the trained model binary `bank_model.pkl` from [this Google Drive link](https://drive.google.com/file/d/1XE2-j9askzmLlOLuMKE7EojMTNbyFoLM/view?usp=sharing) and place it in the **root directory** of this project before starting the server.
>
> **Before doing this:** treat any `.pkl` file from a link you don't control as untrusted. `pickle.load()` can execute arbitrary code on your machine. Verify the source/owner of this link before downloading, or ask them to provide the model in a safer format (e.g. ONNX, or weights as JSON).

Make sure Python is installed, then from the project root run:

```bash
pip install -r requirements.txt
```

### Step 2: Configure Environment Credentials

To enable live Llama-3.3 explanation generation, set your Groq API key as an environment variable.

**Git Bash / Linux / macOS:**
```bash
export GROQ_API_KEY="your_actual_api_key_here"
```

**Windows (cmd):**
```cmd
set GROQ_API_KEY=your_actual_api_key_here
```

**Windows (PowerShell):**
```powershell
$env:GROQ_API_KEY="your_actual_api_key_here"
```

> 💡 **Note:** If no key is set, the app falls back to baseline internal text generation instead of live LLM calls.

### Step 3: Start the Server

From the project root, run:

```bash
python -m uvicorn main:app --reload
```

Once the server starts, view the interactive API docs at:
**http://127.0.0.1:8000/docs**

---

## Part 2: API Endpoints & Example Usage

Keep the server running in one terminal, and use a second terminal to test these endpoints with `curl`.

### 1. Health Check — `GET /health`

Checks that the app is running and the model loaded successfully.

```bash
curl -X 'GET' 'http://127.0.0.1:8000/health' -H 'accept: application/json'
```

**Example response:**
```json
{
  "status": "ok",
  "model": "RandomForestClassifier-TrackC"
}
```

### 2. Predict — `POST /predict`

Takes a customer profile and returns subscription probability and top contributing factors.

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/predict' \
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
```

**Example response:**
```json
{
  "will_subscribe": true,
  "probability": 0.83,
  "top_factors": [
    "extended communication conversation length",
    "absence of active housing debt obligations"
  ]
}
```

### 3. Explain — `POST /explain`

Routes prediction results through a Llama-3.3 model (via Groq) to generate a plain-language pitch summary for bank staff.

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/explain' \
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
```

**Example response (with key configured):**
```json
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
```


