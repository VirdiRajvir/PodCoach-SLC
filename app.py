from flask import Flask, render_template, request, redirect, url_for, jsonify
from generate_script import generate_script
from generate_audio import generate_audio
from generate_response import generate_response, append_message
import os
from langchain_ollama import ChatOllama
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def landing():
    if request.method == 'POST':
        username = request.form.get('username')
        if not username:
            error = "Please enter your name."
            return render_template('landing.html', error=error)
        # Redirect to goal_selection with username in query string
        return redirect(url_for('goal_selection', username=username))
    return render_template('landing.html')


@app.route('/goal_selection', defaults={'goal': None})
@app.route('/goal_selection/<goal>')
def goal_selection(goal=None):
    username = request.args.get('username')
    if goal is None:
        # No goal selected yet — show list of goals
        goals = ["Focus", "Confidence", "Motivation"]
        return render_template('goal_selection.html', goals=goals, username=username)
    else:
        # Goal is selected — show confirmation or next step
        return render_template('coaching.html', goal=goal, username=username)


@app.route('/start_coaching', methods=['POST'])
def start_coaching():
    goal = request.form.get('goal')
    username = request.form.get('username')
    if not goal:
        return "No goal provided", 400

    # 1. Generate script
    script = generate_script(goal, username)

    # 2. Generate audio from script
    audio_file = generate_audio(script, username, goal)  # returns something like 'static/audio/abc123.mp3'

    # with open('static/script/coaching_script.txt', 'r') as file:
    #     script = file.read()
    # audio_file = 'static/audio/generated_audio.mp3'


    # 3. Redirect to coaching page with audio
    return render_template('coaching.html', goal=goal, script=script, audio_url='/' + audio_file, username=username)


@app.route('/summary')
def summary():
    with open('static/summary/summary.txt', 'r') as file:
        summary_content = file.read()
    with open('static/script/coaching_script.txt', 'r') as file:
        coaching_script = file.read()
    return render_template('summary.html', summary=summary_content, script=coaching_script)

@app.route('/feedback', methods=['GET'])
def feedback(): 
    return render_template('feedback.html')

@app.route('/submit_feedback', methods=['POST'])
def submit_feedback():
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
    coach_reply = generate_response(user_message)
    append_message(coach_reply)

    return jsonify({'response': coach_reply})