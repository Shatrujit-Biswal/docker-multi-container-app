from flask import Flask, jsonify
import redis
import os

app = Flask(__name__)

REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))

r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

@app.route("/")
def home():
    return "<h2>Docker Multi-Container Demo</h2><p>Go to /api/visits</p>"

@app.route("/api/visits")
def visits():
    try:
        count = r.incr("visits")
        return jsonify({"visits": int(count)})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
