import re

s = 'life is short,i use python'

#None

r = re.search('life.*python',s)
print(r.group())   # 输出: life is short,i use python

r = re.search('life(.*)python',s)
print(r.group(0))  # 输出: life is short,i use python

print(r.group(1))  # 输出:  is short,i use

r = re.findall('life(.*)python',s)
print(r)  # 输出: [' is short,i use ']


s = 'life is short,i use python, i love python'

r= re.search('life(.*)python(.*)python',s)

##方法1 
print(r.group(0)) # 输出: life is short,i use python, i love python
print(r.group(1)) # 输出:  is short,i use
print(r.group(2)) # 输出: , i love

##方法2
print(r.group(0,1,2))   # 输出: ('life is short,i use python, i love python', ' is short,i use ', ', i love ')


print(r.groups())   # 输出: (' is short,i use ', ', i love ')

