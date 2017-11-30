
def demo(param1,*param,param2):
    print(param1) # a
    print(param) # (1, 2, 3)
    print(param2) # paramxxxxx


demo('a',1,2,3,param2='paramxxxxx')

