#import Human   #使用这个引入报错  TypeError: module.__init__() takes at most 2 arguments (3 given)
from Human import Human

class Student(Human):

    def __init__(self,school,name,age):
        self.school = school
        #Human.__init__(self,name,age)  #第一种方法,相当于是一个普通的方法,所以要带上self   2.因为是类访问的
        super(Student,self).__init__(name,age)  #第二种方法,调用父类
       
    
    def do_homework(self):
        super(Student,self).do_homework()
        print('xxxx')
    
student1 = Student('人民路小学','张三',28)
student1.do_homework()

print(student1.name)  #输出:张三
print(student1.age)  #输出:28
print(student1.school)  #输出:人民路小学