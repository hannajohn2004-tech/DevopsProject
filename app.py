from flask import Flask
import datetime

app = Flask(__name__)

def log_visitor():
    with open("visitors.txt", "a") as f:
        f.write(str(datetime.datetime.now()) + "\n")

def get_visitors():
    try:
        with open("visitors.txt", "r") as f:
            return f.readlines()
    except:
        return []

@app.route('/')
def home():
    return """
    <h1>Hi, I'm Hanna 💜</h1>
    <p>3rd Year CSE Student</p>
    <p>Skills: Java, Python, Web Development, DevOps Basics</p>
    <p>Project: Visitor Tracking System with Docker</p>
    <a href='/visit'>Visit Page</a><br>
    <a href='/visitors'>View Visitors</a>
    """

@app.route('/visit')
def visit():
    log_visitor()
    return "<h3>Visit recorded!</h3><a href='/'>Go Back</a>"

@app.route('/visitors')
def visitors():
    data = get_visitors()
    output = "<h2>Visitor Logs:</h2>"
    for d in data:
        output += f"<p>{d}</p>"
    return output

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
