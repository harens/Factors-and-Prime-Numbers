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

import prime-harens
import pytest

def is_prime_check():
  assert prime-harens.is_prime(0) is False
  assert prime-harens.is_prime(9) is False
  assert prime-harens.is_prime(-1) is False
  
  assert prime-harens.is_prime(2) is True
  assert prime-harens.is_prime(29) is True
  assert prime-harens.is_prime(31) is True
  
def smaller_prime_check(num):
  assert prime-harens.smaller_prime(0) is False
  assert prime-harens.smaller_prime(9) is False
  assert prime-harens.smaller_prime(-1) is False
  
  assert prime-harens.smaller_prime(2) is True
  assert prime-harens.smaller_prime(29) is True
  assert prime-harens.smaller_prime(31) is True
