"""
flask app to do things on a raspberry pi
"""

from flask import Flask, request, render_template
import requests
import sys

from voice_commands import parser

def create_app():
  app = Flask(__name__)
  app.secret_key = 'fjp98j4389c398caoaw993823'
  return app

app = create_app()

@app.route('/', methods=['GET', 'POST'])
def index():
  return 'Welcome to 3.1415926535...'


@app.route('/tester')
def tester():
  return render_template('tester.jinja.html')


@app.route('/speech', methods=['GET', 'POST'])
def speech():
  if request.method == 'POST':
    # return 'You said ' + request.form['text']
    print "Received the following command", request.form['text']
    desired_action = parser.parse(request.form['text'])
    desired_action()
    return 'listen, biatch'
  return render_template('speech.html')


if __name__ == "__main__":
  port = int(sys.argv[1]) if len(sys.argv) > 1 else 5000
  app.run(debug=True, host='0.0.0.0', port=port, use_reloader=True)
