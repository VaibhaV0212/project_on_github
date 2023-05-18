class Student:
    school = '_VOIS'

    def __init__(self,m1,m2,m3) -> None:
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    
    def avg(self):
        return (self.m1 + self.m2 + self.m3)//2

    # Getters
    def get_m1(self):
        return self.m1
    
    # Setters
    def set_m1(self, value):
        self.m1 = value

    @classmethod
    def info(cls):
        return cls.school

s1 = Student(21,32,45)
result = s1.avg()
print(f'Result is {result} and school is {s1.info()} and also {Student.school}')