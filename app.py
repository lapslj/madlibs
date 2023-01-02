from flask import Flask, request, render_template
from stories import Story, story

app = Flask(__name__)

#convert story to HTML structure

@app.route('/story')
def buildstory():
    answers = {}
    answers['place'] = request.args.get('place')
    answers['noun'] = request.args.get('noun')
    answers['verb'] = request.args.get('verb')
    answers['adjective'] = request.args.get('adjective')
    answers['plural_noun'] = request.args.get('plural_noun')
    result = story.generate(answers)
    return result

@app.route('/form')
def form():
    prompts = story.prompts
    return render_template("index.html",prompts=prompts)