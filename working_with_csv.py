import csv
import pandas as pd

with open('data.csv', 'r') as file: #replace your file name
    csv_reader = csv.reader(file)
    header = next(csv_reader)  # Read the header
    for row in csv_reader:
        # Process each row
        print(row)


#another method by built inn python libraries



df = pd.read_csv('data.csv')
#print(df.head())  # Display first few rows

#write a csv file from a data


data = [
    ['id', 'name', 'age'],
    [1, 'Alice', 30],
    [2, 'Bob', 25],
    [3, 'Cathy', 27] 
]

with open('output.csv', 'w', newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows(data)

