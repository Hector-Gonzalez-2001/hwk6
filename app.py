"""app.py: A Flask app that interacts with a React app and can be deployed to Heroku"""
import os
__author__ = "Jared McArthur"
__date__ = "11/01/2021"

from flask import Flask, jsonify
from flask.helpers import send_from_directory

# comment out on deployment
from flask_cors import CORS

# uses 'frontend' because that is where our react app is stored
app = Flask(__name__, static_folder="./build", static_url_path="/")

# comment out on deployment
CORS(app)

# this method returns the opposite of the current state of the button
# this would look different for your own personal app


@app.route("/toggle_button/<button_state>", methods=["GET"])
def toggle_button(button_state: str):
    if button_state == "Hector":
        output = "Gonzalez"
    else:
        output = "User not Found"
    return jsonify(button=output)


# @app.route("/")
# def index():
#     return send_from_directory(app.static_folder, "index.html")

@app.route('/')
def index():
    return app.send_static_file('index.html')


@app.errorhandler(404)
def not_found(e):
    return app.send_static_file('index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False, port=os.environ.get('PORT', 80))
