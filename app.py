# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, DevOps World! This was built by Jenkins!'

if __name__ == '__main__':
    # Run the app on all interfaces on port 5000
    app.run(debug=True, host='0.0.0.0', port=5000)
