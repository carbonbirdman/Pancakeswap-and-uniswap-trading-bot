from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize(["pancakeswap_bot.py","swap.py"])
)

# at the command line use this
# python setup.py build_ext --inplace
