
def date_converter(s):
    year = s[6] + s[7]

    if int(s[6]) > 2:
        year = "19" + s[6] + s[7]
    else:
        year = "20" + str(year)

    month = s[0] + s[1]
    day = s[3] + s[4]
    new_date = str(year+"-"+month+"-"+day)

    return new_date


date = input("Write an American date: (MM/DD/YY): ")

print("Swedish date:", date_converter(date))
