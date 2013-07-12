import unittest
import test_myapp


if __name__ == "__main__":
#    unittest.TextTestRunner().run(test_myapp.suite())
    mytests = unittest.TestLoader().loadTestsFromModule(test_myapp)
    unittest.TextTestRunner().run(mytests)
