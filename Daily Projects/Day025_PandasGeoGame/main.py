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
import pandas as pd

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


# Squirrel Challenge! Get count of all fur colors

df_s = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
df_s_fur = df_s[['Primary Fur Color', 'Location']]
gray_squirrels = len(df_s[df_s['Primary Fur Color'] == "Gray"])
red_squirrels = len(df_s[df_s['Primary Fur Color'] == "Cinnamon"])
black_squirrels = len(df_s[df_s['Primary Fur Color'] == "Black"])

data_dict = {
    # 'gray' : gray_squirrels,
    # 'red' : red_squirrels,
    # 'black' : black_squirrels
    'fur color' : ['gray', 'red', 'black'],
    'count' : [gray_squirrels, red_squirrels, black_squirrels]
}

df_s_colors = pd.DataFrame(data_dict)

# sq_scounts = df_s_fur.groupby('Primary Fur Color').count()
# sq_scounts.columns = ['Count']
# sq_scounts.sort_values('Count', ascending=False).to_csv('squirrel_counts.csv')
df_s_colors.to_csv('squirrel_counts.csv')