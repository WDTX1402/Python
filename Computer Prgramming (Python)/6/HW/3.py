def shoutnumber(n):
    sdigit = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
            "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen","I don't know"]
    ddigit = ["s", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    if 0 <= n <= 999:
        if n == 0:
            return "zero"
        elif n < 20:
            return sdigit[n]
        elif n < 100:
            if n % 10 == 0:
                return ddigit[n // 10]
            else:
                return ddigit[n // 10] + "-" + sdigit[n % 10]
        elif n >= 100:
            if n % 100 == 0:
                return sdigit[n // 100] + " hundred"
            else:
                s = n % 100
                if s < 20:
                    return sdigit[n // 100] + " hundred and "+ sdigit[s]
                elif s < 100:
                    if s % 10 == 0:
                     return sdigit[n // 100] + " hundred and "+ ddigit[s // 10]
                    else:
                     return sdigit[n // 100] + " hundred and "+ ddigit[s // 10] + "-" + sdigit[s % 10]
    else:
        return sdigit[20]
    
amogus = shoutnumber(999)
print(amogus)



