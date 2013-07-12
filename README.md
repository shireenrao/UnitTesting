README
======

This project is to document the different ways a Python projects directory 
structure can be setup to also suport testing. The code used here is not
important. It's very trivial and its there to just prove a point. I am tryng 
to figure out the best way to do it for all my projects going forward. I am
only using the unittest framework. For execution I am executing the test
cases by either directly using python or by using the nose test runner. 

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

or use the nose test runner

    % nosetests

Test discovery works too

    % python -m unittest discover

##Type 2

Here the unit tests are located in its own tests folder in the package you want
to test. Running the unit tests from inside the tests folder won't work as it
worked in Type 1. That's because the myapp module can not be resolved. Here is
how the directory structure looks like 

    Projects/
        MyApp/
            __init__.py
            myapp.py
            tests/
                __main__.py
                __init__.py
                test_myapp.py

It will work if you ran it from inside the package folder and gave the complete
 path to the test file as

    % python tests/test_myapp.py

This will also work

    % python -m tests.test_myapp

As we have a __main__.py in the tests folder this will work too

    % python -m tests

It will also work if you used the nose test runner from inside MyApp.
 
    % nosetests

Test discovery works here too

    % python -m unittest discover

It will also work from inside the tests folder or outside the MyApp folder. If
you added MyApp to your PYTHONPATH, but that is an option I dont like. So,
instead of changing the PYTHONPATH, the best way is to write either a makefile
or a script to add your module just for the run. So if you are running from
outside the MyApp folder the command will be 

    % PYTHONPATH=MyApp python -m unittest discover

or

    % PYTHONPATH=MyApp python -m MyApp.tests

or
 
    % PYTHONPATH=MyApp python -m MyApp.tests.test_myapp

or

    % PYTHONPATH=MyApp nosetests

If running from inside tests folder you would run 

    % PYTHONPATH=../ python test_myapp.py

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
            __main__.py
            __init__.py
            test_myapp.py


You can run the tests from within the MyApp package by referencing the tests
folder as 

    % python ../tests/test_myapp.py

As you are running the test from the package, the myapp module is automatically
in your PYTHONPATH. The other way of doing this would be by putting your
package in your PYTHONPATH, which I don't like to do. Then you can run the 
tests from its own location. Test discovery does not work as far as I know.

Like in Type2 you can use a makefile or a script to temporarily change the
PYTHONPATH and execute the test cases.

These work from outside the MyApp folder

    % PYTHONPATH=MyApp python -m tests

or

    % PYTHONPATH=MyApp python -m tests.test_myapp

or

    % PYTHONPATH=MyApp python -m unittest discover

or

    % PYTHONPATH=MyApp nosetests
