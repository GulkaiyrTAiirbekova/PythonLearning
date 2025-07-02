class Worker:
    def __init__(self, first_name: str, salary: float):  # исправлено __init__
        self.first_name = first_name
        self.salary = salary

    def work(self):
        return f"{self.first_name} работает в нашей компании"


class Manager(Worker):
    def __init__(self, first_name: str, salary: float, position: str):
        super().__init__(first_name, salary)
        self.position = position

    def work(self):
        base_work = super().work()
        return f"{base_work} — как {self.position} и получает зарплату ${self.salary} в год."



class Developer(Worker):
    def __init__(self, first_name: str, salary: float, position: str, language: str):
        super().__init__(first_name, salary)
        self.position = position
        self.language = language

    def work(self):
        base_work = super().work()
        return f"{base_work} — как {self.position}, пишет код на {self.language} и получает зарплату ${self.salary} в год."


# Пример использования:
dev = Developer("Gulkaiyr", 500000, "Backend", "Python и Java")
res = dev.work()
print(res)