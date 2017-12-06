import re

a = 'Csdlf9823sd28329sxd332'

r = re.findall('\d',a)
print(r) # 输出:['9', '8', '2', '3', '2', '8', '3', '2', '9', '3', '3', '2']

r = re.findall('\D',a)
print(r) # 输出:['C', 's', 'd', 'l', 'f', 's', 'd', 's', 'x', 'd']


#字符集
s = 'abc,acc,adc,aec,afc,ahc'
r = re.findall('a[cf]c',s)
print(r)  # 输出:['acc', 'afc']

r = re.findall('a[^cf]c',s)
print(r)  # 输出: ['abc', 'adc', 'aec', 'ahc']

r = re.findall('a[c-f]c',s)
print(r)  # 输出: ['acc', 'adc', 'aec', 'afc']


#概括字符集
a = 'python1111java678php'

## \d  [0-9]
r = re.findall('\d',a)
print(r)  # 输出: ['1', '1', '1', '1', '6', '7', '8']

r = re.findall('[0-9]',a)
print(r)  # 输出: ['1', '1', '1', '1', '6', '7', '8']

## \D  [^0-9]
r = re.findall('\D',a)
print(r)  # 输出: ['p', 'y', 't', 'h', 'o', 'n', 'j', 'a', 'v', 'a', 'p', 'h', 'p']

r = re.findall('[^0-9]',a)
print(r)  # 输出: ['p', 'y', 't', 'h', 'o', 'n', 'j', 'a', 'v', 'a', 'p', 'h', 'p']

## \w  [A-Za-z0-9_] #单词字符(数字+字母)
r = re.findall('\w',a)
print(r)  # 输出: ['p', 'y', 't', 'h', 'o', 'n', '1', '1', '1', '1', 'j', 'a', 'v', 'a', '6', '7', '8', 'p', 'h', 'p']


r = re.findall('[A-Za-z0-9_]',a)
print(r)  # 输出: ['p', 'y', 't', 'h', 'o', 'n', '1', '1', '1', '1', 'j', 'a', 'v', 'a', '6', '7', '8', 'p', 'h', 'p']


a = 'Csdlf9823sd2832&9sxd332'

## \W  等同于s(等&会取不出来)   #非\w字符集 非单词字符 包括 空格 回车 \r \n \t  &等
r = re.findall('\W',a)
print(r)  # 输出:['&']

r = re.findall('\s',a)
print(r)  # 输出:[]




