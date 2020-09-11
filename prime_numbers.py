

#
# def find_primes(start, end):
#     '''A simple function that returns all of the prime
#     numbers within a given range.
#     '''
#     for i in range(start, end):
#         for j in range(2, i):
#             if i % j == 0:
#                 # composite
#                 break
#         else:
#             print(i)
#
# # this is also bugged
# print(find_primes(5, 25))


numbers_list = [2, 3, 4, 5, 6, 7, 8, 9, 10]

def find_primes_in_list(numbers):
    '''
    This method finds all of the prime integers in a list, and adds each
    prime integer to a list.
    '''
    primes = []
    start = 0
    end = len(numbers)

    for i in range(start, end):
        for j in range (2, numbers[i]):
            if numbers[i] % j == 0:
                break
        else:
            # number is prime
            primes.append(numbers[i])
    return (primes)

print(find_primes_in_list(numbers_list))

