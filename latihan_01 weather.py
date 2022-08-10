from cgitb import text
import requests
r = requests.get('https://api.openweathermap.org/data/2.5/weather?q=cimahi&appid=0af7650b00321f8081a8a9ad3a838f51') #>> lokasi database
x=r.json() #merequest dalam bentuk json
#misal mau pangggil kota saja
# print(x["name"])

#mencoba memanggil beberapa atribut
# print("Kota",x["name"], "memiliki suhu", x["main"]["temp"], "dan tekanan sebesar", x["main"]["pressure"])


#memanggil value yang terdapat kurung siku harus pake index, satu pasang kurung kurawal menyatakan satu index
# print(x["weather"][0]["id"])
# print(x["weather"][0]["main"])
# print(x["weather"][0]["description"])
# print(x["weather"][0]["icon"])

#apabila ingin print semua value dalam satu key
print(x["wind"])

