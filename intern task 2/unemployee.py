import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the data into a pandas DataFrame
df = pd.read_csv("unemployment.csv")

# Clean the data
df = df.dropna()
df["unemployment_rate"] = df["unemployment_rate"].astype(float)

# Visualize the data
plt.plot(df["year"], df["unemployment_rate"], marker="o")
plt.xlabel("Year")
plt.ylabel("Unemployment Rate (%)")
plt.title("Unemployment Rate Over Time")
plt.show()