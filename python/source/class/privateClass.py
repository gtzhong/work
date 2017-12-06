class Student():
    sum =0
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.__score =0
        self.__class__.sum += 1 # 

student1 = Student('张三',18)
student2 = Student('王五',20)

student1.__score = -1    #没有报错,因为是python新添加的特例,动态添加变量,相当于新添加一个实例变量
print(student1.__score)  # 输出 -1

#print(student2.__score)  # 输出 报错

print(student1.__dict__)  #输出  {'name': '张三', 'age': 18, '_Student__score': 0, '__score': -1}    _Student__score为真正的私有变量,以类名拼接     __score 为外部定义的

print(student2.__dict__)  #输出  {'name': '王五', 'age': 20, '_Student__score': 0}  