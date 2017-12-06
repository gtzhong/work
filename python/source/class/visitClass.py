class Student():
    sum1 =10
    def __init__(self,name,age):
        print(Student.sum1) #内部访问变量方法1  输出:10
        print(self.__class__.sum1) #内部访问变量方法2   输出:10

student1 = Student('李四',18)

print(Student.sum1) #外部访问类的变量   输出:10