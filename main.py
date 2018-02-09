from models import *
from queries import *
from plot import plot


def insertProgram(datum, length):
    Program.create(date=datum, length=length)


def removeProgram(id):
    Program.get(Program.id == id).delete_instance()


def get_config():
    with open("config.json", "r") as f:
        config = json.load(f)
    return config


def instructions():
    print(
        """Welcome to the swimlog. Your current database is {}. You have the following options: \n
        (1): insert new program
        (2): display last five programs
        (3): generate report
        (4): remove program
        (9): change active database
        (0): exit\n""".format(get_config()["dbname"])
    )


def display(number=5):
    for program in lastPrograms(number):
        print(
            """id: {}
             date: {}
             length: {} \n
            """.format(program.id, program.date, program.length)
        )


def changedb(name):
    with open("config.json", "r") as f:
        config = json.load(f)
    config["dbname"] = "databases/" + name + ".db"
    with open("config.json", "w") as f:
        json.dump(config, f)
    get_or_create_db()


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
            id = input("choose an id to remove: ")
            try:
                removeProgram(id)
                print("removed program with id {}... \n".format(id))
            except:
                print("there is no program with this id\n".format(id))
        elif choice == "9":
            name = str(raw_input("choose a new active database"))
            changedb(name)
            print("Now using database {}".format(get_config()["dbname"]))
        elif choice == "0":
            break


if __name__ == "__main__":
    interactive()
