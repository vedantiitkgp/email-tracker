from flask import Flask, request, send_file
from datetime import datetime

app = Flask(__name__)

@app.route('/tracker.gif')
def tracker():
    email = request.args.get("email", "unknown")
    with open("opens.log", "a") as f:
        f.write(f"{datetime.now()} - Opened by {email}\n")
    return send_file("tracker.gif", mimetype="image/gif")
