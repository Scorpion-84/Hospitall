import sqlite3

connection = sqlite3.connect("Hospitall.db")

cursor = connection.cursor()

cursor.execute("""
        
        CREATE TABLE IF NOT EXISTS SICK(
            code INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            family TEXT NOT NULL,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            type_of_disease TEXT NOT NULL,
            doctor_name TEXT NOT NULL,
            role TEXT NOT NULL
        )
                       
""")

cursor.execute("""
               
        CREATE TABLE IF NOT EXISTS DOCTOR(
            code INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            family TEXT NOT NULL,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            time_visit DATE NOT NULL,
            role TEXT NOT NULL
        )               
               
""")



cursor.execute("""
               
        CREATE TABLE IF NOT EXISTS EMPLOYEE(
            code INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            family TEXT NOT NULL,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            role TEXT NOT NULL
        )               
               
""")



cursor.execute("""
               
        CREATE TABLE IF NOT EXISTS VISIT(
            code INTEGER PRIMARY KEY,
            date DATE NOT NULL,
            doctor_name TEXT NOT NULL,
            sick_name TEXT NOT NULL,
            status TEXT NOT NULL
        )               
               
""")



cursor.execute("""
               
        CREATE TABLE IF NOT EXISTS PAYMENT(
            code INTEGER PRIMARY KEY,
            code_of_visit TEXT NOT NULL,
            date DATE NOT NULL,
            sum_price TEXT NOT NULL,
            status TEXT NOT NULL
        )               
               
""")

connection.commit()


cursor.close()
connection.close()

