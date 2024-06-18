# def sum(i1, i2):
#     result = 0
#     for i in range(i1, i2 + 1):
#         result += i 
#     return result
# def main():
#     print("Sum from 1 to 10 is", sum(1, 10))
#     print("Sum from 20 to 37 is", sum(20, 37)) 
#     print("Sum from 35 to 49 is", sum(35, 49))

# main()

def printGrade(score):
    if score >= 90.0:
        grade = 'A'
    elif score >= 80.0:
        grade = 'B'
    elif score >= 70.0:
        grade = 'C'
    elif score >= 60.0: 
        grade = 'D'
    else:   
        grade = 'F'

    return grade

def main() :
   score = 90
   print("The grade is ", printGrade(score))

main() 

def main():
 x=5
 print("Before the call, x is", x)
 increment(x)
 print("After the call, x is", x)

def increment(n):
    n+=1
    print("\tn inside the function is", n)

main()