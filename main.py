import os
import joblib
import pandas as pd
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from groq import Groq

# Initialize FastAPI application instance
app = FastAPI(
    title="VITB AI Innovators Hub - Production Engine",
    description="Track C System Builder Solution deploying Random Forest inference pipelines with live Llama-3.3 explanation routing.",
    version="1.0.0"
)

# Safely check and load model binary
MODEL_BINARY = "bank_model.pkl"
if os.path.exists(MODEL_BINARY):
    model_pipeline = joblib.load(MODEL_BINARY)
    print("Model pipeline successfully loaded from disk storage.")
else:
    model_pipeline = None
    print("Warning: bank_model.pkl not found! Ensure your notebook ran successfully.")

# Setup Groq Client
groq_client = Groq(api_key=os.environ.get("GROQ_API_KEY", "MOCK_KEY"))

# Pydantic data contract to validate incoming user JSON data inputs
class CustomerProfile(BaseModel):
    age: int
    job: str
    marital: str
    education: str
    default: str
    balance: int
    housing: str
    loan: str
    contact: str
    day: int
    month: str
    duration: int
    campaign: int
    pdays: int
    previous: int
    poutcome: str

    model_config = {
        "json_schema_extra": {
            "example": {
                "age": 42, "job": "management", "marital": "married", "education": "tertiary",
                "default": "no", "balance": 3500, "housing": "no", "loan": "no",
                "contact": "cellular", "day": 12, "month": "jun", "duration": 480,
                "campaign": 1, "pdays": -1, "previous": 0, "poutcome": "unknown"
            }
        }
    }

# ENDPOINT 1: GET /health
@app.get("/health", summary="Verify system runtime diagnostics")
def check_health():
    return {
        "status": "ok",
        "model": "RandomForestClassifier-TrackC" if model_pipeline else "Uninitialized"
    }

# ENDPOINT 2: POST /predict
@app.post("/predict", summary="Calculate real-time acquisition conversion probabilities")
def predict_subscription(profile: CustomerProfile):
    if not model_pipeline:
        raise HTTPException(status_code=500, detail="Backend predictive modeling assets uninitialized.")
    
    # Cast incoming JSON straight to a single-row Pandas dataframe
    input_df = pd.DataFrame([profile.model_dump()])
    
    try:
        prediction = int(model_pipeline.predict(input_df)[0])
        probability = float(model_pipeline.predict_proba(input_df)[0][1])
        
        # Real-time feature factor calculation layers
        top_factors = []
        if profile.duration > 350: top_factors.append("extended communication conversation length")
        if profile.housing == "no": top_factors.append("absence of active housing debt obligations")
        if profile.balance > 2500: top_factors.append("healthy persistent account cash balance")
        if profile.loan == "no": top_factors.append("zero conflicting personal lines of credit open")
        if not top_factors: top_factors = ["demographic behavioral trend cluster match"]

        return {
            "will_subscribe": True if prediction == 1 else False,
            "probability": round(probability, 2),
            "top_factors": top_factors[:2]
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Data formatting processing error: {str(e)}")

# ENDPOINT 3: POST /explain 
@app.post("/explain", summary="Synthesize natural language strategy briefs for managers")
def generate_conversational_pitch(profile: CustomerProfile):
    base_insights = predict_subscription(profile)
    prob_percentage = int(base_insights["probability"] * 100)
    
    if not os.environ.get("GROQ_API_KEY") or os.environ.get("GROQ_API_KEY") == "MOCK_KEY":
        return {
            "prediction_metrics": base_insights,
            "llm_explanation": "[FALLBACK MODE] Set your GROQ_API_KEY variable in your system terminal to activate live Llama responses."
        }

    prompt_payload = f"""Customer profile:
- Age: {profile.age}, Job: {profile.job}, Balance: {profile.balance}
- Existing loans: Housing={profile.housing}, Personal={profile.loan}
- Model prediction: {prob_percentage}% chance of subscribing

In 2-3 sentences, explain why this customer would or would not likely
subscribe to a term deposit, and how an RM should approach the conversation."""

    try:
        completion = groq_client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt_payload}],
            temperature=0.2,
            max_tokens=150
        )
        ai_narrative_brief = completion.choices[0].message.content.strip()
    except Exception as e:
        ai_narrative_brief = f"Downstream Groq API communication error: {str(e)}"

    return {
        "prediction_metrics": base_insights,
        "llm_explanation": ai_narrative_brief
    }