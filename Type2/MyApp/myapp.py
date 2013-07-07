#!/usr/bin/env python
import sys

def sum(a, b):
    return a + b

def difference(a, b):
    return a - b

def main(argv):
    a = int(argv[1])
    b = int(argv[2])
    print "Sum of %s and %s is %s"%(a, b, str(sum(a,b)))
    print "Difference of %s and %s is %s"%(a,b,str(difference(a,b)))

if __name__ == '__main__':
    main(sys.argv)

