# importing the required module
import sqlite3

#use the database if it pre-exists or create it otherwise
try:
    connection = sqlite3.connect("myemp.db")
    print("Connected with the database successfully .....")
except:
    print("Database creation ERROR !!!")
