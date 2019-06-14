from setuptools import setup

setup(
    name='bcrypt',
    version='0.1.0',
    description='Native Python implementation of the py-bcrypt',
    url='https://github.com/erlichmen/py-bcrypt.git',
    author='Shay Erlichmen',
    author_email='erlichmen@gmail.com',
    license='MIT',
    packages=['bcrypt'],
    include_package_data=False,
    zip_safe=False)
