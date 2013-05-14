"""
flask app to do things on a raspberry pi
"""

from flask import Flask, request, render_template

def create_app():
  app = Flask(__name__)
  app.secret_key = 'fjp98j4389c398caoaw993823'
  return app

app = create_app()

@app.route('/', methods=['GET', 'POST'])
def index():
  return 'Welcome to 3.1415926535...'

@app.route('/voice', methods=['GET', 'POST'])
def voice():
  """
  run a voice command
  """
  if request.method == 'POST':
    print request.files
    return "this isn't done yet"
  return render_template('voice.jinja.html')

if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0', use_reloader=True)
