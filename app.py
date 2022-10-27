from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"*": {"origins": "*"}})

@app.route("/", methods=["GET"])
def index():
    slackUsername = "string"
    backend = True
    age = 28
    bio = "Am a developer who loved coding in python"

    response = {
        "slackUsername": slackUsername,
        "backend": backend,
        "age": age,
        "bio": bio
    }

    return response

if __name__ == ("__main__"):
    app.run(debug=True)