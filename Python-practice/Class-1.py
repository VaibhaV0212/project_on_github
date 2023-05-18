'''
Class:- Suppose if I talk about Human beings, you and me, we share some common set of properties like name, gender, occupation.
and does some common activites like eating, walking, speaking. So the first is called "Attributes" and the
second is called "methods".
'''

'''
Object:- It is a specific instance, and when we talk about instance, the behaviour varies.
e.g.- You and me are the instance of the same Human class but you are referenced as "Saurab" and 
I am referenced by "VaibhaV".
'''

class Human:
    # Class Variable
    car = "BMW"

    def __init__(self, name, occupation) -> None:
        # instance varibale
        self.name = name
        self.occupation = occupation

    def speak(self):
        print(f"{self.name} loves to speak!! and drives {self.car}")

h1 = Human('Vaibhav', 'Developer')
h1.speak()
print("Modifying class variable--")
Human.car = "Audi"
print("Modifying instance variable--")
h1.name = "Nidhi"
h1.speak()