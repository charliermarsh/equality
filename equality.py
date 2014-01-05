"""
    O(1) information test for equality of two bitstrings from Interactive Information Complexity [Braverman '11].
"""

import numpy as np
from random import randint
import unittest


def is_invertible_F2(a):
    """
        Determine invertibility by Gaussian elimination.
        Via http://stackoverflow.com/questions/16254654/test-if-matrix-is-invertible-over-finite-field.
    """
    a = np.array(a, dtype=np.bool_)
    n = a.shape[0]
    for i in range(n):
        pivots = np.where(a[i:, i])[0]
        if len(pivots) == 0:
            return False

        # swap pivot
        piv = i + pivots[0]
        row = a[piv, i:].copy()
        a[piv, i:] = a[i, i:]
        a[i, i:] = row

        # eliminate
        a[i + 1:, i:] -= a[i + 1:, i, None] * row[None, :]

    return True


def generate_A(n):
    """Returns a non-singular n-by-n matrix on F_2."""
    while True:
        a = np.random.randint(0, high=2, size=(n, n))
        if is_invertible_F2(a):
            continue
        return a


class Player(object):

    def __init__(self, data):
        self.data = data
        self.n = len(data)

    def multiply(self, scale):
        return np.dot(np.array(self.data), scale)

    def isEqual(self, scale, b):
        return self.multiply(scale) == b


def equality(alice, bob):
    """Returns True if Alice and Bob have equal bitstrings."""
    A = generate_A(alice.n)

    # Check equality of each row
    for row in A:
        if not alice.isEqual(row, bob.multiply(row)):
            return False

    return True


def random_bitstring(n):
    """Generate a random bitstring on n bits."""
    return [randint(0, 1) for i in range(n)]


class TestEquality(unittest.TestCase):

    def test_equal(self):
        for t in range(100):
            bitstring = random_bitstring(100)
            alice = Player(bitstring)
            bob = Player(bitstring)
            self.assertTrue(equality(alice, bob))

    def test_inequality(self):
        for t in range(100):
            # Assign Alice's data
            bitstring = random_bitstring(100)
            alice = Player(bitstring)

            # Ensure Bob has different data
            bitstring = random_bitstring(100)
            while alice.data == bitstring:
                bitstring = random_bitstring(100)
            else:
                bob = Player(bitstring)

            self.assertTrue(not equality(alice, bob))

if __name__ == '__main__':
    unittest.main()
