exp = -1
total = 0
maxexp = 0
minexp = 0
exp_list = []

while exp!=0:
    exp = eval(input('Enter the expense = '))
    total = total + exp
    exp_list = str(exp_list.extend(total))
    if exp>maxexp:
        maxexp = exp
    

print('Total =',total)
print('Maxexp =',maxexp)
print('Minexp =',minexp)
print('exp_list = ', exp_list)
