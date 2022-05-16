"""  Give your birthday and the current date, calculate your age in days. """


def is_leap_year(year: int):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False


def daysInMonth(year: int, month: int):
    # if month in [1, 2, 5, 7, 8, 10, 12]
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    else:
        if month == 2:
            if is_leap_year(year):
                return 29
            else:
                return 28
        else:
            return 30


def nextDay(year: int, month: int, day: int):
    """ Warning: this version incorrectly assumes all month have 30 days! """
    if day < daysInMonth(year, month):
        return year, month, day + 1
    else:
        if month < 12:
            return year, month + 1, 1
        else:
            return year + 1, 1, 1


def dateIsBefore(
    year1: int, month1: int, day1: int, year2: int, month2: int, day2: int
):
    """ Return true if year1-month1-day1 is before year2-month2-day2. otherwise
     return false."""
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False


def daysBetweenDates(
    year1: int, month1: int, day1: int, year2: int, month2: int, day2: int
):
    days = 0
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1
    return days


def my_test():
    # tests with 30-day months!
    assert daysBetweenDates(2013, 1, 1, 2013, 1, 1) == 0
    assert daysBetweenDates(2013, 1, 1, 2013, 1, 2) == 1
    assert nextDay(2013, 1, 1) == (2013, 1, 2)
    assert daysBetweenDates(2012, 1, 1, 2013, 1, 1) == 366
    assert daysBetweenDates(2013, 1, 1, 2014, 1, 1) == 365
    assert daysBetweenDates(2013, 1, 24, 2013, 6, 29) == 156
    print('test finished')


def test():
    test_cases = [
        ((2012, 1, 1, 2012, 2, 28), 58),
        ((2013, 1, 1, 2012, 3, 1), 60),
        ((2011, 6, 30, 2012, 6, 30), 366),
        ((2011, 1, 1, 2012, 8, 8), 585),
        ((1900, 1, 1, 1999, 12, 21), 36523),
        ((2022, 5, 16, 2022, 5, 17), 1)
    ]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print("Test with data:", args, "failed")
        else:
            print("Test case passed!")


my_test()
test()