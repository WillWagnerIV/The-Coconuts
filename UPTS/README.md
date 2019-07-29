# UPTS - Unified Player Tracking System

This is a simple Proof Of Concept for an internal developer tool for tracking and working with player, game and user data in Python.  The application allows a developer group to input and output to and fram a MySQL database as well as reading to and from json files.  It has integrated support for Pandas and Numpy, making it an ideal tool to work with other data science modules.


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Prerequisites

You will need a combination of the following...

Either iPython (includes Python 3.7, Pandas, Numpy and requests)
```
pip install ipython
```
or install them individually
```
pip install python3.7
pip install pandas
pip install numpy
pip install requests

```
Then install the following:
```
pip install mysql
pip install mysql-connector
```


## Installation Instructions

This project uses testPyPi for easy pip installation, however...

**testPyPi erases its content without warning to create space for new test projects.**

If there are any errors with testPyPi, please use the tar package instructions.


### testPyPi pip Installation ( Easiest )

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
pip install --index-url https://test.pypi.org/ upts_poc
```

### tar Package pip Installation

1.) You can download the tar or the wheel here:

<https://github.com/WillWagnerIV/The-Coconuts/tree/master/UPTS/dist>

2.) copy the downloaded tar to your working directory

3.) Activate your virtual env
```
env/bin/activate
```
4.) cd to your working directory.
```
cd path/to/awesomeness
```
5.) use pip to install the archive.  The following is example code. Change ~/test_env to 
      wherever you have your tar.
```
pip install --no-index --find-links=~/test_env upts_poc
```


### Alternate Installation - To work with the python files
### .tar Package no pip Installation

1.) You can download the tar or the wheel here:

<https://github.com/WillWagnerIV/The-Coconuts/tree/master/UPTS/dist>

2.) move the downloaded .tar to your working directory

3.) Double-Click on the .tar to unpack it



## Test Your Installation

You can test that it was installed correctly by running it from your Python interpreter.

Start your Python interpreter (make sure you are still in your virtualenv if you are using one):
```
ipython
```

And then simply run *upts_main*.
```
run upts_main.py
```
### OR - If you unpacked the .tar to edit the python files
upts_main.py is located in upts_poc/src

Start your virtualenv and ipython then navigate to upts_poc/src:
```
env/bin/activate
ipython
cd upts_poc/src
run upts_main.py
```


## Running the accompanying tests

To run the tests, you will need to install pyTest and optionally pytest-coverage
```
pip install pytest
pip install pytest-cov
```

To run the accompanying tests with coverage, you can execute the following code from the UPTS folder.
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


