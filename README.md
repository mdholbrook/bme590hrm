# Heart rate project
_Heart rate monitor project for BME590 - Medical Software Design_

This purpose of this project is to develop code which can calculate useful statistics from an ECG read from file. A key part of this project is the use of proper software development methods, including good Git practices, detailed documentation, and integrated unit testing on Github.

#### Travis contiuous integration status
[![Build Status](https://travis-ci.org/travis-ci/travis-web.svg?branch=master)](https://travis-ci.org/travis-ci/travis-web)

## Instructions
 The main function in this this project is ``heart_rate_monitory.py``. This script is used to call all other methods used in this project.
 
 This script is run via the command line. There are additional arguments which are **required** to run the code. The syntax to run the program is as follows:
 
 ``python heart_rate_monitor.py path/to/data_file.csv StartTime EndTime``
 
 The first commandline argument defines the relative or absolute path to the ECG file, e.g. ``test_data/test_data1.csv``. All of the test data for this project are found in the ``test_data/`` folder.
 
 The second two arguments are numbers (integer or decimal) **_in minutes_** which denote the time interval used for calculating average heart rate. These parameters are *optional*, though warnings will be thrown when they are omitted. The behavior of the code with these parameters is as follows:
 * If no parameters are given, the entire duration of the ECG is used for heart rate calculations
 * If one parameter is given, then it is assumed to denote the interval duration starting from the beginning of the ECG file
  * If two parameters are passed, the code will calculate the mean heart rate in the time between the two parameters
 * If the input parameters denote a duration outside the time spanned in the ECG file, the the program will use the entire duration of the ECG file for its calculations
    
  The code will calculate a series of metrics based on these inputs that will be displayed both in the terminal window and written to disk as a ``JSON`` file. The file will be written in a automatically generated results folder, ``output_data/``, found in the root path. The calculated metrics are contained in a dictionary with the following fields:
  * ``num_beats``: the number of heart beats in the ECG file
  * ``beats``: time at which each beat occurs
  * ``voltage_extremes``: the minimum and maximum voltages in the ECG trace
  * ``mean_hr_bpm``: mean heart rate, in beats per minute, calculated over the time spanned by ``StartTime`` and ``EndTime``
