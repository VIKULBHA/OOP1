class Student:
    def __init__(self, name, number):
        self.name = name
        self.number = number


class Department:
    def __init__(self, name, code):
        self.name = name
        self.code = code


class Course:
    def __init__(self, name, course_code, department, ):
        print("Initiating", name, course_code, "Department", vars(department))
        self.name = name
        self.course_code = course_code
        self.department = department