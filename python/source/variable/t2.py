# c=10 #全避变量

def demo():
    c=50 #局部变量
    # a =''
    # 块级作用域
    for i in range(0,9):
        a='a'
        c+=1
    print(c)
    print(a)

demo()