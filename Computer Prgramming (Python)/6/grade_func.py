def printGrade(score):
    if score > 100:
        grade ='Invalid'
    if score >= 80.0:
        grade = 'A'
    elif score >= 70.0:
        grade = 'B'
    elif score >= 60.0:
        grade = 'C'
    elif score >= 50.0: 
        grade = 'D'
    elif 0 <= score < 50:
        grade = 'F'
    else:
        grade = 'Invalid'
    return grade

def main(score) :
   print("The grade is", printGrade(score))

main(90) 