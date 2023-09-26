# with open("weather-data.csv") as data_files:
#     data = data_files.readlines()
#     print(data)
#
# import csv
#
# with open("weather-data.csv") as data_files:
#     data = csv.reader(data_files)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas as pd

# data = pd.read_csv("weather-data.csv")
# print(type(data))
# # print(data["temp"])
# data_dict = data.to_dict()
# # print(data_dict)
# temp_list = data["temp"].to_list()
# # print(len(temp_list))
# average = sum(temp_list) / len(temp_list)
# print(average)
# print(data["temp"].mean())
# print(data["temp"].max())
# print(data["temp"].min())

# Get data in column
# print(data["condition"])

# Get data in Row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# Create a DataFrame from a scratch
# data_dict = {
#     "students": ["saad", "adil", "asad"],
#     "scores": ["67", "45", "89"]
#
# }
# data = pd.DataFrame(data_dict)
# data.to_csv("new_data.csv")

data = pd.read_csv("2018-Central-Park-Squirrel-Census-Squirrel-Data.csv")
# print(data)
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
# print(grey_squirrels_count)
# print(red_squirrels_count)
# print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pd.DataFrame(data_dict)
df.to_csv("squirrels_count")