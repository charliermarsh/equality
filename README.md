equality
===

Demonstration of a zero-error, O(1) information complexity algorithm for equality found in Interactive Information Complexity [[Braverman11](http://eccc.hpi-web.de/report/2011/123/)].

# The Algorithm

A basic outline of the procedure is as follows:

1. Alice and Bob have private bit strings x and y, respectively.
2. A non-singular n-by-n matrix A over the finite field F_2 is randomly sampled (with public randomness).
3. For each row A_i in A:
    1. Alice sends A_i • x to Bob.
    2. If A_i • x != A_i • y, Bob returns `False`.
4. Bob returns `True`.

At termination, we have two possible outcomes:

- If A_i • x != A_i • y for any i, then x != y.
- If A_i • x == A_i • y for all i, then Ax = Ay. Further, as A is non-singular, this implies that x = y.

# Running

To run, initiate the test suite with `python equality.py`. Both known-equal strings and known-unequal strings will be tested.

# Appendix

The proof of the procedure's O(1) information complexity can be found in the [linked paper](http://eccc.hpi-web.de/report/2011/123/) mentioned above.
