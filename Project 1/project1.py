# I am using the hard-way to calculate mean, median, and mode!
import csv

# read the CSV file
df = "/Users/cc/Desktop/Python/Shiyi.github.io/Project 1/NYPD_Arrest_Data__Year_to_Date_.csv"

# read the column names
column_name = 'ARREST_PRECINCT'

# read the file manually
value = []
with open(df, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        val = row[column_name]
        try:
            num = float(val)
            value.append(num)
        except ValueError:
            continue  # skip non-numeric rows

print(f"Read {len(value)} numeric values from {column_name}")
        
    
# compute the mean, median, and mode of the "ARREST_PRECINCT" column
# Mean = sum / count
total = 0
for v in value:
    total += v

mean = total / len(value)
print(f"Mean: {mean:.2f}")

# Median = middle value when sorted
sorted_values = sorted(value)
n = len(sorted_values)
if n % 2 == 1:
    median = sorted_values[n//2]
else:
    median = (sorted_values[n//2-1]+sorted_values[n//2])/2
print(f"median: {median:.2f}")

# Mode = most frequent value
from collections import Counter
counter = counter = Counter (value)
mode_data = counter.most_common(1)
mode = mode_data [0][0]
print (f"mode: {mode:.2f}")
