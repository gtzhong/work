from student import Student

#实例化
student1 = Student('王八',20)
print(student1.name)
print(student1.__dict__) #输出: {'name': '王八', 'age': 20}
print(Student.__dict__)

#输出
"""
{'__module__': 'student', 'name': '', 'age': 0, '__init__': <function Student.__init__ at 0x038D5348>, 'print_file': <function Student.print_file at 0x038D5390>, 'do_homework': <function Student.do_homework at 0x038D53D8>, '__dict__': <attribute '__dict__' of 'Student' objects>, '__weakref__': <attribute '__weakref__' of 'Student' objects>, '__doc__': None}

"""

