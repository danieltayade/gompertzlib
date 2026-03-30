import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Gompertz function
def gompertz(x, a, b, c):
    return a * np.exp(-b * np.exp(-c * x))

# Fit function
def fit_curve(x, y):
    params, _ = curve_fit(gompertz, x, y, maxfev=10000)
    return params  # a, b, c

# Predict function
def predict(x, a, b, c):
    return gompertz(x, a, b, c)

# Plot function
def plot_fit(x, y, a, b, c):
    y_pred = gompertz(x, a, b, c)

    plt.scatter(x, y, label="Actual")
    plt.plot(x, y_pred, color='red', label="Gompertz Fit")
    plt.legend()
    plt.show()