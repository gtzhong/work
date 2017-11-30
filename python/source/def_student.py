def print_student_files(name,gender='男',age=18,college='人民路小学'):
    print('我叫'+name)
    print('我今年'+str(age)+'岁')
    print('我是'+gender+'生')
    print('我在'+college+'上学')

print_student_files('张三','男',18,'人民路小学')
print('~~~~~~~~~~~~~~~~~~~~~~')

print_student_files('张三')
print('~~~~~~~~~~~~~~~~~~~~~~')

print_student_files('百敢当')
print('~~~~~~~~~~~~~~~~~~~~~~')

print_student_files('王四','女',16)
print('~~~~~~~~~~~~~~~~~~~~~~')


print_student_files('蛋蛋',age=20)
print('~~~~~~~~~~~~~~~~~~~~~~')


print_student_files('蛋蛋',age=20,college='青山',gender='人妖')
print('~~~~~~~~~~~~~~~~~~~~~~')