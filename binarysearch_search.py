import csv
import string

# Open the CSV File and read it in.
f = open('countries.csv')
data = f.read()

# Split the data into an array of countries.
countries = data.split('\n')

length = len(countries)
# print(countries[1])
# print(countries)

# Start your search algorithm here.
country = input('enter a country: ')
upperbound = length-1
lowerbound = 0
found = False
while lowerbound <= upperbound and found == False:
    midpoint= round((lowerbound+upperbound)/2)
    print(midpoint)
    if country == countries[midpoint]:
        found = True
        print("congrats")
    else:
        if country < (countries[midpoint]):
            upperbound = midpoint-1
        else:
            lowerbound = midpoint+1

if found == False:
    print("not ont the list")
