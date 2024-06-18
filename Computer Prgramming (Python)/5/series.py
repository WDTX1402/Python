number = 0


while number < 49:
    number += 1
    if number % 3 == 0:
        continue
    if number == 49:
        print(number)
        break
    print(number, "," ,end = '')
  
     