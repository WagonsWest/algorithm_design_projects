#! /usr/bin/python3

import sys
import random
from a1p5 import expexp

"""
Some tests.

If you set this file to executable, and have the a1p5.py file in
the same folder, then you should be able to run this. You can and should
of course try your own tests.
"""

def main():
    print('Test 1:', end = ' ')
    r = expexp(1, 1, 1, 2)

    if r == 1:
        print('Passed')
    else:
        print('Failed')


    print('Test 2:', end = ' ')
    r = expexp(2, 2, 2, 31)

    if r == 16:
        print('Passed')
    else:
        print('Failed')

    print('Test 3:', end = ' ')
    r = expexp(103, 12, 112, 127)

    if r == 1:
        print('Passed')
    else:
        print('Failed')

    print('Test 4:', end = ' ')
    r = expexp(104, 12, 112, 127)

    if r == 4:
        print('Passed')
    else:
        print('Failed')

if __name__ == '__main__':
    main()
