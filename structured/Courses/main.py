from student import Student
from student import Course
from student import Department

student_1 = Student("Vikul", 111)
student_2 = Student("Emerson",222)
student_1.enrol(Course)
student_2.enrol("Python")
student_2.enrol("Devops")
print(vars(student_1))
print(vars(student_2))
department_1 = Department("IT", 333)
c1 = Course("Dev awesome course", 1, 35, department_1)
c2 = Course("Ops awesome course", 2, 35, department_1)
cr1 = c1.add_running(2020)
student_1.enrol(cr1)
print("Running", vars(cr1))