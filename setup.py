from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="MLOPS-Hotel-Reservation-Prediction",
    version="0.1",
    author="Ashwini Patil",
    packages=find_packages(),
    install_requires = requirements,
)