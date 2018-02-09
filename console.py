"""Contains everything that is printed to the console"""

from models import *
from queries import *
import calendar
from dateutil.relativedelta import relativedelta
import datetime
import numpy as np


def instructions():
    print(
        """Welcome to the swimlog. You have the following options: \n
        (1): insert new program
        (2): display last five programs
        (3): generate plots
        (4): generate monthly report
        (5): generate weekly report
        (9): remove program
        (0): exit\n""")


def percentageChange(a, b):
    if a == 0:
        return "N/A"
    c = np.true_divide(b, a) - 1
    if c > 0:
        return "+{}%".format(int(round(100 * c)))
    else:
        return "{}%".format(int(round(100 * c)))


def printMonthly(datum=date.today(), months=5):
    """returns [months,lengths,#sessions]"""
    dates, length, sessions = monthly(datum - relativedelta(months=months), datum2=datum)
    for i in range(len(dates) - 1):
        if sessions[i] > 0:
            average = np.true_divide(length[i], sessions[i])
        else:
            average = "N/A"
        print("""
            Month: {} {}
            Number of sessions: {}
            Total metres: {}
            Average per session: {}
            Difference to previous month: {}"""
              .format(
                  calendar.month_name[dates[i].month],
                  dates[i].year,
                  length[i],
                  sessions[i],
                  average,
                  percentageChange(length[i - 1], length[i])
              ))


def display(number=5):
    for program in lastPrograms(number):
        print("""
            id: {}
            date: {}
            length: {}""".format(program.id, program.date, program.length)
              )
