class Student():
    name ='default'

    def __init__(self,name,age):
        self.name = name

    @classmethod
    def plus_sum(cls):
         print(Student.name)
       # print(self.name)  #不能获取实例变量的值

    @staticmethod
    def add(x,y):
        print(Student.name) #获取类变量的值
        #print(self.name)  #不能获取实例变量的值
    
student1 = Student('cmk',18)
student1.add(1,2)    # 使用实例化对象访问类访问,不建议这样使用!!
Student.add(1,2)    # 使用类名访问类方法

student1.plus_sum()
Student.plus_sum()