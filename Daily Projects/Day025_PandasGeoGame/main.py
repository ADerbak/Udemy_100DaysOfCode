# weather =[]
# with open("weather_data.csv") as file:
#     data = file.readlines()
#     for i in data:
#         row = i.strip().split(',')
#         weather.append(row)
#
# print(weather)


# import csv
#
# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)


import pandas

df = pandas.read_csv("weather_data.csv")
# print(df)
# print(df['temp'])

# Challenge - get the average temp
temps = df['temp'].to_list()
print(sum(temps)/len(temps))
print(df.temp.mean())

# Challenge - get the max temp
print(df.temp.max())

# Challenge - get the row for the max temp
print(df[df.temp == df.temp.max()])

# Challenge - get Monday's temperature in Fahrenheit
monday = df[df.day == 'Monday']
print(f"Monday's Temp in F: {int(monday.temp) * 1.8 + 32}")