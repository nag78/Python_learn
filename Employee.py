class Employee ():
    """Модель простого работника"""
    def __init__(self,first,last):
        self.first = first
        self.last = last
        self.salary = 35000

    def give_raise(self,salary_raise = 5000):
        """Годовая прибавка. Возвращает оклад после прибавки"""
        self.salary_raise = salary_raise
        self.salary += self.salary_raise
        return self.salary



my_employee = Employee('staff','staffovich')
print(my_employee.give_raise())
