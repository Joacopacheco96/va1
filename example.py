from flask import Flask
# from thomas import *

app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     print('loaded')
#     thomas.apply_async()
#     return "<p>Hello, World!</p>"
@app.route('/')
def index():
#   return render_template('index.html')
    # return "<p>Hello, World!</p>"
  return "<button> <a href="/my-link/">Click me</a></button>"

@app.route('/my-link/')
def my_link():
  print ('I got clicked!')

  return 'Click.'

if __name__ == '__main__':
  app.run(debug=True)