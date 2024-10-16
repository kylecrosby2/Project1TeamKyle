#! python3

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the CSV file
file_path = 'output/output_teamkyle.csv'
data = pd.read_csv(file_path)

# Prepare the data for plotting
x = data['Number of variables']
y = data['Exec Time (microseconds)']
combo = data['Combo']

# Classify the points as satisfiable or unsatisfiable
unsatisfiable = data[combo == '[]']
satisfiable = data[combo != '[]']

# Create the plot
plt.figure(figsize=(10, 6))

# Plot the satisfiable and unsatisfiable points (leaving the graph unchanged)
plt.scatter(unsatisfiable['Number of variables'], unsatisfiable['Exec Time (microseconds)'], 
            color='red', label='Unsatisfiable', marker='x')
plt.scatter(satisfiable['Number of variables'], satisfiable['Exec Time (microseconds)'], 
            color='green', label='Satisfiable', marker='o')

#  ---- Curve fit ----

# Define a manual exponential function
def manual_exp(x, a, b):
    return a + b * np.power(2, x)

# Manually set the values of 'a' and 'b'
a = 46 
b = 0.30  

# Generate x values for the curve
line_x = np.linspace(unsatisfiable['Number of variables'].min(), unsatisfiable['Number of variables'].max(), 100)
line_y = manual_exp(line_x, a, b)

# Plot the manual exponential curve
plt.ylim(y.min(), 10000)
plt.plot(line_x, line_y, color='blue', linestyle='--', label=f'Bounding Curve: {a} + {b}*2^x')

# -------------------------

# Add labels and title

plt.xlabel('Number of Variables (coins in jar)')
plt.ylabel('Execution Time (μs)')
plt.title('Execution Time vs Number of Variables')

# Add a grid and legend
plt.grid(True)
plt.legend()

# Show the plot
plt.show()
