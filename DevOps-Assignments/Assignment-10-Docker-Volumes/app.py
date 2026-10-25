from flask import Flask
from datetime import datetime
import os

app = Flask(__name__)
LOG_DIR = "/app/data"
LOG_FILE = os.path.join(LOG_DIR, "visits.log")

@app.route("/")
def home():
    os.makedirs(LOG_DIR, exist_ok=True)
    message = f"Hello from Docker! Time: {datetime.now().isoformat()}"
    with open(LOG_FILE, "a") as f:
        f.write(message + "\n")
    return f"<h1>{message}</h1><p>Visit logged persistently.</p>"

@app.route("/logs")
def logs():
    if not os.path.exists(LOG_FILE):
        return "No logs yet."
    with open(LOG_FILE) as f:
        return "<pre>" + f.read() + "</pre>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
