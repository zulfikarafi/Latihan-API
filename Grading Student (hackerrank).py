from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def gradingStudents():
    grades = request.json["grades"]
    n = len(grades) 

    for i in range(n):
        grade = grades[i]
        if grades[i] >= 38:
            modulus = grades[i] % 5  
            if modulus == 3:
                grade = grades[i] + 2
                grades[i] = grade
            elif modulus == 4:
                grade = grades[i] + 1
                grades[i] = grade
            else:
                grade = grades[i]
                grades[i] = grade         
        else:
            grade = grades[i]
            grades[i] = grade
    return grades 

#cara ke dua
# for i in range(len(grades)) :
#         if grades[i] % 5 == 3 and grades[i] > 35:
#             grades[i] = grades[i] + 2
#         elif grades[i] % 5 == 4 and grades[i] > 35:
#             grades[i] = grades[i] + 1
#     return grades 