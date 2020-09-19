'''
Algorithm to find the largest integer represented by k digits base b.
'''
import math

def findNumOfDigits(n, base):
    dig = (math.ceil(math.log(n) / math.log(base)) + 1)
    print("The number of number {} in base {} is {}".format(n, base, dig))



n = 146
base = 7

findNumOfDigits(n, base)

# def base_b_expansion(n, b):
#     # Output: Base b expansion of n. Base b digits are output in reverse order
#     # I am not exactly sure how this is supposed to be working.
#     x = n
#     k = 0
#     a = []
#     i = len(str(n))
#
#     while x != 0:
#         a.append(x % b)
#         x = x / b
#         k += 1
#     return a
#
# print(base_b_expansion(15,2))
