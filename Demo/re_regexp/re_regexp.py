

import re


# 提取出python
key = 'javapythonc++php'
print(re.findall('python', key))  # ['python']
print(re.findall('python', key)[0])  # python

# 提取出hello world
key = '<html><h1>hello world<h1></html>'
print(re.findall('<h1>(.*)<h1>', key))  # ['hello world']
print(re.findall('<h1>(.*)<h1>', key)[0])  # hello world

# 提取出数字2
string = '我有2台手机和1台车'
print(re.findall('\d+', string))  # 数字：['2', '1']
print(re.findall('\D+', string))  # 非数字：['我有', '台手机和', '台车']

# 提取出http://和https://
key = 'http://www.baidu.com and https://boob.com'
print(re.findall('http?://', key))  # ['http://']  这是为什么？？
print(re.findall('https?://', key))  # ['http://', 'https://']

# 提取出 hello
key = 'lalala<hTml>hello</HtMl>hahh'
print(re.findall('<[Hh][Tt][mM][lL]>(.*)</[Hh][Tt][mM][lL]>', key))  # ['hello']

# 提取出hit.
key = 'bobo@hit.edu.com'
print(re.findall('h.*?\.', key))  # ['hit.']

# 匹配sas和saas
key = 'saas and sas and saaas'
print(re.findall('sa{1,2}s', key))  #{m,n}:表示m-n次，['saas', 'sas']

# 占位符提取 2023
key = '"processId":20230114,"name":"alex"'
print(re.findall('"processId":(.*?)....,"',key))