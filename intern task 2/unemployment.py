import csv

# Define the headers and data rows for the file
headers = ["year", "unemployment_rate"]
rows = [
    [2010, 9.7],
    [2011, 9.1],
    [2012, 8.2],
    [2013, 7.9],
    [2014, 6.2],
    [2015, 5.3],
    [2016, 4.9],
    [2017, 4.4],
    [2018, 3.9],
    [2019, 3.5],
    [2020, 6.0],
    [2021, 5.5],
    [2022, 4.8],
]

# Write the data to the file
with open("unemployment.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(rows)
