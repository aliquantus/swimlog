"""
Summary: Contains classes for the database.
Classes: BaseModel with subclasses Program
"""

from peewee import *
import json

with open("config.json", "r") as f:
    config = json.load(f)
    print config
    db = SqliteDatabase(config["dbname"])


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    id = PrimaryKeyField()
    username = TextField(unique=True)


class Program(BaseModel):
    id = PrimaryKeyField()
    length = IntegerField(default=0)
    date = DateField(default="2011-05-11")


class Set(BaseModel):
    id = PrimaryKeyField()


class Leg(BaseModel):
    id = PrimaryKeyField()


if __name__ == "__main__":
    try:
        db.create_tables([Program, Set, Leg])
    except:
        print("There already exists a database with this name!")
