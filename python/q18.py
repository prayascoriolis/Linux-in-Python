'''18. Write a program to create a simple text-based database system with CRUD (Create, read, update and delete) operations.'''

'''
DATABASE SETUP:

Before running the program, you need to create a MySQL database and a table for storing the user records. 
You can execute the following SQL commands in MySQL:

CREATE DATABASE testdb;
USE testdb;
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    city VARCHAR(100)
);
'''

'''
USER SETUP:

Verify user details:
SELECT User, Host, plugin FROM mysql.user WHERE User = 'username';

Create user:
CREATE USER 'username'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password';

Update user passwd:
ALTER USER 'username'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password';

Flush privileges to apply the changes:
FLUSH PRIVILEGES;
'''

import mysql.connector

# Connect to the MySQL database
def connect_db():
    return mysql.connector.connect(
        host="localhost", # MySQL host
        user="colama", # MySQL username
        password="prayas7@P", # MySQL password
        database="testdb" # the name of database
    )

# Create a new record in the database
def create_record():
    name = input("Enter name: ")
    age = input("Enter age: ")
    city = input("Enter city: ")
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("INSERT INTO users (name, age, city) VALUES (%s, %s, %s)", (name, age, city))
    db.commit()
    print("Record created successfully.")
    db.close()

# Read all records from the database
def read_records():
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users")
    records = cursor.fetchall()
    print("Users in the database:")
    for record in records:
        print(record)
    db.close()

# Update a record in the database
def update_record():
    user_id = input("Enter the user ID to update: ")
    name = input("Enter new name: ")
    age = input("Enter new age: ")
    city = input("Enter new city: ")
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("UPDATE users SET name = %s, age = %s, city = %s WHERE id = %s", (name, age, city, user_id))
    db.commit()
    print("Record updated successfully.")
    db.close()

# Delete a record from the database
def delete_record():
    user_id = input("Enter the user ID to delete: ")
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
    db.commit()
    print("Record deleted successfully.")
    db.close()

# Main function to run the program
if __name__ == "__main__":
    while True:
        print("\nSimple Text-based Database System")
        print("1. Create a new record")
        print("2. Read all records")
        print("3. Update a record")
        print("4. Delete a record")
        print("5. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == "1":
            create_record()
        elif choice == "2":
            read_records()
        elif choice == "3":
            update_record()
        elif choice == "4":
            delete_record()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

