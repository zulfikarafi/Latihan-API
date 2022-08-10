# Latihan 3
#buat basic oath
# GET /weather 
# request header: city=bandung 
# Response: {"weather":"Cloudy","coordinate":{"lat":1,"lon":2},"temperature":1} 

## Untuk GET data
# import requests
# from flask import Flask, request
# app = Flask(__name__)

# @app.route('/weather')
# def latihan3():
#     a = request.headers.get('city')
#     r = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={a}&appid=0af7650b00321f8081a8a9ad3a838f51')
#     b = r.json()
#     return {
#         'Weather' : b['weather'][0]['main'],
#         'Coord' : b['coord'],
#         'Temp' : b['main']['temp']
#     }


## AUTORIZATION 
import requests, base64
from flask import Flask, request


app = Flask(__name__)

def BasicAuth() :
    pass_str = request.headers.get('Authorization')     #untuk mengambil authorization di postman
    pass_bersih = pass_str.replace('Basic ',"")         #untuk memotong "basic" (pada value authorization)
    hasil_decode = base64.b64decode(pass_bersih)        #untuk merubah password (decode) "dGVzbWlrOnRlczEyMw==" menjadi "tes123" (base64.b64code merupakan package fungsi dari python)
    hasil_decode_bersih = hasil_decode.decode('utf-8')  #untuk membuang "b" pada hasil_decode (.decode('utf-8))
    username_aja = hasil_decode_bersih.split(":")[0]    #untuk slicing apabila ingin menampilkan username saja (username:)
    pass_aja = hasil_decode_bersih.split(":")[1]        #untuk slicing apabila ingin menampilkan pass saja (:password)
    if username_aja == 'tes' and pass_aja == 'tes123' : #kondisional apabila user memasukan pass dan username sesuai 
        return True

@app.route('/weather')
def latihan3():
    if BasicAuth() :
        a = request.headers.get('city')
        r = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={a}&appid=0af7650b00321f8081a8a9ad3a838f51')
        b = r.json()
        
        return {
            'Weather' : b['weather'][0]['main'],
            'Coord' : b['coord'],
            'Temp' : b['main']['temp']
        } ,200
    else :
        return {
            '401' : 'Salah cuk'
        } , 401