from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

# after working change silly story
from stories import silly_story as story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.get('/')
def show_question():
    """Generates an input form for story prompts"""
    prompts = story.prompts

    return render_template("questions.html", prompts = prompts)

@app.get('/story')
def show_results():
    """Displays the story with user inputs"""
    result = story.generate(request.args)

    return render_template("results.html", text = result)
