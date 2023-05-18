# def greet(name, loc):
#     print(f"""
#     Hi hello how are you {name}? 
#     Where are you from, {loc}!
#     """)

# greet('vaibhav', 'bhopal')


import math

def paint(h, w, cov=5):
    cans = (h * w)/cov
    print('cans=>',math.ceil(cans))

height = eval(input('Enter height='))
width = eval(input('Enter width='))

paint(h=height, w=width)

a = [1,2,3]
print('sum--->',sum(a))