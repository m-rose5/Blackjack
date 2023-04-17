from setuptools import setup, Extension

module = Extension("BlackJack", sources = ["main.c"])

setup(name="BlackJack",
	version = "0.01",
	description = "Contains functions for the logic of the black jack game",
	exp_modules = [module]
)

