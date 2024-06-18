#!/bin/python3

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# self made modules
import utils

df = pd.read_csv("index_of_refraction.csv")
df.rename(columns={"decimal": "angle"}, inplace=True)

df["angle"] = df["angle"] 

print(df[["N", "angle"]])

plt.scatter(df["angle"], df["N"])
utils.mkdir("plots")

def model(angle, n_glass):
    t = 0.825e5 # cm
    wavelength = 0.53
    return 1 / wavelength * (n_glass - 1) * (t/np.cos(np.radians(angle)) - t)

params, error_matrix = curve_fit(model, df["angle"], df["N"])

# (angle, t, n_glass, n_air, wavelength) = params

angle_array = np.linspace(0, 5, 100)
fitted_N_array = model(angle_array, *params)

plt.plot(angle_array, fitted_N_array)

# plt.show()
print(f"Index: {params[0]}")
plt.savefig("plots/my-formula.png")
plt.show()


