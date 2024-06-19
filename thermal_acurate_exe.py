#!/bin/python3

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

accurate_df = pd.read_csv("accurate-thermal.csv")

REL_COUNT_ERR = 1/10 # 1 mistake every 10 counts
error_N = np.sqrt(accurate_df["N"]*REL_COUNT_ERR**2)
error_T = 0.2

def model(T, thermal_coefficient, T_0):
    return thermal_coefficient * (T - T_0)

params, error_matrix = curve_fit(model, accurate_df["T"], accurate_df["N"])

fit_T = np.linspace(30, 65, 1000)
fit_N = model(fit_T, *params)

plt.plot(fit_T, fit_N)
plt.errorbar(accurate_df["T"], accurate_df["N"], xerr=error_T, yerr=error_N,
             marker='.', linestyle='', capsize=5, ecolor="red")
print(params)
plt.show()

