from flask import Flask, render_template, request, redirect, url_for, jsonify, session
from generate_script import generate_script
from generate_audio import generate_audio
from generate_response import generate_response, append_message
import os
from langchain_ollama import ChatOllama
import time
app = Flask(__name__)
app.secret_key = os.getenv('ELEVENLABS_API_KEY')

@app.route('/', methods=['GET', 'POST'])
def landing():
    print(session)
    session.clear()
    # session['messages'] = []
  # Clear session on landing page
    if request.method == 'POST':
        session['username'] = request.form.get('username')
        if not session['username']:
            error = "Please enter your name."
            return render_template('landing.html', error=error)
        # Redirect to goal_selection with username in query string
        return redirect(url_for('goal_selection', username=session['username']))
    return render_template('landing.html')


@app.route('/goal_selection', defaults={'goal': None})
@app.route('/goal_selection/<goal>')
def goal_selection(goal=None):
    print(session)
    # session['username'] = request.args.get('username')
    if goal is None:
        # No goal selected yet — show list of goals
        goals = ["Focus", "Confidence", "Motivation"]
        return render_template('goal_selection.html', goals=goals, username=session.get('username'))
    else:
        # Goal is selected — show confirmation or next step
        session['goal'] = goal
        return redirect(url_for('start_coaching'))

@app.route('/start_coaching', methods=['POST'])
def start_coaching():
    print(session)
    # session['goal'] = request.form.get('goal')
    # username = request.form.get('username')
    if not session.get('goal'):
        goal = request.form.get('goal')
        if goal:
            session['goal'] = goal
    # 1. Generate script
    session['script'], session['summary'] = generate_script(session.get('goal'), session.get('username'))
    session['messages'] = [
        {
            "role": "system",
            "content": f"You are a coach. You are given a transcript of a coaching session you just conducted. Your task is to answer any questions about the session, and also to provide answers to questions the client may ask. Here is the transcript: {session['script']}"
        }
    ]
    # 2. Generate audio from script
    session['audio_file'] = generate_audio(session.get('script'), session.get('username'), session.get('goal'))  # returns something like 'static/audio/abc123.mp3'

    # with open('static/script/coaching_script.txt', 'r') as file:
    #     script = file.read()
    # audio_file = 'static/audio/generated_audio.mp3'
    audio_url = '/' + session['audio_file'] + f'?v={int(time.time())}'


    # 3. Redirect to coaching page with audio
    return render_template('coaching.html', goal=session.get('goal'), script=session.get('script'), audio_url=audio_url, username=session.get('username'))


@app.route('/summary')
def summary():
    print(session)
    # with open('static/summary/summary.txt', 'r') as file:
    #     summary_content = file.read()
    # with open('static/script/coaching_script.txt', 'r') as file:
    #     coaching_script = file.read()
    return render_template('summary.html', summary=session.get('summary'), script=session.get('script'))

@app.route('/feedback', methods=['GET'])
def feedback(): 
    print(session)
    return render_template('feedback.html')

@app.route('/submit_feedback', methods=['POST'])
def submit_feedback():
    print(session)
    feedback = request.form.get('feedback')
    if not feedback:
        return "No feedback provided", 400

    if os.path.exists('static/feedback/feedback.txt'):
        with open('static/feedback/feedback.txt', 'r') as file:
            existing_feedback = file.read()
        if feedback in existing_feedback:
            return redirect(url_for('feedback_thanks'))
    else:
        existing_feedback = ""
    # Here you would typically save the feedback to a database or file
    with open('static/feedback/feedback.txt', 'a') as file:
        file.write(feedback + '\n')

    return redirect(url_for('feedback_thanks'))


@app.route('/feedback_thanks', methods=['GET'])
def feedback_thanks():
    return render_template('feedback_thanks.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    if not data or 'message' not in data:
        return jsonify({'error': 'No message provided'}), 400

    user_message = data['message']
    coach_reply = generate_response(user_message, session)
    append_message(coach_reply, session)

    return jsonify({'response': coach_reply})