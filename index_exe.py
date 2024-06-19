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

# def model(angle, n_glass):
#     t = 0.825e5 # cm
#     wavelength = 0.53
#     return 1 / wavelength * (n_glass - 1) * (t/np.cos(np.radians(angle)) - t)

def model(angle, n):
    try:
        t = 0.825e5 # cm
        wavelength = 0.53

        a = wavelength**2
        b = (n - (wavelength * angle**2)/2)/t
        c = wavelength * (1 - angle)

        D = b**2 - 4*a*c

        if D < 0:
            raise   
        
        return (-b + np.sqrt(b**2 - 4*a*c))/(2*a)
    except Exception as e:
        return np.nan

# def model(angle, n):
#     term1 = N * 

params, error_matrix = curve_fit(model, df["angle"], df["N"], p0=[1])

angle_array = np.linspace(0, 5, 1000)
fitted_N_array = [model(angle, *params) for angle in angle_array]

plt.plot(angle_array, fitted_N_array)

print(f"Index: {params[0]}")
plt.savefig("plots/my-formula.png")

print(params)
plt.show()


