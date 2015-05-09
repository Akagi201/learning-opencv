#!/usr/bin/env python

from numpy import *

# sample
print ('#' * 15 + ' sample ' + '#' * 15)

a = arange(15).reshape(3, 5)

print a

print a.shape

print a.ndim

print a.dtype.name

print a.itemsize

print a.size

print type(a)

b = array([6, 7, 8])

print b

print type(b)

# create ndarray
print ('#' * 15 + ' create ndarray ' + '#' * 15)

a = array([2,3,4])
print a
print a.dtype
b = array([1.2, 3.5, 5.1])
print b.dtype

c = array([(1.5, 2, 3), (4, 5, 6)])
print c

d = array([[1, 2], [3, 4]], dtype = complex)
print d

print zeros((3, 4))
print ones((2,3,4), dtype=int16)
print empty((2, 3))

print arange(10, 30, 5)

print arange(0, 2, 0.3)

# print ndarray
# 1d array
a = arange(6)
print a

# 2d array
b = arange(12).reshape(4,3)
print b

# 3d array
c = arange(24).reshape(2,3,4)
print c

# 4d array
d = arange(2*3*4*5).reshape(2,3,4,5)
print d

print arange(10000)

print arange(10000).reshape(100, 100)

#set_printoptions(threshold='nan')
#print arange(10000)

# basic operation
print ('#' * 15 + ' basic operation ' + '#' * 15)
a = array([20, 30, 40, 50])
b = arange(4)
print b
c = a - b
print c
print b**2
print 10 * sin(a)
print a < 35

A = array([[1,1],
[0,1]])
B = array([[2,0],
[3,4]])

# elementwise product
print A*B

# matrix product
print dot(A,B)

a = ones((2,3), dtype=int)
b = random.random((2,3))
a *= 3
print a
b += a
print b

# b is converted to integer type
a += b

print a

# upcast
