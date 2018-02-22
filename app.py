from flask import Flask
application = Flask(__name__)

@app.route('/')
def hello_worlsoud():
    return 'Hello, World!'

if __name__ == "__main__":
  application.run(host='0.0.0.0', port=8000)