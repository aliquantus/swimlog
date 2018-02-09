from models import *
from queries import *


def insertProgram(datum, length):
    Program.create(date=datum, length=length)


def removeProgram(id):
    Program.get(Program.id == id).delete_instance()


def instructions():
    print(
        """Welcome to the swimlog. You have the following options \n
        (1): insert new program
        (2): display last five programs
        (3): remove program
        (0): exit\n"""
    )


def display(number=5):
    for program in lastPrograms(number):
        print(
            """id: {}
             date: {}
             length: {} \n
            """.format(program.id, program.date, program.length)
        )


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
