import os
from flask import Flask
app = Flask(__name__)

#orig_message=os.environ.get('ORIG_MESSAGE')
orig_message = 'Tony'

@app.route("/")
def hello():
  return orig_message

if __name__ == "__main__":
  app.run()