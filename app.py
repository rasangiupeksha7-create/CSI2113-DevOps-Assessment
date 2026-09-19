from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome to My DevOps Web Application</h1><p>CSI2113 Practical Assessment</p>"

@app.route("/about")
def about():
    return "<h2>About</h2><p>This application demonstrates a DevOps CI/CD workflow.</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)