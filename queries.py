"""
Summary: Contains queries used by report.py
"""

from models import *
from datetime import date, timedelta
from dateutil import rrule
from dateutil.relativedelta import relativedelta


def future():
    return date.today() + timedelta(days=1)


def farago():
    return date(2010, 01, 01)


def programsBetween(date1, date2):
    return Program.select().where(Program.date.between(date1, date2))


def length(programs):
    return sum([program.length for program in programs])


def count(items):
    return len(items)


def sessionsBetween(date1, date2):
    return len(programsBetween(date1, date2))


def yearly(date1, date2):
    """returns [years (dt obj),lengths,#sessions], allows any date/year inserted"""
    years = range(date1.year, date2.year + 1)
    lengths = [length(programsBetween(date(year=year, month=1, day=1), date(year=year, month=12, day=31))) for year in years]
    sessions = [count(programsBetween(date(year=year, month=1, day=1), date(year=year, month=12, day=31))) for year in years]
    return [date(year=year, month=1, day=1) for year in years], lengths, sessions


def lastDayofMonth(datum):
    return date(year=datum.year, month=datum.month, day=1) + relativedelta(months=1, days=-1)


def monthly(datum1, datum2):
    """returns [years (dt obj),lengths,#sessions], allows any date/year inserted"""
    #months = [date(year=datum.year)]
    datum1 = date(year=datum1.year, month=datum1.month, day=1)
    datum2 = lastDayofMonth(datum2)
    datum = datum1
    dates = []
    while datum < datum2:
        dates.append(datum)
        datum += relativedelta(months=1)
    lenths = []
    sessions = []
    lengths = [length(programsBetween(datum, lastDayofMonth(datum))) for datum in dates]
    sessions = [count(programsBetween(datum, lastDayofMonth(datum))) for datum in dates]
    return dates, lengths, sessions
