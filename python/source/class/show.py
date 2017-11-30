from student import Student

#实例化
student = Student('王八',20)
#student.__init__('张三',11)  #在外部可以调用__init__()
student.print_file()
print(student.name)
print(student.age)
