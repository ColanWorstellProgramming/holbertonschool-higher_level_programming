#!/usr/bin/python3
__main__ = __name__
from add_0 import add
a = 1
b = 2
print('{one}'.format(one=a), '+', '{two}'.format(two=b), '=', '{results}'.format(results=add(a, b)))
