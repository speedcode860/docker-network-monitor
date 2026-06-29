from flask import Flask, jsonify, request
import os
import time

app = Flask(__name__)
start_time = time.time()

@app.route("/health", methods=["GET"])
def health():
    return jsonify(status="UP"), 200

@app.route("/info", methods=["GET"])
def info():
    return jsonify(
        service="network-monitor",
        hostname=os.uname().nodename
    ), 200

@app.route("/metrics", methods=["GET"])
def metrics():
    uptime = int(time.time() - start_time)
    return jsonify(
        uptime_seconds=uptime
    ), 200

@app.route("/reload", methods=["POST"])
def reload():
    return jsonify(message="Configuration reloaded"), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
