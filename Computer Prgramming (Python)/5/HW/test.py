
# while True:
    
#     inpus = input("Enter a number: ")

#     if inpus == 'exit':
#         break

#     try:
#      e = int(inpus)
           
#     except ValueError:
#         continue
    
#     if len(inpus) >= 1:
#      n = 0 
#      for r in range(0,e):
#         e -= 1 
#         for x in range (0,e+1):
#             for a in range (0, x):
#                 print ('*', end = '')
#             print()
#         for b in range (0,e+1):
#             x = x - 1
#             for d in range (0, x):
#                  print ('*', end = '')
#             print()
    
            
# num = int(input ("Enter the number greater than or equal to 1: "))
# if num <1:
#   print ("Please Enter the number greater than or equal to 1")
# else:
#  if num == 1:
#   print ("\n*")
#  else:
#   print("*")
#   for u in range (num):
#     for i in range (1, num-u) : 
#         for _ in range(i+1) :
#           print ("*",end="")
#         print ()
#     for j in range(num-(u+1)) :
#      for _ in range((num-u) - (j+1)): 
#         print("*", end="")
#      print()
#   print("*")

n = int(input("Enter: "))

guess = n/2
j = 1
while j < 8:
         temp = n/guess
         guess = (guess  + temp)/2
         j += 1
         if  5 <= j <= 7: 
          print("aprrox square root is", format(guess, '3f'))