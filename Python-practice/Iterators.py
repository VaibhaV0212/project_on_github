# Iterators - Is an object that contains countable number of values, 
# which consits of methos "iter()" which return iterator object  & "next() to print it."

my_list = [3,4,5,6,7]

my_iter = iter(my_list)
# print(next(my_iter))


'''
Difference between "yeild" and "return" is, when using a return inside a function, once function is over,
 no memory is saved and we are out of the fucntion but yield remembers it position and value of last used.
'''


