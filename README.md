# Installation
First of all, what should already be installed on this machine?

- Python 3.7+
- an appropriate pip version for your Python version

## Install requirements
If you want to install these requirements on your own machine, execute the following step. \
NOTE: we assume "pip" is the cli command needed to call the pip process, this may be "pip3" in your case.

- pip install -e .

If you prefer to install these requirements to a virtual environment, follow the following steps. \
NOTE: we assume "python" is the cli command needed to call the python process, this may be "python3" in your case.

Open a cmd terminal and navigate to the folder containing the repo. \
Then execute these commands in order.

0. pip install virtualenv

### Windows

1. python -m venv venv
2. .\venv\Scripts\activate.bat
3. pip install -e .

### Unix/macOS

1. python -m venv venv
2. source venv/bin/activate
3. pip install -e .

## Running the API

To run the API, simply open a terminal, navigate to the repo folder. \
If you have installed the requirements in a virtual environment, make sure it's active (see step 2 in installation for your OS). \
Now run the following command.

- python main.py

The API will now begin running, make sure you do not close this terminal for as long as you require the API to be active.

## Navigating the API

An extremely basic webpage has been created for you to more easily enter information and navigate the API without needing to know the endpoints. \
To access this, open the index.html file included in the repository. \
Each section is one part of the task.

## Running the tests.

In order to run the tests, open a new terminal (make sure the API remains active). \
Once again, navigate to the repository, then execute the following command.

- python test.py

This will run all the tests, if the test passes, a dot will be printed. \
If the test fails, a capital letter "F" will be printed. \
If an error occurs, a capital letter "E" will be printed. \
When all the tests have run, you will get a really short summary of the results.

The tests should take about 30 seconds in total. \
These tests include testing the results the API gives, as well as unittests for the written back-end code.
