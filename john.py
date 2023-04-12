from dataclasses import dataclass

@dataclass
class Employee:
    name: str
    dept: str
    salary: str

john = Employee('john','Lab',10000)
john.dept
john.salary    