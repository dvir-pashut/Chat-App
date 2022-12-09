import mysql.connector

#Connection to db using the connector

def db_connect():
    pass
    

cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password"
)
cursor = cnx.cursor()



#table name wiil  be : general,room1,room2,room3,room4....)

#The cursor executes all my sql commands

# Check if the "users" table exists
# DATABSE INITIALIZATION - Runs only one time

msg="[2022-12-08 15:57:53] Benny: ITWORKS"




def DB_INITIALIZATION():
    cursor.execute("CREATE DATABASE chatapp;")
    
    
cursor.execute("USE chatapp;")
cursor.execute("SHOW TABLES LIKE 'room1'")
if cursor.fetchone():
    print("Table exists Insetrting message:")
    cursor.execute(f"INSERT INTO room1 (message) VALUES ('{msg}');")
    cursor.execute("SELECT * from room1;")
    results = cursor.fetchall()
    string = ""
    for result in results:
        id = result[0]
        message = result[1]
        #print(f"ID: {id}, Message: {message}")
        string += f"ID: {id}, Message: {message}\n"
    print(string)

else:
    print("Table does not exist")
    cursor.execute("CREATE TABLE room1 (id INT AUTO_INCREMENT PRIMARY KEY,message TEXT);")
    

    



# cursor.execute("CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))")


cnx.commit()

cnx.close()
