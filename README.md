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
the tests. The directory structure is like this

    Projects/
        MyApp/
            __init__.py
            myapp.py
            test_myapp.py


Simply run the test from within the MyApp folder as

    % python test_myapp.py
    or
    % nosetests

##Type 2

The unit tests are located in its own tests folder in the package you want to
test. Running the unit tests from inside the tests folder won't work as it 
worked in Type 1. That's because the myapp module can not be resolved. Here is
how the directory structure looks like 

    Projects/
        MyApp/
            __init__.py
            myapp.py
            tests/
                __init__.py
                test_myapp.py

It will work if you ran it from inside the package folder and gave the complete
 path to the test file as

    % python tests/test_myapp.py

It will also work if you used the nose test runner from inside MyApp.
 
    % nosetests

It will also work from inside the tests folder if you added MyApp to your
PYTHONPATH, but that is an option I dont like.

##Type 3

This is where the tests folder is on the same level as the package folder. You
can not run the test scripts from within the tests folder as again it will not
be able to resolve the myapp package. Here is how the directory structure looks 
like
 
    Projects/
        MyApp/
            __init__.py
            myapp.py
        tests/
            __init__.py
            test_myapp.py


You can run the tests from within the MyApp package by referencing the tests
folder as 

    % python ../tests/test_myapp.py

As you are running the test from the package, the myapp module is automatically
in your PYTHONPATH. The other way of doing this would be by putting your
package in your PYTHONPATH, which I don't like to do. Then you can run the 
tests from its own location.
