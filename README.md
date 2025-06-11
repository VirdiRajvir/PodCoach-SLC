# PodCoach-SLC

PodCoach-SLC is a Flask-based AI coaching web application that generates personalized coaching scripts, converts them to audio, and provides an interactive chat for users.

---

## Features

- User selects a goal and receives a personalized AI-generated coaching script.
- Script is converted to speech and played as audio.
- Interactive chat with the AI coach about the session.
- Feedback collection and session summary.

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/PodCoach-SLC.git
cd PodCoach-SLC
```

### 2. Create and Activate a Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

If you don't have a `requirements.txt`, generate it with:

```bash
pip freeze > requirements.txt
```

### 4. Set Environment Variables

Create a `.env` file or set the following environment variable in your shell:

```bash
export SECRET_KEY='your_secret_key_here'
```

### 5. Set LLM for chat response

The current system uses locally run Llama3 using Ollama. Users have two choices:
1. Use Local Ollama models:
   - Install ollama at https://ollama.com/
   - Pull a chosen model:
   ```bash
   ollama pull llama3
   ```
   - Modify generate_response.py to use your pulled model
2. Use API based models:
   - Modify generate_response.py to use other models, returning content of LLM response

---

## Usage

### 1. Run the Flask App

```bash
flask run
```


### 2. Access the App

Open your browser and go to:  
[http://localhost:5000](http://localhost:5000)

---

## File Structure

- `app.py` — Main Flask application with all routes and session management.
- `generate_script.py` — Generates personalized coaching scripts.
- `generate_audio.py` — Converts scripts to audio using gTTS.
- `generate_response.py` — Handles AI chat responses.
- `templates/` — HTML templates for the web interface.
- `static/` — Static files (audio, images, feedback, etc.).

---

## Notes

- Make sure you have [gTTS](https://pypi.org/project/gTTS/) and other required packages installed.
- Make sure you have Ollama running locally with Llama3 installed, or 
