from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"*": {"origins": "*"}})

@app.route("/")
def index():
    slackUsername = "Nathaniel"
    backend = True
    age = 28
    bio = "Software developer and technical writer"

    response = {
        "slackUsername": slackUsername,
        "backend": backend,
        "age": age,
        "bio": bio
    }

    return response

if __name__ == ("__main__"):
    app.run(debug=True)