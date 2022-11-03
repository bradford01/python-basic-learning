class Employee:
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def full_name(self):
        return f" {self.first} {self.last}"

    def appy_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    # @classmethod
    # def set_raise_amt(cls, amount):
    #     cls.raise_amt = amount


class Developers(Employee):
    raise_amt = 2.04

    def __init__(self,first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Managers(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay, )
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print("-->", emp.full_name())




emp_1 = Employee("SYLVESTER", "IKE-AGBO", 5000)
emp_2 = Employee("Daniella", "IKE-AGBO", 40000)
dev_1 = Developers("jESSICA", "IKE-AGBO", 30000, "Java")
dev_2 = Developers("mark", "onaeko", 400, "Python")
mg_1 = Managers("sly", "ike", 2000, [dev_1])
print(mg_1.employees)
print(mg_1.add_emp(dev_2))
print(mg_1.print_emps())
print(emp_1.pay)
emp_1.appy_raise()
print(emp_1.pay)
print(dev_1.prog_lang)

dictionary = {
    "child1": {
        "name":"sly",
        "course":"ice"

    },
    "child2": {
        "name": "daniella",
        "course": "Pharmacist",
        "age": 60

    }
}

