from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

# after working change silly story
from stories import excited_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)
@app.get('/')
def show_question():
    prompts = excited_story.prompts

    return render_template("questions.html", prompts = prompts)
