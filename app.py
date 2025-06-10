from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/greet/<name>')
def greet(name):
    return f'Hello, {name}!'

@app.route('/goalselection')
def goal_selection():
    return 'Goal Selection Page'

@app.route('/goal_selection/<goal>')
def goal_selection_with_param(goal):
    return f'Goal Selection for: {goal}'

@app.route('/goal_selection/<goal>/coaching')
def goal_selection_coaching(goal):
    return f'Coaching for Goal: {goal}'

@app.route('/goal_selection/<goal>/coaching/summarypage')
def goal_selection_coaching_summary(goal):
    return f'Summary Page for Coaching Goal: {goal}'

@app.route('/goal_selection/<goal>/coaching/feedback')
def goal_selection_coaching_feedback(goal):
    return f'Feedback for Coaching Goal: {goal}'