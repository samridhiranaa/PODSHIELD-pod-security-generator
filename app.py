from flask import Flask, request
from generator import generate_policy

app = Flask(__name__)

@app.route('/generate', methods=['POST'])
def generate():

    data = request.json

    image = data["image"]
    allow_root = data["allow_root"]

    policy = generate_policy(image, allow_root)

    return policy

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)