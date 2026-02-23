date = int(input())
month = int(input())
year = int(input())

valid_date = True

if (year <= 0 or month > 12 or month < 1):
    valid_date = False
else:
    if month in (1,3,5,7,8,10,12):
        max_date = 31
    elif month in (4,6,9,11):
        max_date = 30
    else:
        if (year % 4==0):
            max_date = 29
        else:
            max_date = 28

    if (date > max_date or date < 1):
        valid_date = False

if valid_date:
    if date < max_date:
        date += 1
    else:
        date = 1
        if month == 12:
            month = 1
            year += 1
        else:
            month += 1

    print(f"{date:02d}-{month:02d}-{year}")
else:
    print("Invalid Date")