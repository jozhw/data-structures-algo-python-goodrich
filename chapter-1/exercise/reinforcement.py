from typing import List, Tuple, Any

# R-1.1
def is_multiple(n: int,m: int) -> bool:
    if m % n == 0:
        return True
    return False

# R-1.2
def is_even(k: int) -> bool:
    dic = {0: True, 2: True, 4: True, 6: True, 8: True}
    return bool(dic[int(str(k)[-1])])

# R-1.3
def min_max(data: list) -> Tuple:
    min = data[0]
    max = data[0]
    for i in data:
        if i < min:
            min = i
        if i > max:
            max = i
    return (min, max)

# R-1.4
def sum_squares(n: int) -> int:
    n = n -1
    if n <= 0:
        return 0
    else:
        return n**2 + sum_squares(n)

# R-1.5
def sum_alter(n: int) -> int:
    return sum([i**2 for i in range(n+1) if i != 0 and i !=n])

# R-1.6
def sum_odd(n: int, not_include: bool = True) -> int:
    if n <= 0:
        return 0
    elif n % 2 == 0:
        return sum_odd(n-1, not_include = False)
    elif n % 2 != 0:
        if not_include == True:
            return sum_odd(n-2, not_include = False)
        return n**2 + sum_odd(n-2, not_include = False)

# R-1.7
def sum_odd_alter(n: int) -> int:
    return sum([i**2 for i in range(n+1) if (i % 2 !=0) and (i != n)])

# R-1.8
"""
The equivalent in terms of s[j] to s[k] where k is negative
and j positive is the inverse of each other. For example s[k = -1] is the same
as s[j=n-1, where n is the length of the string]
"""

# R-1.9
"""
The range function has three arguments - start - stop (not inclusive) - step. In order to
obtain the a range of the following values 50, 60, 70, 80, use the following
range(50, 81, 10)
"""

# R-1.10
"Use range(-8,9,2)"

# R-1.11
def target_list(n: int) -> List:
    return [2**i for i in range(n)]

#R-1.12
import random
def choice_emulator(to_choose: List) -> Any:
    random_selection = random.randrange(len(to_choose))
    return to_choose[random_selection]
