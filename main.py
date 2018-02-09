from models import *
from queries import *
from plot import plot
from console import *


def insertProgram(datum, length):
    Program.create(date=datum, length=length)


def removeProgram(id):
    Program.get(Program.id == id).delete_instance()


def interactive():
    instructions()
    while True:
        choice = str(raw_input("make a choice: "))
        if choice == "1":
            datum = str(raw_input("date (YYYY-MM-DD): "))
            length = input("length: ")
            insertProgram(datum, length)
            print "program inserted \n"
        elif choice == "2":
            display(number=5)
        elif choice == "3":
            choice = str(raw_input("choose monthly(m) or yearly(y): "))
            if choice in ["m", "monthly"]:
                plot(beginning(), future(), "monthly")
            elif choice in ["y", "yearly"]:
                plot(beginning(), future(), "yearly")
            else:
                print("not a valid choice \n")
        elif choice == "4":
            printMonthly()
        elif choice == "5":
            printMonthly()
        elif choice == "9":
            id = input("choose an id to remove: ")
            try:
                removeProgram(id)
                print("removed program with id {}... \n".format(id))
            except:
                print("there is no program with this id\n".format(id))
        elif choice == "0":
            break


if __name__ == "__main__":
    interactive()
