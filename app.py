from flask import Flask, request, render_template, jsonify
from generator import generate_policy

app = Flask(__name__)

# -----------------------------
# Home Page (UI)
# -----------------------------
@app.route("/")
def home():
    return render_template("index.html")


# -----------------------------
# Generate Security Policy API
# -----------------------------
@app.route("/generate", methods=["POST"])
def generate():

    data = request.json

    if not data:
        return jsonify({"error": "Invalid request"}), 400

    image = data.get("image")
    allow_root = data.get("allow_root", False)
    profile = data.get("profile", "baseline")   # default profile

    if not image:
        return jsonify({"error": "Container image is required"}), 400

    # Generate policy using generator module
    policy = generate_policy(image, allow_root, profile)

    return policy


# -----------------------------
# Health Check Endpoint
# (useful for Kubernetes)
# -----------------------------
@app.route("/health")
def health():
    return {"status": "PodShield running"}


# -----------------------------
# Run Flask App
# -----------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)