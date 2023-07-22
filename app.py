from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return f"Udacity Cloud Devops Capstone project by RBT"
app.run(host="0.0.0.0", port=80)
