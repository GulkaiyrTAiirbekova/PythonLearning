#You can add if statements in the case evaluation as an extra condition-check:
#month = 5
#day = 4
#match day:
#    case 1|2|3|4|5 if month ==3:
#        print("A weekday in March")
#    case 1|2|3|4|5 if month ==5:
#        print("A weekday in May")
#    case _:
#        print("No match")

#month =11
#day = 6
#match day:
#    case 6|7 if month == 4:
#        print("Weekends in April ")
#    case 6|7 if month ==11:
#        print("Weekends in November")
#    case _:
#        print("No match")
month =11
day = 6
match day:
    case 6|7 if month == 4:
        print("Weekends in April ")
    case 6|7 if month ==12:
        print("Weekends in December")
    case _:
        print("No match")


