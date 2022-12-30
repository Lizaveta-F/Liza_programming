from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

app = Flask(__name__)
app.secret_key = "some secret string"

@app.route("/")
def home():
    return render_template('index.html')


class LoginForm(FlaskForm):
    email = StringField(label='Email', validators= [DataRequired(), Email()])
    password = PasswordField(label='Password', validators= [DataRequired(), Length(min=8)])
    submit = SubmitField(label = "Log in")

@app.route('/login', methods = ["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return render_template('success.html')
    else:
        return render_template('denied.html')
    # return render_template('login.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)