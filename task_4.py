class EmployeeSalary:
    hourly_payment = 400  # почасовая оплата — переменная класса

    def __init__(self, name, hours=None, rest_days=0, email=None):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email

    @classmethod
    def get_hours(cls, name, hours=None, rest_days=0, email=None):
        # если hours не указаны, рассчитываем по формуле
        if hours is None:
            hours = (7 - rest_days) * 8
        # возвращаем новый экземпляр класса
        return cls(name, hours, rest_days, email)

    @classmethod
    def get_email(cls, name, hours=None, rest_days=0, email=None):
        # если email не указан, генерируем по шаблону
        if email is None:
            email = f"{name}@email.com"
        # возвращаем новый экземпляр класса
        return cls(name, hours, rest_days, email)

    @classmethod
    def set_hourly_payment(cls, new_payment):
        cls.hourly_payment = new_payment

    def salary(self):
        # считаем зарплату по формуле
        return self.hours * self.hourly_payment


# Пример использования:

# Создаём сотрудника с известными часами
emp1 = EmployeeSalary.get_hours('Ivan', hours=40, rest_days=2)
print(emp1.name, emp1.hours, emp1.rest_days, emp1.email)  # Ivan 40 2 None
print(emp1.salary())  # 40 * 400 = 16000

# Создаём сотрудника без указания часов, часы считаются по rest_days
emp2 = EmployeeSalary.get_hours('Petr', hours=None, rest_days=1)
print(emp2.name, emp2.hours, emp2.rest_days, emp2.email)  # Petr 48 1 None
print(emp2.salary())  # 48 * 400 = 19200

# Создаём сотрудника без email — он будет сгенерирован
emp3 = EmployeeSalary.get_email('Maria', hours=35, rest_days=2, email=None)
print(emp3.name, emp3.hours, emp3.rest_days, emp3.email)  # Maria 35 2 Maria@email.com
print(emp3.salary())  # 35 * 400 = 14000

# Изменяем почасовую оплату
EmployeeSalary.set_hourly_payment(500)
print(emp1.salary())  # 40 * 500 = 20000
