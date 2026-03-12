from flask import Flask, request, render_template, jsonify
from generator import generate_policy
from cluster_scanner import scan_cluster
from security_analyzer import analyze_security
from ai_advisor import generate_advice
from security_score import calculate_security_score
from yaml_scanner import scan_yaml
app = Flask(__name__)
# Home Page (UI)
@app.route("/")
def home():
    return render_template("index.html")
# Generate Security Policy API
@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid request"}), 400
    image = data.get("image")
    allow_root = data.get("allow_root", False)
    profile = data.get("profile", "baseline")
    if not image:
        return jsonify({"error": "Container image is required"}), 400
    try:
        policy = generate_policy(image, allow_root, profile)
        # return raw YAML text
        return policy, 200, {"Content-Type": "text/plain"}
    except Exception as e:
        return jsonify({"error": str(e)}), 500
# Kubernetes Cluster Scanner API
@app.route("/scan")
def scan():
    try:
        pods = scan_cluster()
        issues = analyze_security(pods)
        advice = generate_advice(pods)
        score, breakdown = calculate_security_score(pods)
        return jsonify({
            "pods": pods,
            "issues": issues,
            "advice": advice,
            "score": score,
            "breakdown": breakdown
        })
    except Exception as e:
        return jsonify({
            "error": "Cluster scan failed",
            "details": str(e)
        }), 500
# Health Check Endpoint
@app.route("/health")
def health():
    return jsonify({
        "status": "PodShield running"
    })
@app.route("/scan-yaml", methods=["POST"])
def scan_yaml_api():
    data = request.json
    yaml_text = data.get("yaml")
    issues, fixes = scan_yaml(yaml_text)
    return jsonify({
        "issues": issues,
        "fixes": fixes
    })
# Run Flask App
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)