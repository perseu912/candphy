from setuptools import setup
from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    readme = fh.read()

setup(name='candphy',
    version='0.0.202',
    url='https://github.com/perseu912/candphy',
    license='MIT License',
    author='Reinan Br',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='slimchatuba@gmail.com',
    keywords='covid-19 covid api data science',
    description=u'Library for works in the physical projects',
    packages=find_packages(),
    install_requires=['pyrtlsdr','bs4','requests','soundfile','pandas','h5py','astropy','scipy','toddy','numpy','matplotlib','pillow','qutip'],)
