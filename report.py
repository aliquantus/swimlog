from models import *
from queries import *
import datetime
import matplotlib.pyplot as plt


x, y, _ = monthly(farago(), future())
plt.scatter(x, y)
plt.plot()
plt.show()





def monthly(date1, date2):
    """returns [months,lengths,#sessions]"""


def weekly(date1, date2):
    """returns [weeks,lengths,#sessions]"""
