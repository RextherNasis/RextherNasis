from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to Rexther's Flask API",
        "status": "API is running"
    })

@app.route('/api/greet', methods=['GET'])
def greet():
    name = request.args.get('name', 'Guest')
    return jsonify({
        "message": f"Hello {name}, welcome to the API!"
    })

@app.route('/api/add', methods=['GET'])
def add_numbers():
    num1 = request.args.get('num1', 0)
    num2 = request.args.get('num2', 0)

    result = int(num1) + int(num2)

    return jsonify({
        "num1": num1,
        "num2": num2,
        "result": result
    })

if __name__ == '__main__':
    app.run()