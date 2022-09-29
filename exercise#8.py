#Exercise 8
#problem 1
import mysql.connector

connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='root',
         autocommit=True
         )

inputICAO = input("input ICAO: ")

sql = "select name, municipality from airport where ident = '"+ inputICAO + "'"

cursor = connection.cursor()
cursor.execute(sql)
result = cursor.fetchall()

if cursor.rowcount > 0:
    for row in result:
        print(f"The airport name is {row[0]} and the location is {row[1]}")

#Problem 2
import mysql.connector

connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='root',
         autocommit=True
         )
area_code = input("area code: ")

sql = "select municipality, type from airport where iso_country = '"+ area_code +"' order by type"

cursor = connection.cursor()
cursor.execute(sql)
result = cursor.fetchall()

if cursor.rowcount > 0:
    for row in result:
        print(f"The airport location is {row[0]} and the airport type is {row[1]}")

#problem 3