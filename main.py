from flask import Flask, request, redirect, render_template
import cgi
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    template = jinja_env.get_template('homepage.html')
    return render_template('homepage.html')

@app.route("/add", methods=['POST'])
def add():
    username= request.form['username']
    password= request.form['password']
    verify= request.form['verify']
    email= request.form['email']

    username_error= ""
    password_error= ""
    verify_error=""
    email_error=""

    if username == "":
        username_error = "You didn't write anything, come on man!"
    elif len(username) <=3 or len(username) >20:
        username_error = "Invalid length of username you imbacile!"
        
    if verify =="" or verify != password:
        verify_error = "Passwords do not match! Why are you so stupid!"
        verify = ""

    if email == "":
        email_error = "That email won't work, duh..."
    elif "@" not in email:
        email_error = "Need @ in email faker..."
    elif "." not in email:
        email_error = "Need . in email faker..."

    if len(password) <3 or len(password) >20:
        password_error = "Password must be between 3 and 20 characters you illiterate dummy!"
    elif " " in password:
        password_error = "No empty spaces in the password fool!"
    elif password == "":
        password_error = "You didn't write anything for the password brosef..."

    

    if not username_error and not password_error and not verify_error and not email_error:
       return render_template('welcome.html', username=username)
    else:
       return render_template('homepage.html',
                              username=username, username_error=username_error,
                              password_error=password_error,
                              verify_error=verify_error,
                              email=email, email_error=email_error)

if __name__ == "__main__":
    app.run()