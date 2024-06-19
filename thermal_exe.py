#!/bin/python3

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

up_df = pd.read_csv("thermal_up.csv")
down_df = pd.read_csv("thermal_downwards.csv")

print(down_df)

print(up_df.columns)
print(down_df.columns)

REL_COUNT_ERR = 1/10 # 1 mistake every 10 counts
error_up_N = np.sqrt(up_df["N"]*REL_COUNT_ERR**2)
error_down_N = np.sqrt(down_df["N"]*REL_COUNT_ERR**2)
error_up_T = 0.2
error_down_T = 0.1

plt.errorbar(up_df["T"], up_df["N"],
             xerr=error_up_T, yerr=error_up_N,
             label="up",
             marker='.', linestyle='', capsize=5)
plt.errorbar(down_df["temperature "], 300 - down_df["N"],
             xerr=error_down_T, yerr=error_down_N,
             label="down",
             marker='.', linestyle='', capsize=5)


from scipy.optimize import curve_fit

accurate_df = pd.read_csv("accurate-thermal.csv")

REL_COUNT_ERR = 1/10 # 1 mistake every 10 counts
error_N = np.sqrt(accurate_df["N"]*REL_COUNT_ERR**2)
error_T = 0.2

def model(T, thermal_coefficient):
    T_0 = 24.2
    return thermal_coefficient * (T - T_0)

params_accurate, error_matrix = curve_fit(model, accurate_df["T"], accurate_df["N"])
print(f"accurate: {params_accurate} pm {np.sqrt(np.diag(error_matrix))}")

params_up, error_matrix = curve_fit(model, up_df["T"], up_df["N"])
print(f"most points: {params_up} pm {np.sqrt(np.diag(error_matrix))}")

slope = params_up[0]
wavelength = .5 # μm
initial_length_rod = 8.98e6 # μm
thermal_expension_coefficient = slope * wavelength / (2*initial_length_rod)
print(f"thermal expansion coefficient = {thermal_expension_coefficient}")

fit_T = np.linspace(20, 65, 1000)
fit_N = model(fit_T, *params_accurate)

plt.plot(fit_T, fit_N)
plt.errorbar(accurate_df["T"], accurate_df["N"], xerr=error_T, yerr=error_N,
             marker='.', linestyle='', capsize=5,
             label="up - equilibrium")


plt.grid(which="major", linewidth=.8)
plt.minorticks_on()
plt.grid(which="minor", linewidth=.3)
plt.xlabel("temperature (°C)")
plt.ylabel("number of transitions")
plt.legend()
plt.savefig("plots/thermal.png")
