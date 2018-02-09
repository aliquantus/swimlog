from models import *
from queries import *
import datetime
from dateutil.relativedelta import relativedelta
import matplotlib.pyplot as plt
import calendar
import numpy as np


def printWeekly(datum, nWeeks=5):
    """returns [weeks,lengths,#sessions]"""
