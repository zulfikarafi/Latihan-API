from flask import Flask, request

app = Flask(__name__)

@app.route('/hello-json', methods=['GET'])
def hello_json():
     x = request.args.get("message")
     return {
        "message" : "Hello " + x
     }