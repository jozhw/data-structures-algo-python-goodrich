"""R-5.6 Our implementation of insert for the DynamicArray class, as given
in Code Fragment 5.5 has the following inefficiency. In the case when a resize
occurs, the resize operation takes time to copy all the elements from an old
array to a new array, and then the subsequent loop in the body of insert shift
many of those elements. Give an improved implementation of the insert method,
so that, in the case of a resize, the elements are shifted into their final
position during that operation, thereby avoiding subsequent shifting."""

import ctypes


class DynamicArray:
    """A dynamic array class akin to a simplified Python list"""

    def __init__(self) -> None:
        """Create an empty array"""

        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)

    def _make_array(self, c):
        """Return new array with capacity c."""
        return (c * ctypes.py_object)()

    # modify
    def insert(self, k, value):
        """To make this algo more efficient make it so that you create
        a new array that is double the existing when needed and append
        all of the values that are indexed before the point of insertion
        and then append the values that are to be inserted and then
        append the remaining values. This would give this algo O(n) time
        complexity"""

        # resize array if met capacity
        if self._n == self._capacity:
            new_array = self._make_array(2 * self._capacity)
            # insert all values before insert position
            for index in range(k):
                new_array[index] = self._A[index]
            # insert new value
            new_array.push(value)
            # insert all values after the insert
            for index in range(k, self._n):
                new_array[index + k] = self._A[index + k]
                self._A = new_array
        else:
            for j in range(self._n, k, -1):
                self._A[j] = self._A[j - 1]
            self._A[k] = value
        self._n += 1
