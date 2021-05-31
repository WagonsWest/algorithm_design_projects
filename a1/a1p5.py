"""
ECE406, W'21, Assignment 1, Problem 5
Skeleton solution file.
"""

"""
You are not allowed to import anything. If we see any import
statement, you earn an automatic 0.

You should adopt reasonable assumptions for the time-efficiency of
built-in operators and functions. E.g., you should assume that a//b
and a%b to compute floor(a/b) and a mod b, respectively, each run in
time O(n^2) where n = log a + log b. It is NOT reasonable to assume
that they run in constant-time.
"""
def pow_mod(a, b, c):
    if b == 0:
        return 1
    elif b == 1:
        return a%c
    else:
        if b%2 == 0:
            return (pow_mod(a, b//2, c)*pow_mod(a, b//2, c))%c
        else:
            return (pow_mod(a, b//2, c)*pow_mod(a, b//2, c)*a%c)%c


def expexp(x,y,z,p):
    # a = pow(y, z, p-1)
    # return pow(x, a, p)
    temp = pow_mod(y, z, p-1)
    return pow_mod(x, temp, p)

# By Fermat's little theorem, x**p-1 = 1 (mod p)
# let temp = y**z (mod p-1)
# result = x**temp (mod p)
# Since a%c runs in time O(n^2) where n = log a + log c and pow_mod(a, b, c) runs in time O(log b)*O((log a + log b)^2);
# expexp(x,y,z,p) runs in time O((log n)^3) 

"""
You need to implement this method.

You are certainly allowed to define any subroutines you want
above this method in this file.

We will test with inputs that match the spec only. I.e., all of
x,y,z,p will be positive integers, and p will be a prime.
"""