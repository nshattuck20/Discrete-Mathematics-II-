

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
	return(x)


gcd = euclids_algorithm(54, 156) 
print("The greatest common divisor is" , gcd) 