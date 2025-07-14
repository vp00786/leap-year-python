def is_leap_year(year):
    if year % 4 == 0:
        if year % 400 == 0:
            return True
        elif year % 100 == 0:
            return False
        else:
            return True
    else:
        return False
year=int(input("Enter a year"))
if is_leap_year(year)==True:
    print(f"the year {year} is a leap year")
else:
    print(f"the year {year} is not a leap year")
