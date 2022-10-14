import sqlite3
from sqlite3 import Error


def sql_connection():
    try:
        con = sqlite3.connect('SQL_Students.db')
        return con
        print("Соединение работает")
    except Error:
        print(Error)


# "FOREIGN KEY (FacultyID) REFERENCES Faculties(FacultyID),"
#
# "FOREIGN KEY (SpecialtyID) REFERENCES Specialities(SpecialtyID),"
#
# "FOREIGN KEY (SetID) REFERENCES Sets(SetID),"
# "FOREIGN KEY (TeachFormID) REFERENCES TeachForm(TeachFormID),"
#
# "FOREIGN KEY (GroupID) REFERENCES Groups(GroupID),"

def sql_faculties(con):
    cursorObj = con.cursor()
    cursorObj.execute(
        "CREATE TABLE Faculties("
        "FacultyID integer PRIMARY KEY,"
        "FacultyName text,"
        "Descript text)")

    cursorObj.execute(
        "INSERT INTO Faculties "
        "VALUES(1, 'ФКТиПМ', 'Факультет компьютерных технологий и прикладной математики')"
    )
    cursorObj.execute(
        "INSERT INTO Faculties "
        "VALUES(2, 'РГФ', 'Гуманитарии')"
    )

    cursorObj.execute(
        "INSERT INTO Faculties "
        "VALUES(3, 'Журфак', 'Бесполезнарии')"
    )
    con.commit()


def sql_specialities(con):
    cursorObj = con.cursor()
    cursorObj.execute(
        "CREATE TABLE Specialties("
        "SpecialtyID integer PRIMARY KEY,"
        "FacultyID integer,"

        "SpecialtyName text,"
        "SpecialtyCode integer,"
        "Descript text)")
    con.commit()


def sql_sets(con):
    cursorObj = con.cursor()
    cursorObj.execute(
        "CREATE TABLE Sets(SetID integer PRIMARY KEY,"
        "SpecialtyID integer,"

        "SetName text,"
        "SetYear text)")
    con.commit()


def sql_teach_form(con):
    cursorObj = con.cursor()
    cursorObj.execute(
        "CREATE TABLE TeachForm("
        "TeachFormID integer PRIMARY KEY,"
        "Descript text)")
    con.commit()


def sql_groups(con):
    cursorObj = con.cursor()
    cursorObj.execute(
        "CREATE TABLE Groups("
        "GroupID integer PRIMARY KEY,"

        "TeachFormID integer,"

        "GroupName text)")
    con.commit()


def sql_students(con):
    cursorObj = con.cursor()
    cursorObj.execute(
        "CREATE TABLE Students("
        "StudentID integer PRIMARY KEY,"
        "GroupID integer,"

        "Surname text,"
        "Firstname text,"
        "Lastname text,"
        "Phone text)")
    con.commit()


con = sql_connection()

sql_faculties(con)
sql_specialities(con)
sql_sets(con)
sql_teach_form(con)
sql_groups(con)
sql_students(con)
