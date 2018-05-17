import datetime

def meetup_day(year, month, day_of_the_week, which):
    start = datetime.date(year, month, 1)
    possiblities = []
    meet = 0
    ths = {"1st":0, "2nd":1, "3rd":2, "4th":3, "5th":4}

    try:
        for x in range(1, 32):
            try:
                if start.replace(day=x).strftime("%A") == day_of_the_week:
                    possiblities.append(x)
            except(ValueError):
                pass

        if which == "teenth":
            for x in possiblities:
                if x in range(13,20):
                    meet = x
                else:
                    pass

        elif which in ths:
            meet = possiblities[ths.get(which)]

        elif which == "last":
            meet = possiblities.pop()
        return start.replace(day=meet)
    except(ValueError, IndexError):
        raise MeetupDayException("There is no {which} {day_of_the_week} in {month} of {year}.")

class MeetupDayException(Exception):
    pass
