from flask import Flask, request

app = Flask(__name__)
@app.route("/number", methods = ["PUT"])
def numbers():
    i = request.json ["number"]
    x = request.get_json()
    even_numbers = []
    odd_numbers = []
    for i in range(len(x)):
        if i%2 == 0 :
            even_numbers.append(x[i])
        else:
            odd_numbers.append(x[i])
    return {"Genap" : even_numbers, 
            "Ganjil" : odd_numbers
            }