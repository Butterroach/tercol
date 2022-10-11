from ast import keyword
from setuptools import setup, find_packages
classifiers = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='tercol',
    version='0.0.4',
    description='TerCol is a simple library that colors your text, I guess',
    long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
    url='',
    author='Sultan Marzouq',
    author_email='epicnoobcontactemail@gmail.com',
    license='MIT',
    classifiers=classifiers,
    keywords='terminal styling, colors, style',
    packages=find_packages(),
    install_requires=['']
)