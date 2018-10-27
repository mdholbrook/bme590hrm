# Heart rate project
Heart rate monitor project for BME590 - Medical Software Design

This purpose of this project is to develop code which can calculate useful statistics from an ECG read from file. A dual part of this project is proper code development methods, involving good Git practices, detailed documentation, and integrated unit testing on Github.

#### Travis contiuous integration status
[![Build Status](https://travis-ci.org/travis-ci/travis-web.svg?branch=master)](https://travis-ci.org/travis-ci/travis-web)

## Instructions
 The main function in this this project is ``heart_rate_monitory.py``. This script is used to call all other methods used in this project.
 
 This script is run via the command line. There are additional arguments which are required to run the code. The syntax for running the program is as follows:
 
 ``python heart_rate_monitor.py path/to/data_file.csv StartTime EndTime``
 
 The first argument defines the relative or absolute path to the test data, e.g. ``test_data/test_data1.csv``. All of the test data for this project are found in the ``test_data/`` folder.
 
 The second two arguments are numbers (integer or decimal) **_in minutes_** which denote the time interval used for calculating average heart rate. These parameters are *optional*, though warnings will be thrown when they are omitted. The behavior of the code with these parameters is as follows:
 * If no parameters are given, the entire duration of the ECG is used for heart rate calculations
 * If one parater is given, then it is assumed to denote the interval duration starting from the beginning of the ECG file
  * If two parameters are passed, the code will calculate mean heart rate between the two parameters
    * **Note:** If the first number is larger than the second, a warning will be sent and the second number will be ignored and the code will act as though there were only one input
 * If the input duration is outside the time spanned in the ECG file, the the program will use the entire duration of the ECG file for its calculations
    
  The code will calculate a series of metrics based on these inputs that will be displayed both in the terminal window and written to disk as a ``JSON`` file. The file will be written in a created folder called ``output_data/`` found in the root path. The calculated metrics are contained in a dictionary with the following fields:
  * ``num_beats``: the number of heart beats
  * ``beats``: time at which beats occur
  * ``voltage_extremes``: the minimum and maximum voltages in the input ECG
  * ``mean_hr_bpm``: mean heart rate in beats per minute calculated over the input time span
