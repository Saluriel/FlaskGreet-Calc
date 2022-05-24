from flask import Flask

app = Flask(__name__)

@app.route('/')
def home_page():
    """Home page, links to other pages"""
    return """<h1>Welcome to the home page</h1>
    <a href=/welcome>Welcome</a> |
    <a href=/welcome/home>Welcome Home</a> |
    <a href=/welcome/back>Welcome Back"""

@app.route('/welcome')
def welcome():
    """prints welcome"""
    return "welcome"

@app.route('/welcome/home')
def welcome_home():
    """prints welcome home"""
    return "welcome home"

@app.route('/welcome/back')
def welcome_back():
    """prints welcome back"""
    return "welcome back"