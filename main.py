from flask import Flask, url_for
from flask.templating import render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Email, Length

admin_credentials = {
    "email": "admin@email.com",
    "password": "12345678"
}

app = Flask(__name__)
Bootstrap(app)
app.secret_key = "1597536428".encode('utf8')

class SignupForm(FlaskForm):
    email = StringField(label='Email', validators=[Email(), Length(min=4)])
    password = PasswordField(label='Password', validators=[Length(min=8, max=12)])
    submit = SubmitField(label='Log In')

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    login_form = SignupForm()
    login_form.validate_on_submit()
    if login_form.validate_on_submit():
        email = login_form.email.data
        password = login_form.password.data
        if email == admin_credentials["email"] and password == admin_credentials["password"]:
            return app.redirect(url_for("logged"))
        else:
            return app.redirect(url_for("denied"))
    return render_template("login.html", form=login_form)

@app.route("/logged")
def logged():
    return render_template("success.html")

@app.route("/denied")
def denied():
    return render_template("denied.html")

if __name__ == '__main__':
    app.run(debug=True)