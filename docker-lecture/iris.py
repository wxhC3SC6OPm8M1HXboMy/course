import pandas as pd
from datetime import datetime

INPUT_FILE = "iris.csv"
OUTPUT_FILE = "iris_averages.txt"

# Define column names for the Iris dataset
column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']

# Read the CSV file into a DataFrame
iris_data = pd.read_csv(INPUT_FILE, header=None, names=column_names)

# Display the first few rows of the DataFrame
print(iris_data.head())

# Calculate the average of each feature
averages = iris_data[column_names[0:-1]].mean()

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

# Write the averages to a file
with open(OUTPUT_FILE, 'w') as f:
    f.write(f'The current time is {current_time}\n')
    f.write('Averages of Iris dataset features:\n')
    for feature, avg in averages.items():
        f.write(f'{feature}: {avg}\n')
