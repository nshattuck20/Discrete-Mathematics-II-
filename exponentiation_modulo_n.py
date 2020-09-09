from math import modf




def exponentiation_mod_n(n):
    p = n
    for i in range(158):
        p = (13 * p) * modf(71)
        return (p)


print(exponentiation_mod_n(13))