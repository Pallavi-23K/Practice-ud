#The part before .route must be the Flask app instance name (not the filename).
#Both decorators should use the same app instance (e.g., app or jinja), not different ones.
#Just create one app instance (commonly called app):
from flask import Flask

app=Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to the flask application!"

@app.route("/index")
def index():
    return "This is the my index page."

if __name__=="__main__":
    app.run(debug=True)
    ''' debug is used to enable debug mode in Flask, 
    which provides helpful error messages and automatic reloading during development.'''
