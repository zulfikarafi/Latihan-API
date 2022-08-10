#SOAL : 
# GET /hurdle-race/k/1 
# Req body: { "height": [1,2,3,3,2] } 
# Resp body: { "min_doses": 2 } 

import requests
from flask import Flask, request
app = Flask(__name__)
@app.route ("/hurdle-race/k/<k1>", methods = ["GET"])
def hurdleRace(k1):
    height = request.json["height"] #mengambil data json berdasarkan key (dlm kasus ini key adalah height )
    # height_ = request.get_json()  # tidak dipakai karena mengambil semua data 
    k = int(k1)                     # k1 adalah string karena mengambil dari path maka dari itu hatrus dibuat menjadi integer
    doses = 0
    if max(height) > k :
        doses = max(height) - k
    elif k > max(height):
        doses = 0
    return { "min_doses" : doses
            }
# print(hurdleRace(2)) 
