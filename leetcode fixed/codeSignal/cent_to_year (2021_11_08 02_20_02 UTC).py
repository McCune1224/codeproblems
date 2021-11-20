def centuryFromYear(year):
    if year <=100:
        return 1
    str_year = str(year)
    cent = ''
    if len(str_year) <=3:
        cent += str_year[0]
        if str_year[1:] != "00":
            cent = int(cent) + 1 
    else:
        cent += str_year[0:2]
        if str_year[2:] != "00":
            cent = int(cent) + 1
    print(cent)
test = input("Year: ")
centuryFromYear(int(test))
