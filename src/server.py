from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/open', methods=['POST'])
def index():
    content = request.json
    print(content)
    return jsonify({"status":"ok"})