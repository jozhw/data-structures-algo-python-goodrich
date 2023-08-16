import typing
from copy import deepcopy

# R-2.1
"""surgical robots; self-driving cars; vital monitors"""

# R-2.2

"""virtually any application that seeks to retain or gain market share will
need to have adaptibility, otherwise the self-imposed limitations on clients
with various hardware specifications will
be lost"""

# R-2.3

# R-2.4


class Flower:
    def __init__(self, name: str, petals: int, price: float):
        self.name = name
        self.petals = petals
        self.price = price

    # set new values of each variable

    def set_name(self, new_name: str):
        self.name = new_name

    def set_petals(self, new_petals: int):
        self.petals = new_petals

    def set_price(self, new_price: float):
        self.price = new_price

    # get values
    def get_name(self):
        return self.name

    def get_petals(self):
        return self.petals

    def get_price(self):
        return self.price


# R-2.5

"""within the make_payment class method, add a try/except clause to catch to
see if it is a float or integer
for example:
    def make_payment(self, amount):
        try:
            amount = float(amount)
        except:
            print("The amount must be a number")
    """

# R-2.6
"""
        def make_payment(self, payment):
            if (payment < 0):
                continue
                return
            raise ValueError('Value cannot be negative')

"""


# R-2.7
class CreditCard:
    def __init__(
        self, customer: str, bank: str, acnt: float, limit: float, starting_balance=0
    ):
        self.customer = customer
        self.bank = bank
        self.acnt = acnt
        self.limit = limit
        self.starting_balance = starting_balance


# R-2.8
"""
Question seems open ended. If the question wants only the for loop range to be changed and not
the command then we can determine which reaches first by the difference in the ratio and the rates.

1. sum from n=1 to n=x of n = 2500
2. sum from n=1 to n=x of 2*n = 3500 = sum of ... of n = 1750
3. sum from n=1 to n=x of 3*n = 5000 = sum of ... of n = 1633.33....

Thus the x for the third equation is smaller than the first and second. This means that the
first to exceed the credit limit is the third.
"""


# R-2.9 - R-2.15
class Vector:
    # R-2.15
    def __init__(self, d):
        if isinstance(d, int):
            self._coords = [0] * d
        elif isinstance(d, list):
            self._coords = d

    def __len__(self):
        return len(self._coords)

    def __getitem__(self, j):
        return self._coords[j]

    def __setitem__(self, j, val):
        self._coords[j] = val

    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError("dimensions must agree")
        result = Vector(len(self))
        for i in range(len(self)):
            result[i] = self[i] + other[i]
        return result

    # R-2.11
    def __radd__(self, other):
        """uses __add__ but switches the position of other"""
        return self + other

    # R-2.9
    def __sub__(self, other):
        if len(self) != len(other):
            raise ValueError("dimensions must agree")
        result = Vector(len(self))
        for i in range(len(self)):
            result[i] = self[i] - other[i]
        return result

    def __eq__(self, other):
        return self._coords == other._coords

    def __ne__(self, other):
        return not self == other

    def __str__(self):
        return "<" + str(self._coords)[1:-1] + ">"

    # R-2.10
    def __neg__(self):
        result = deepcopy(self)

        for i in range(len(self)):
            result[i] = self[i] * -1

        return result

    # R-2.12
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            result = Vector(len(self))
            for i in range(len(self)):
                result[i] = self[i] * other
            return result
        # R-2.14
        elif isinstance(other, Vector):
            result = 0
            for i in range(len(self)):
                result += self[i] * other[i]
            return result

    # R-2.13
    def __rmul__(self, other):
        return self * other


# R-2.16
# self explanatory with an example

# R-2.17
# just drawing diagrams for classes

# R-2.18
# just add a self._array to store all of the values of the progression
# and within a method to get value given index

# R-2.19
# given start is 0 and increments 128 every time, the answer will be
# 2^63/128 + 1 times

# R-2.20
# hard to pinpoint a bug and hard to keep track of all of the methods
# as well as methods that are useless for a particular class
# being inherited
# there it is not good in a design perspective

# R-2.21
# redundancy and it increases memory overhead since every instance of
# a class allocates memory to it

# R-2.22
from abc import ABCMeta, abstractmethod

'''
class Sequence(metaclass=ABCMeta):
    @abstractmethod
    def __len__(self):
        """Return length of sequence"""

    @abstractmethod
    def __getitem__(self, j):
        """Return the element at index j of the sequence"""

    def __contains__(self, val):
        for j in range(len(self)):
            if self[j] == val:
                return True
            else:
                return False

    def index(self, val):
        for j in range(len(self)):
            if self[j] == val:
                return j
            raise ValueError("value not in sequence")

    def count(self, val):
        k = 0
        for i in range(len(self)):
            if self[i] == val:
                k += 1
        return k

    # answer
    def __eq__(self, val):
        if isinstance(val, Sequence):
            if len(self) != len(val):
                return False
            else:
                for i in range(len(self)):
                    if self[i] != val[i]:
                        return False
                return True
'''
# R-2.23
# refering to length of the sequence? if so implementation is simple
# compare the lens and return true or false
