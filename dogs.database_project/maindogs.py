import os
import sqlite3
from sqlite3 import Error

def main():
    while True:
        add_dog_to_table()
        list_dog_table()
        
        answer = input("\nDo you want to add another dog? j\n: ")
        if (answer != "j"):
            break

def add_dog_to_table():
    os.system('cls' if os.name == 'nt' else 'clear')
    dogname = input("Enter Name : ")
    dogbreed = input("Enter Breed : ")

    sqliteConnection = sqlite3.connect("dogs.db")
    cursor = sqliteConnection.cursor()
    sqlite_insert_query = f"""INSERT INTO dogs
                            (Name, Breed)
                            VALUES
                            ('{dogname}', '{dogbreed}') """
    
    cursor.execute(sqlite_insert_query)
    sqliteConnection.commit()
    print("\nSuccessfully added new dog\n")
    cursor.close()
    sqliteConnection.close()

def list_dog_table():
    sqliteConnection = sqlite3.connect("dogs.db")
    cursor = sqliteConnection.cursor()
    
    sqlite_select_query = """SELECT * from dogs ORDER by name"""
    cursor.execute(sqlite_select_query)
    records = cursor.fetchall()
        
    for row in records:
        print(f"\tID: {row[0]}, \tNAME: {row[1]}, \tBREED: {row[2]}")
        
    cursor.close()
    sqliteConnection.close()
    print("The SQlite connection is closed")

main()