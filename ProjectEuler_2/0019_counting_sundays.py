# You are given the following information, but you may prefer to do some research for yourself.
#
# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth
# century (1 Jan 1901 to 31 Dec 2000)?


class Daysinmonth:

    def __init__(self):

        self.daysinmonth = {
            1: 31,
            2: 28,
            3: 31,
            4: 30,
            5: 31,
            6: 30,
            7: 31,
            8: 31,
            9: 30,
            10: 31,
            11: 30,
            12: 31
        }

    def truemonthdays(self, month, year):
        days = self.daysinmonth[month]
        if month == 2:
            if year % 4 == 0 and (year % 100 != 0 or (year % 100 == 0 and year % 400 == 0)):
                days += 1
        return days


def main():

    daysinmonth = Daysinmonth()
    curryear = 1900
    currmo = 1
    dayofweek = 1
    sundays = 0
    while curryear <= 2000:
        daysinmo = daysinmonth.truemonthdays(currmo, curryear)
        dayofweek += daysinmo
        dayofweek %= 7
        if curryear >= 1901 and dayofweek == 0:
            sundays += 1
        currmo += 1
        if currmo > 12:
            currmo = 1
            curryear += 1

    print(sundays)


if __name__ == '__main__':
    main()
