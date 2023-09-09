import json
import pandas as pd
import matplotlib.pyplot as plt
import os

# Set the working directory
#os.chdir(directory_path)

# Clear variables from memory (Not necessary in Python)
# You can skip this step in Python

# Set working directory (Not necessary in Python)
# You can skip this step in Python

# Load JSON data
with open("./simulation_results/greedy_allocator.json", "r") as greedy_file:
    greedy_data = json.load(greedy_file)

with open("./simulation_results/random_allocator.json", "r") as random_file:
    random_data = json.load(random_file)

# Create a 2x2 grid of subplots
fig, axs = plt.subplots(2, 2)

# Print the head of random_data
print(random_data[:5])  # Assuming you want to print the first 5 elements

# Extract and calculate average for greedy_uti_r
greedy_uti_r = greedy_data[3]
greedy_uti_r_average = sum(greedy_uti_r) / len(greedy_uti_r)
print(greedy_uti_r_average)

# Extract and calculate average for random_uti_r
random_uti_r = random_data[3]
random_uti_r_average = sum(random_uti_r) / len(random_uti_r)
print(random_uti_r_average)

# Plot histograms
axs[0, 0].hist(greedy_uti_r, color="blue")
axs[0, 1].hist(random_uti_r, color="red")

# Boxplots
axs[1, 0].boxplot(greedy_uti_r, labels=["Greedy"], vert=False)
axs[1, 1].boxplot(random_uti_r, labels=["Random"], vert=False)

# Adjust layout
plt.tight_layout()

# Show the plots
plt.show()
