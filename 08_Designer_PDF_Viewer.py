# Soal
# GET /pdf-viewer?word=torn 
# Req body: { "height": [1,2,3,3,2,...] } 
# Resp body: { "area": "9 mm2" }
import requests
from flask import Flask, request
app = Flask(__name__)
@app.route ("/pdf-viewer", methods =["GET"])
def designerPdfViewer():
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    height = request.json["height"]
    word =request.args.get("word")
    Kamus = {}
    item = []
    output = 0
    for i in range(len(alphabet)):
        for j in range(len(height)):
            if i == j :
                Kamus[alphabet[i]] = height[j]
    for k in word:
            item.append(Kamus.get(k))
            output = max(item)*1*len(word)
    return { "area" : output}
# print(designerPdfViewer([1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5], "abc"))
                
            