class Student():
    sum=0


    def __init__(self,age):
        self.__class__.sum +=1   # 方法1  使sum累加
        print(self.__class__.sum)


    #实例方法
    def do_homework(self):
        print('homework')

    @classmethod
    def plus_sum(cls):
        cls.sum +=1 # 方法2  使sum累加
        print(cls.sum)


student1 = Student(1)
student1.plus_sum()  # 使用实例化对象访问类访问,不建议这样使用!!
Student.plus_sum()# 使用类名访问类方法

student2 = Student(1)
student2.plus_sum()
Student.plus_sum()