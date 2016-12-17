from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    greeting = "Hello World"
    render = render_template('index.html', greet = greeting)
    return greeting

if __name__ == "__main__":
    app.run()
