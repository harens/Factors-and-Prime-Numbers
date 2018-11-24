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

from sympy import factorint  # Used for `small` prime factors


def is_prime(num):
    if num == 2 or num == 3:
        return True
    elif (
        num > 1 and num % 2 != 0 and num % 3 != 0
    ):  # False for anything below 2 or divisible by 2 or 3
        for prime_counter in range(2, (num // 2) + 1):
            if num % prime_counter == 0:  # Checks if output is a float
                return False
        return True
    return False


def smaller_prime(num):
    return sympy.isprime(num)


def factors(num):
    factor_list = []
    if num < 2:  # For 1 and 0
        return [num]
    elif is_prime(num) is True:
        return [1, num]
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


def smaller_hcf(x, y):
    return math.gcd(x, y)


def perfect_number(limit):
    perfect_list = []
    for perfect_counter in range(6, limit + 1):  # 6 is the first perfect number
        perfect_sum = sum(factors(perfect_counter)) - perfect_counter
        if perfect_sum == perfect_counter:
            perfect_list.append(perfect_counter)
    return perfect_list


def prime_generator(num1=1, num2=1000):
    prime_list = []
    for prime_counter in range(num1, num2):  # Less than but not equal to number
        if is_prime(prime_counter) is True:
            prime_list.append(prime_counter)
    return prime_list


def smaller_prime_generator(num1=1, num2=1000):
    return [number for number in sympy.primerange(num1, num2)]  # Acts as a generator


def prime_factors(num):
    if is_prime(num) is True:
        return [num]
    divide_number = 2
    factor_list = []
    while num != 1:
        if num % divide_number == 0:
            num /= divide_number
            factor_list.append(divide_number)
        else:
            divide_number += 1
            while is_prime(divide_number) is False:
                divide_number += 1
    return factor_list


def smaller_prime_factors(num):
    return factorint(num, multiple=True)  # Outputs as list rather than dictionary


print(is_prime(0))

# PYTESTS


class CHECK_FUNCTIONS(object):
    def is_prime_check(self):
        assert is_prime(0) is False
        assert is_prime(9) is False
        assert is_prime(-1) is False

        assert is_prime(2) is True
        assert is_prime(29) is True
        assert is_prime(31) is True

    def smaller_prime_check(self):
        assert smaller_prime(0) is False
        assert smaller_prime(9) is False
        assert smaller_prime(-1) is False

        assert smaller_prime(2) is True
        assert smaller_prime(29) is True
        assert smaller_prime(31) is True

    def factors_check(self):
        assert factors(1) == [1]
        assert factors(12) == [1, 2, 3, 4, 6, 12]

    def hcf_check(self):
        assert hcf(12, 4) == 4
        assert hcf(13, 2) == 1

    def smaller_hcf_check(self):
        assert smaller_hcf(12, 4) == 4
        assert smaller_hcf(13, 2) == 1
