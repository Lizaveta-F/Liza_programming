from flask import Flask
import random

app = Flask(__name__)


@app.route('/')
def main_page():
    return '<h1>Guess a number between 0 and 9</h1>\
        <img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'

random_number = random.randint(0,9)

@app.route('/<int:input_number>')
def guess_number(input_number):
    if random_number>input_number:
        return "<h1>It is too low, try again</h1><img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
    elif random_number<input_number:
        return "<h1>It is too high, try again</h1><img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"
    else:
        return '<h1>Congratulations! You got it!</h1><img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'

if __name__=="__main__":
    app.run(debug=True)


