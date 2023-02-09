from setuptools import setup


setup(
    name= "Constructing Chemistry",
    version= "0.0.1",
    license= "MIT",

    url="https://github.com/Reverend-Toady/chemical-compound-maker",
    description= "A webapp to help in the making of chemical substances",
    long_description= open("README.md", "r").read(),

    author= "Aditya",
    author_email= "rev.toady.py@gmail.com",

    packages= ["ConstructingChemistry"],
    install_requires= open("requirements.txt").read().split("\n")
)