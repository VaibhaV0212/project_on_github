import csv
from datetime import date

dt = date.today()
dt = dt.strftime("%d/%m/%Y")
filename = 'test.csv'
exp = []
stopped = True

with open(filename, 'a', newline='') as f:
    csvwriter = csv.writer(f)
    while stopped:
        xp = eval(input('Enter the expense (type 0 to exit) = '))
        if xp == 0:
            stopped = False
            print('Bye!!')
        else:        
            
            csvwriter.writerow([dt, xp])
            exp.append(xp)
            print()

print('Done!!')
print('Your Expenses are = ', exp)
print('Your total is = ', sum(exp))
