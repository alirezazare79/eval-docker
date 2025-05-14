from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return f"Hello from Flask! DB: {os.getenv('POSTGRES_DB')}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
