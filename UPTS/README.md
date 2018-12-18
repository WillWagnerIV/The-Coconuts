# UPTS - Unified Player Tracking System

This is a simple Proof Of Concept for an internal developer tool for tracking and working with player, game and user data in Python.  The application allows a developer group to input and output to and fram a MySQL database as well as reading to and from json files.  It has integrated support for Pandas and Numpy, making it an ideal tool to work with other data science modules.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Prerequisites

You will need a combination of the following...

Either iPython (includes Python 3.7, Pandas, Numpy and requests):
```
pip install ipython
```

or install them individually:
```
pip install python3.7
pip install pandas
pip install numpy
pip install requests
```

After installing the above requirements, install the following:
```
pip install mysql-connector
```


## Installation Instructions

After installing the prerequisites, do one of these:

### tar Package Installation

1.) You can download the tar or the wheel here:

<https://github.com/WillWagnerIV/The-Coconuts/tree/master/UPTS/dist>

2.) move the downloaded tar to your working directory

3.) Double-Click on the tar to unpack it

4.) use Python to run upts_main.py
    upts_main.py is located in upts_pypoc/src


### testPyPi URL installation as Python module

This project uses testPyPi for easy pip installation, however...

**testPyPi erases its content without warning to create space for new test projects.**

If there are any errors with testPyPi, please use the tar package instructions.

### testPyPi Installation

You can use pip to install from TestPyPI:

1.) Activate your virtual env (for example):
```
env/bin/activate
```
2.) cd to your working directory.
```
cd path/to/awesomeness
```
3.) Install with the following command:
```
pip install --index-url https://test.pypi.org/ upts_pypoc
```


### Alternate Installation

1.) You can download the tar and the wheel here:

<https://github.com/WillWagnerIV/The-Coconuts/tree/master/UPTS/dist>

2.) copy the downloaded files to your working directory

3.) cd to your working directory.
```
cd path/to/awesomeness
```
4.) Activate your virtual env
```
env/bin/activate
```
5.) use pip to install the archive.  The following is example code.  Please change the path (~/Documents/TestArea) to match your downloaded tar location.
```
pip install --no-index ~/Documents/TestArea upts_pypoc
```



## Test Your Installation

You can test that it was installed correctly by running it from your Python interpreter.

Start your Python interpreter (make sure you are still in your virtualenv if you are using one):
```
ipython
```
And then simply import *upts_pypoc*.
```
import upts_main
```


### OR - If you unpacked the .tar to edit the python files

upts_main.py is located in ```upts_pypoc/src```

Simply run *upts_main*.
```
run upts_main.py
```



## Running the included tests

To run the tests, you will need to install pyTest and optionally pytest-coverage
```
pip install pytest
pip install pytest-cov
```

To run the accompanying tests with coverage, you can execute the following code from the upts_pypoc folder.
```
pytest -s -v --cov=src tests/test_upts.py
```


## Deployment

For purposes of the class project, we have deployed a MySQL server that will be accessed by this program.  This server is not secure and no personal information should be stored on the server.  The default server may be shut down at any point by CGU.  

Any further deployment would require a MySQL or equivalent database server running either locally or remotely.  This would need to be set up prior to using the program.

The database variables at the beginning should be customized for your database.



## Authors

* **William Wagner** 
* Manar Al-kayed

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Thanks to Professor Wallace Chipidza for lots of help and knowledge


