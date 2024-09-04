import csv

with open("weather.csv", "r") as file:
    data = list(csv.reader(file))

city = input("Enter a city: ")
city = city.title()

for row in data:
    if row[0] == city:
        print("The temperature is " + str(row[1]) + " degrees.")