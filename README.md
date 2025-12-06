# Symptom-Checker-by-Ai

A smart AI-powered web application that analyzes symptoms using **Google Gemini 2.0 Flash**. It features Voice Input (Speech-to-Text), AI Voice Results (Text-to-Speech), and downloadable health reports.

## Features
- **AI Diagnosis:** Analyzes symptoms, severity, and medical history.
- **Voice Input:** Speak your symptoms instead of typing.
- **AI Voice:** The app reads the diagnosis summary aloud.
- **Smart Reports:** Download results as a text file for your records.
- **Responsive Design:** Clean and modern UI using Tailwind CSS.

---

## How to Run (Installation Guide)

Follow these steps to set up and run the project on your machine.

### 1. Prerequisites
- **Python 3.10+** installed on your system.
- A **Google Gemini API Key** (Get it free from [Google AI Studio](https://aistudio.google.com/)).

### 2. Clone the Repository
Open your terminal and run:
```bash
git clone https://github.com/Alsukhailah/Symptom-Checker-by-Ai.git
cd Symptom-Checker-by-Ai
```

### 3. Create a Virtual Environment (Recommended)
This keeps your project isolated.

For Mac/Linux:

```bash

python3 -m venv venv
source venv/bin/activate
```

For Windows:

```bash

python -m venv venv
venv\Scripts\activate
```

4. Install Dependencies
Install the required libraries (Flask, Google Generative AI, etc.):

```bash

pip install -r requirements.txt
```

5. Set Up API Key 
To keep your key safe, we use environment variables.

Create a new file named .env in the main folder.
put your API Key here
```bash
echo "GOOGLE_API_KEY=YOUR_REAL_API_KEY_HERE" > .env
```
To make sure
```bash
cat .env
```
6. Run the Application
Start the local server:

```bash

python app.py
You should see: Running on http://127.0.0.1:5000
```

Disclaimer: This tool is for informational purposes only and does not replace professional medical advice.
