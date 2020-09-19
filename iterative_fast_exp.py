"""
A more efficient approach to fast exponentiation using an iterative algorithm.
Coming soon, recursion(recursion(recursion(recursion(recursion()))))
Input: Positive integers x and y.
Output: xy

p := 1     // p holds the partial result.
s := x     // s holds the current x^2^^j.
r := y     // r is used to compute the binary expansion of y

While ( r > 0 )
      If ( r mod 2 = 1 )
            p := p·s
      s := s·s
      r := r div 2
End-while

Return(p)
"""


def fast_exp(x, y):
    p = 1  # p holds the partial result
    s = x  # s holds the current x^^2^j
    r = y

    while r > 0:
        if r % 2 == 1:
            p = p * s
        s = s * s
        r = r // 2
    return p


def modular_exp(x, y, j):
    p = 1  # p holds the partial result
    s = x  # s holds the current x^^2^j
    r = y
    n = j  # n holds the current successive square.
    while r > 0:
        if r % 2 == 1:
            p = p * s % n
        s = s * s % n
        r = r // 2
    return p


fast = fast_exp(7, 11)
print(fast)

mod = modular_exp(7, 11, 11)
print(mod)
