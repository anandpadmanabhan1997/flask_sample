from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome"

@app.route("/hello", methods=["GET"])
def hello():
    name = request.args.get("name", "Guest")
    return f"Hello, {name}!"

@app.route("/echo", methods=["POST"])
def echo():
    data = request.get_json()
    return jsonify({"you_sent": data})


if __name__=="__main__":
    app.run(host='0.0.0.0', port=5000)