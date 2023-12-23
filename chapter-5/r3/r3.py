"""R-5.3 Modify the experiment from Code Fragment 5.1 in order to
demonstrate that Python's list class occasionally shrinks the size of its underlying array
when elements are popped from a list"""

import sys

data = [None] * 26
for k in range(len(data)):
    data.pop()
    a = len(data)
    b = sys.getsizeof(data)
    print("Length: {0:3d}; Size in bytes: {1:4d}".format(a, b))
