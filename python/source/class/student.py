class Student():
    name =''
    age = 0

    def __init__(self, name,age):
        self.name = name
        self.age=age
        print('loading')

    def print_file(self):
        print('name:'+self.name)
        print('age:'+str(self.age))

    def do_homework(self):
        print('homework')

#student = Student()
#student.print_file()

