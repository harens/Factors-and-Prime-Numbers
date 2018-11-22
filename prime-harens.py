# /usr/bin/env python

# This file is part of Factors-and-Prime-Numbers.

# Types-and-Variables is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# Factors-and-Prime-Numbers is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with List-Questions.  If not, see <http://www.gnu.org/licenses/>.

# NOTE `print` is required to display output
# Example: print(is_prime(8))

import sympy  # Used for `small` functions
import math  # Used for `small` functions
import time  # Times factors function


def is_prime(num):
    if num > 1:
        for prime_counter in range(2, (num // 2) + 1):
            if num % prime_counter == 0:  # Checks if output is a float
                return False
        return True
    return False  # False for anything below 2


def even_smaller_prime(num):
    return sympy.isprime(num)


def factors(num):
    factor_list = []
    if num < 2:  # For 1 and 0
        factor_list.append(num)
        return factor_list
    list_position = 0  # Position in list to insert
    for list_counter in range(1, num // 2):
        if (
            num % list_counter == 0
            and factor_list.count(list_counter) == 0  # Can't already be in list
        ):
            factor_list.insert(list_position, list_counter)
            factor_list.insert(list_position + 1, int(num / list_counter))
            list_position += 1
    return factor_list


def hcf(x, y):
    start_time = time.time()  # Starts timing function
    factor_counter = x
    if x > y:  # Sets factor_counter to lowest number
        factor_counter = y
    while factor_counter > 0:
        if x % factor_counter == 0 and y % factor_counter == 0:
            end_time = time.time()
            print("Total time (roughly):", end_time - start_time, "seconds")
            return factor_counter
        factor_counter -= 1  # Decreases until it can divide both x and y

def even_smaller_hcf(x, y):
    return math.gcd(x, y)
