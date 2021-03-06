from setuptools import find_packages, setup

with open("README.md") as fh:
    long_description = fh.read()

setup(
    name='qiime-studio',
    version='0.0.1dev',
    long_description=long_description,
    packages=find_packages(),
    install_requires=['click', 'flask', 'gevent']
)
