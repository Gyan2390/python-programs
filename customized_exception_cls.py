
class SalaryNotInRangeError(Exception):

    def __init__(self, salary, message="Salary is not in (5000, 15000)range"):
        self.salary=salary
        self.message=message
        super().__init__(self.message)

salary = int(input("salary amount: "))
if not 5000<salary<15000:
    raise SalaryNotInRangeError(salary,"salary error")