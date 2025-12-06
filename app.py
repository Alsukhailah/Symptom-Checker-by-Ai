import os
import json
from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if GOOGLE_API_KEY:
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel('gemini-2.0-flash')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze_symptoms():
    try:
        if not GOOGLE_API_KEY:
             return jsonify({"error": "error: There is no API_Key in the file .env"}), 500

        data = request.json
        
        user_symptoms = data.get('symptoms', '')
        severity = data.get('severity', 5)
        duration = data.get('duration', 'Not specified')
        associated = data.get('associated', []) 
        history = data.get('history', 'None')
        meds = data.get('meds', 'None')

        associated_str = ", ".join(associated) if associated else "None"

        prompt = f"""
        Act as a professional medical AI assistant. 
        
        Patient Data:
        - Main Symptom: "{user_symptoms}"
        - Severity: {severity}/10
        - Duration: {duration}
        - Associated Symptoms: {associated_str}
        - Medical History: {history}
        - Current Medications: {meds}
        
        Analyze this data carefully. Check for drug interactions if medications are listed.
        
        Return the output strictly as a JSON object with the following structure (no markdown):
        {{
            "conditions": [
                {{"name": "Condition Name", "prob": probability_integer, "severity": "Mild/Moderate/Severe", "color": "green/yellow/red"}}
            ],
            "steps": ["Step 1", "Step 2", "Step 3", "Step 4"],
            "note": "A concise clinical summary explaining the diagnosis based on the history and symptoms provided."
        }}
        
        Rules:
        1. "prob" must be a number between 0 and 100.
        2. "color" logic: green (low risk), yellow (medium risk), red (high risk).
        3. Provide exactly 3 possible conditions sorted by probability.
        """

        response = model.generate_content(prompt)
        response_text = response.text.replace('```json', '').replace('```', '').strip()
        result_json = json.loads(response_text)
        
        return jsonify(result_json)

    except Exception as e:
        print(f"Server Error: {e}") 
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    print("Starting Flask Server...")
    app.run(debug=True, port=5000)