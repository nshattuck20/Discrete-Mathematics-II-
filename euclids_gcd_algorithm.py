import timeit
code_to_test = """
def euclids_algorithm(x, y):

	if(y < x):
		temp = y 
		y = x 
		x = temp
	r = y % x

	while (r != 0):
		y = x
		x = r 
		r = y % x
	return(x,)
"""
more_code_to_test = """
def recursive_euclid(x, y):

	if y == 0:
		return x
	else:
		return recursive_euclid(y, (x % y))

"""
# gcd = euclids_algorithm(54, 156)
# rgcd = recursive_euclid(54, 156)

time_elapsed_for_recursive_euclid = timeit.timeit(more_code_to_test, number = 100) / 100
time_elapsed_for_euclid = timeit.timeit(code_to_test, number = 100) / 100
print("Recursive Euclid ran: ")
print(time_elapsed_for_recursive_euclid)

print(" Euclid ran: ")
print(time_elapsed_for_euclid)

# print(gcd)
# print(rgcd)


