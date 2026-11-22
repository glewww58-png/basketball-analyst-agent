from flask import Flask, request, jsonify
from agent import handler   # import the function defined in agent.py

app = Flask(__name__)

@app.post("/api/run")
def run_agent():
    payload = request.get_json(silent=True) or {}
    msg = payload.get("message")
    if not msg:
        return jsonify({"error": "Missing 'message' field"}), 400

    try:
        answer = handler(msg)
        return jsonify({"response": answer})
    except Exception as exc:
        # In production you would log `exc` to a monitoring service
        return jsonify({"error": str(exc)}), 500

if __name__ == "__main__":
    # Local development only – Vercel will use gunicorn
    app.run(host="0.0.0.0", port=8080)
