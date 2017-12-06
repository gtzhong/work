import re
a = 'C|c++|php|java|Python|Javascript'
print(a.index('Python')>-1)  # 输出:True

print('Python' in a ) # 输出:True


res =re.findall('Python',a)
print(res)  # 输出 : 'Python']