README
======

This project is to document the different ways a directory structure can be
setup to do testing. The code used for testing is not important. I am tryng 
to figure out the best way to do it for all my projects going forward. I am
only using the unittest framework. For execution I am executing the test
cases directly using python.  You can also run all the tests using the nose 
testing framework. Just execute the command 'nosetests'.

##Type 1

The unit tests are located in the same package as the module being tested. This
is the easiest to implement and run. I don't have to do anything special to run
the tests. Simply run the test as

    % python test_myapp.py
    or
    % nosetests

##Type 2

The unit tests are located in its own tests folder in the package you want to
test. Running the unit tests from inside the tests folder won't work as it 
worked in Type 1. That's because the myapp module is not found.  It will work 
if you ran it from inside the package folder and gave the complete path to 
the test file as

    % python tests/test_myapp.py

It will also work if you used the nose test runner from inside the package.
 
    % nosetests

##Type 3

This is where the tests folder is on the same level as the package folder.
