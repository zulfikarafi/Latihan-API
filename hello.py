#flask tutorial
from flask import Flask

app = Flask(__name__) 

@app.route("/") #untuk path dan routing
def hello_world():
    return "<p>Hello, World!</p>"