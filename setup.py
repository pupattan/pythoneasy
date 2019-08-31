from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='pythoneasy',
    version='1.1',
    url='https://github.com/pupattan/pythoneasy',
    license='MIT',
    author='pupattan',
    author_email='',
    description='PythonEASY APIs',
    long_description=long_description,
    packages=find_packages(),
    install_requires=[
          'requests',
          'beautifulsoup4',
      ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
