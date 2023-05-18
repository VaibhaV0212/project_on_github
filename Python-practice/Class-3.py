class Employee:

    num_of_emp = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay) -> None:
        self.first = first
        self.last = last
        self.email = self.first + '.' + self.last + '@email.com'
        self.pay = pay

        Employee.num_of_emp += 1

    def fullname(self):
        return f"{self.first} {self.last}"
    
    def apply_raise(self, pay):
        return self.pay * self.raise_amt
    
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount
    
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

# e1 = Employee('Vaibhav','Tomar', 50000) 
# e2 = Employee('Nidhi','Sharma', 57890) 

# print(Employee.raise_amt)
# print(e1.raise_amt)
# print(e2.raise_amt)

# Employee.set_raise_amt(3.2)
# print(Employee.raise_amt)
# print(e1.raise_amt)
# print(e2.raise_amt)

emp = "Vaibhav-Tomar-99000"

e1 = Employee.from_string(emp)
print(e1.email)
print(e1.pay)