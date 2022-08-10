# from itertools import count
# import requests
# r= requests.get('https://vpic.nhtsa.dot.gov/api/vehicles/getallmanufacturers?format=json')
# x = r.json()
#memanggil lewat "count" sebagai panjang array
# arr = x["Count"]
# for i in range(arr):
#     if x["Results"][i]["Country"] == "UNITED KINGDOM (UK)":
#         print(x["Results"][i]["Country"], x["Results"][i]["Mfr_Name"])


#apabila kita mau memanggil lewat array "result" yg berupa nested
# arr = x["Results"]
# for i in (arr):
#     if i["Country"] == "UNITED KINGDOM (UK)":
#         print(i["Country"], i["Mfr_Name"])


#memanggil truk dan countrynya beserta mfr
#cara 1
# arr = x["Results"]
# for i in (arr):
#     if i ["VehicleTypes"]!= []:
#         for j in range(len(i["VehicleTypes"])):
#             if i["VehicleTypes"][j]["Name"] == "Truck ":
#                 print(i["Country"], i["Mfr_Name"])

#cara 2
# arr = x["Count"]
# for i in range(arr):
#     if x["Results"][i]["VehicleTypes"] != []:
#         for j in range(len(x["Results"][i]["VehicleTypes"])):
#             if x["Results"][i]["VehicleTypes"][j]["Name"] == "Truck ":
#                 print(x["Results"][i]["Country"], x["Results"][i]["Mfr_Name"])

#cara 3 (dictionary)
# if r.status_code == 200 :  #untuk memastikan respon ok , bisa pakai if/else atau try/except (terjadi error apabila ada kesalahan pd parameter)
# try :    
#     for i in x["Results"]:
#         if i ["VehicleTypes"]!= []:
#             for j in (i["VehicleTypes"]):
#                 if j["Name"] == "Truck ":
#                     print({
#                         "Country":i["Country"], 
#                         "Mfr_Name":i["Mfr_Name"],
#                     })
# except :
# # else :
#     print(f"error : {r.status_code} ")


