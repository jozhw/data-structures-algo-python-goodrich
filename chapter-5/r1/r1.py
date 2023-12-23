"""R-5.1 Execute the experiment from Code Fragment 5.1 and compare the results on your
system to those we report in Code Fragment 5.2"""
import sys

data = []
for k in range(27):
    a = len(data)
    b = sys.getsizeof(data)
    print("Length: {0:3d}; Size in bytes: {1:4d}".format(a, b))
    data.append(None)
