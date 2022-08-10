# GET /cat-and-mouse/x/1?y=2
# req header: z=3
# resp body: { "message": "Cat B" } 
import requests
from flask import Flask, request

app = Flask(__name__)
@app.route('/cat-and-mouse/x/<x1>', methods= ['GET']) #/x/<x1> path parameter
def catAndMouse(x1):

    z = request.headers.get("z")                    #request header
    x = x1                                          #path parameter
    y =request.args.get("y")                        #query parameter
    if abs(int(x)-int(z)) < abs(int(y)-int(z)):
        return {"message":"Cat A"}
    elif abs(int(x)-int(z)) > abs(int(y)-int(z)):
        return {"message":"Cat B"}
    elif abs(int(x)-int(z)) == abs(int(y)-int(z)):
        return {"message":"Cat C"}

