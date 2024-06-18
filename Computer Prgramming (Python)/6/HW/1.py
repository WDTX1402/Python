def converttime(x):
    extract1 = x[0:2]
    extract2 = x[3:5]
    hours = int(extract1)
    mins = int(extract2)
    if 23 >= hours >= 0 and 0 <= mins <= 59:
        if hours == 00:
            return str(hours) + ":" + x[3:5] + "AM"
        elif 1 <= hours < 12:
            return str(hours) + ":" + x[3:5] + "AM"
        elif hours == 12:
            return str(hours) + ":" + x[3:5] + "PM"
        elif 23 >= hours > 12.:
            ans = hours - 12
            return str(ans) + ":" + x[3:5] + "PM"
    else:
        return "Invalid time format"

converted_hours = converttime("13:54")
print(converted_hours)
