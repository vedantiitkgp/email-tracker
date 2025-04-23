from flask import Flask, request, send_file, make_response, Response
from datetime import datetime
import os

app = Flask(__name__)
LOG_FILE = "opens.log"

@app.route("/tracker.gif")
def tracker():
    email = request.args.get("email", "unknown")
    uid = request.args.get("uid", "none")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open(LOG_FILE, "a") as f:
        f.write(f"{timestamp} - {email} (UID: {uid})\n")

    print(f"Email opened by {email} D: {uid}) at {datetime.now()}")
    response = make_response(send_file("tracker.gif", mimetype="image/gif"))
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    return response

@app.route("/logs")
def logs():
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            content = f.read()
        return Response(content, mimetype="text/plain")
    else:
        return "No logs yet."

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Use Render's assigned port
    app.run(host="0.0.0.0", port=port)