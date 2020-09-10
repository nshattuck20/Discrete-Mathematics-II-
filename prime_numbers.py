


def find_primes(start, end):
    '''A simple function that returns all of the prime
    numbers within a given range.
    '''
    for i in range(start, end):
        for j in range(2, i):
            if i % j == 0:
                # composite
                break
        else:
            print(i)

# this is also bugged
print(find_primes(5, 25))


# numbers = [2, 3, 4, 5, 6, 7]
# primes = []
# for i in range(min(numbers), max(numbers)):
'''
This does not work...yet. 
'''
#     for j in range(2, i):
#         if (i % j == 0):
#             break
#        else:
#            primes.append(i)
#     return(primes)
