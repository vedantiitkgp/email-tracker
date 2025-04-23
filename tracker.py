from flask import Flask, request, send_file, make_response
from datetime import datetime
import os

app = Flask(__name__)

@app.route('/tracker.gif')
def tracker():
    email = request.args.get("email", "unknown")
    with open("opens.log", "a") as f:
        f.write(f"{datetime.now()} - Opened by {email}\n")
    print(f"{datetime.now()} - Email opened by {email}")
    response = make_response(send_file("tracker.gif", mimetype="image/gif"))
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    return response

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Use Render's assigned port
    app.run(host="0.0.0.0", port=port)