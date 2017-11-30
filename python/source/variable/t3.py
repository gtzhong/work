c=1

def fun1():
    c=2
    def fun2():
        c=3
        print(c)
    fun2()

# 链式 作用域链
fun1()