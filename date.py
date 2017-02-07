#implements a proleptic Gregorian calendar date as Julain day number
import datetime
class Date:
    def __init__(self, month, day, year):
        self._julianDay = 0
        assert self._isValidGregorian(month, day, year), \
            "Invalid Gregorian date."
        tmp = 0
        if month < 3:
            tmp = -1
        self._julianDay = day - 32075 + (1461 * (year + 4800 + tmp) // 4) + \
            (367 * (month - 2 - tmp * 12) // 12) - \
            (3 * ((year + 4900 + tmp)//100)//4)

    def month(self):
        return (self._toGregorian())[0] # returning M from (M, d, y)
    def day(self):
        return (self._toGregorian())[1] # returning d
    def year(self):
        return (self._toGregorian())[2] #returning y

    def dayOfWeek(self):
        month, day, year = self._toGregorian()
        if month < 3:
            month = month + 12
            year = year - 1
        return ((13*month + 3)//5 + day + \
                year + year // 4 - year // 100 + year // 400) %7

    def __str__(self):
        month, day, year = self._toGregorian()
        return "%02d/%02d/%04d" %(month, day, year)

    def __eq__(self, otherDate):
        return self._julianDay == otherDate._julianDay
    def __lt__(self, otherDate):
        return self._julianDay < otherDate._julianDay

    def __le__(self, otherDate):
        return self._julianDay <= otherDate._julianDay

    def _isValidGregorian(self,month, day, year):
        try:
            datetime.datetime(year=year, month=month, day=day)
            return True
        except ValueError:
            return False
    def _toGregorian(self):
        A = self._julianDay + 68569
        B = 4 * A // 146097
        A = A - (146097 * B + 3) // 4
        year = 4000 * (A+1)//1461001
        A = A - (1461 * year // 4) + 31
        month = 80 * A // 2447
        day = A - (2447 * month // 80)
        A = month // 11
        month = month + 2 - (12*A)
        year = 100 * (B - 49) + year + A
        return month, day, year
