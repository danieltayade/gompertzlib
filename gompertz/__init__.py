# gompertzlib/__init__.py
from .gompertz.model import prepare_data, fit_curve, predict, plot_fit

__all__ = ["prepare_data", "fit_curve", "predict", "plot_fit"]