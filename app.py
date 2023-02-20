from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import Story, story, story2
app = Flask(__name__)


@app.route('/')
def home_page_select():
    return render_template('home.html')


@app.route('/form')
def word_prompt_form():
    if request.args['stories'] == 'story1':
        return render_template('form.html', story=story, story_id=1)
    elif request.args['stories'] == 'story2':
        return render_template('form.html', story=story2, story_id=2)


@app.route('/story', methods=['POST'])
def show_story():
    if request.form['story_id'] == '1':
        new_story = story.generate(request.form)
        return render_template('story.html', story=new_story)
    elif request.form['story_id'] == '2':
        new_story = story2.generate(request.form)
        return render_template('story.html', story=new_story)
