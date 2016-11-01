import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'readme.md')) as readme:
    README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='csgoexchange',
    version='0.0.1',
    packages=['csgoexchange'],
    include_package_data=True,
    url='https://github.com/xacce/csgoexchange',
    license='BSD License',
    author='xacce',
    author_email='thisice@gmail.com',
    description='',
    long_description=README,
    install_requires=[
        'requests',
        'bs4',
    ],
)
