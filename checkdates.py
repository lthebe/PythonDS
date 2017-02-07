#Extracts a collection of birthdates from the user and determines if each indiv
#dual is at least 21 years of age

from date import Date

def main():
    bornBefore = Date(6, 1, 1995) #date to be 21 or older
    date = promptAndExtractDate()
    while date is not None:
        if date <= bornBefore:
            print ("Is at least 21 years of age: ", date)
        date = promptAndExtractDate()

def promptAndExtractDate():
    print ("Enter a birth date.")
    month = int(input("month (0 to quit): "))
    if month == 0:
        return None
    else:
        day = int(input("day: "))
        year = int( input ("year: "))
        return Date(month, day, year)

main()
