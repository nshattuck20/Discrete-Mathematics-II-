'''
A simple peice of code searching for an item in 
a sequence using a while loop. 
'''

my_list = [7,6,1,3]

i = 0 
x = 1

while (my_list[i] != x and i < len(my_list)): 
	i+=1 

if (my_list[i] == x): 
	print("Found at index", i)
else:
	print("Not found.")
