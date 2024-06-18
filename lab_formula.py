#!/bin/python3

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# self made modules
import utils

df = pd.read_csv("index_of_refraction.csv")
print(df)

def get_n(N, theta, wavelength, thickness):
    return (
        (
                (
                    N * wavelength / (2 * thickness)
                    + np.cos(np.radians(theta)) - 1
                )**2 
            + 
                np.sin(np.radians(theta))**2
        )/(
            2 *
            (
                - N * wavelength / (2 * thickness)
                - 
                np.cos(np.radians(theta)) + 1
            )
        )
    )

n_array = get_n(df["N"], df["decimal"], 0.5, 0.825e5)
print(n_array.mean())
