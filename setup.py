from setuptools import setup, find_packages

setup(
    name="gompertzlib",           # PyPI package name
    version="0.1",
    packages=find_packages(),      # find all subpackages automatically
    install_requires=[
        "numpy",
        "scipy",
        "matplotlib",
        "pandas"
    ],
    python_requires='>=3.8',
)