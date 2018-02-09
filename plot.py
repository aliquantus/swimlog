from models import *
from queries import *
import matplotlib.pyplot as plt


def plotMonthly(datum1, datum2):
    dates, lengths, sessions = monthly(datum1, datum2)
    plt.plot(dates, lengths)
    plt.show()

    plt.savefig("./output/figures/monthly_{}to{}".format(datum1, datum2))


def plot(datum1, datum2, timescale, stroke=0):
    if timescale == "monthly":
        dates, lengths, sessions = monthly(datum1, datum2)
        plt.xlabel("Month")
    elif timescale == "yearly":
        dates, lengths, sessions = yearly(datum1, datum2)
        plt.xlabel("yearly")

    plt.ylabel("Distance")
    plt.title("Distance over time")
    plt.scatter(dates, lengths)
    plt.savefig("output/figures/{}_report_on_{}".format(timescale, date.today()))
    plt.show()
