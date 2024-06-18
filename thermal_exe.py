#!/bin/python3

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

up_df = pd.read_csv("thermal_upwards.csv")
down_df = pd.read_csv("thermal_downwards.csv")

print(down_df)

# pandas is quite retarted:
# up_df.columns = up_df.columns.str.strip()
# down_df.columns = down_df.columns.str.strip()

print(up_df.columns)
print(down_df.columns)


plt.scatter(up_df["temperature"], up_df["N"], label="up")
plt.scatter(down_df["temperature "], 300 - down_df["N"], label="down")
plt.xlabel("temperature")
plt.ylabel("N")
plt.legend()

plt.savefig("plots/thermal.png")
plt.show()
