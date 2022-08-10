# Latihan 4 

# POST /car-manufacturer 
# Request body: { "country": "UK" }
# Response: { "manufacturers": [] } 

from dataclasses import replace
from re import X
import requests
from flask import Flask, request

app = Flask(__name__)
def Bauth():
    pass_str = request.headers.get("Authorization")
    pass_bersih = pass_str.replace("Basic ","")
    hasil_decode = base64.b64decode(pass_bersih)
    hasil_decode_bersih = hasil_decode.decode('utf-8')
    username_aja = hasil_decode_bersih.split(":")[0]
    pass_aja = hasil_decode_bersih.split(":")[1]
    if username_aja == "rafi" and pass_aja == "mantap":
        return True


@app.route("/car-manufacture", methods=["POST"])
def car_manufacture ():
    x =requests.get ("https://vpic.nhtsa.dot.gov/api/vehicles/getallmanufacturers?format=json")
    y = x.json()
    z = request.get_json()
    hasil = []
    r = y ["Results"]
    for i in r:
        if i["Country"] == z["Country"]:
            hasil.append(i["Mfr_Name"])
    return hasil
   



