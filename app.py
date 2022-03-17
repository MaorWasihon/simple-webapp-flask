import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "<h1>My name is Tony Montoya. </h1>
		<h1>And I'm ... </h1>
		<h1>===> THE KING OF THE JUNGLE <===</h1>"

@app.route('/how are you')
def hello():
    return 'I am good, how about you?'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
