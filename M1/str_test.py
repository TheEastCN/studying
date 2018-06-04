# -*- coding:utf-8 -*-

str = 'abcdededededefg'

#根据索引获取数据，0查看第一个字符，-1 查看从右开始的第一个字符
print(str[0])
print(str[-1])

#字符串截取/切片
print(str[2:]) # cdededededefg ,从索引为2的字符开始截取一直到最后
print(str[1:3]) # bc ,从索引为1的字符开始截取到3-1位置，不包含3所在位置字符
print(str[:3]) # abc ,从头开始截取到3-1位置，不包含3所在位置字符
print(str[0:6:2]) # ace ,从索引为0的字符开始截取到6-1位置，不包含6所在位置字符,切片步长为2，每两个字符截取一个
print(str[::-1]) # gfedededededcba，字符串倒叙输出




#S.capitalize()- > str  返回一个第一个字符大写的字符串
print(str.capitalize()) #返回：Abcdededededefg

# S.center(width[, fillchar]) 以字符串为中心，左右补充字符 ，width = 设置的宽度，fillchar=补位字符
print(str.center(20,'-')) #返回:"--abcdededededefg---"

#count  S.count(sub[, start[, end]]) -> int 统计字符串S中的某字符或字符串出现的次数，可进行切片查询
print('count',str.count('de'))
print('count',str.count('de',3,6))

# encode  S.encode(encoding='utf-8', errors='strict') -> bytes 使用encoding后定义编码对字符串进行转码
print(str.encode('GBK'))

# endswith  S.endswith(suffix[, start[, end]]) -> bool 判断后缀是否为指定的字符串，如果是返回True,否则返回Flase ,可进行截位查询
print('endswith->',str.endswith('g'))

# expandtabs  S.expandtabs(tabsize=8) -> str 将字符串中的制表符改为空格，tabsize进行设置替换的空格数量，默认为8
print('expandtabs','ab\ta'.expandtabs(10))

# find/rfind查找S.find(sub[, start[, end]]) -> int 可以搜索字符串，根据start ----end 切片范围内搜索
print(str.find('f'))
print(str.find('de', 6, 9))
print(str.rfind('de')) #从右开始进行查找

 # format 对字符串进行格式化
print('My name is {name},age is {age}'.format(name='wyd',age=18))

 # format_map
dict = {'Foo': 54.23345}
fmt = "Foo = {Foo:.3f}"
result = fmt.format_map(dict)
print(result)

#  index 、rindex S.index(sub[, start[, end]]) -> int 使用index获取字符所在索引
print(str.index('c'))
print(str.rindex('c'))

# isalnum S.isalnum() -> bool  判断字符串中是否全为字母和数字，是则返回True
print(str.isalnum())

# isalpha  S.isalpha() -> bool 判断字符串中是否全为字母，是则返回True
print(str.isalpha())

# isdecimal  S.isdecimal() -> bool  判断字符串中是否全为数字，是则返回True
print('isdecimal ->','1234'.isdecimal())

# isdigit S.isdigit() -> bool  判断字符串中是否全为数字，是则返回True
print('isdigit ->','4445a'.isdigit())
# isidentifier  S.isidentifier() -> bool
print('isidentifier','_def'.isidentifier())

# islower 判断字符串是否全部为小写，是则返回True
print(str.islower())
# isupper 判断字符串是否全部为大写，是则返回True
print(str.isupper())
# isnumeric 字符串中如果为纯数字 返回True
s = '123'
print(s.isnumeric()) #true
print(str.isnumeric()) #Flase

# isprintable 判断字符串的字符是否可全部打印，是则返回True
print('isprintable',str.isprintable())
# isspace 判断字符串是否全为空格，如果是怎返回True
print('isspace','   '.isspace())
# istitle 判断字符串中所有的单词拼写首字母是否为大写，且其他字母为小写，如果是怎返回True
print('Abcd'.istitle())

#S.join(iterable)- > str  将序列中的元素以指定的字符连接生成一个新的字符串
print('b'.join(['a','c'])) #返回一个字符串 abcebcegbs

# ljust/rjust 返回一个原字符串左对齐,并使用空格填充至指定长度的新字符串。如果指定的长度小于原字符串的长度则返回原字符串。
print('ljust',str.ljust(50)) #右补空格
print('rjust',str.rjust(50)) #左补空格

#lower 返回一个字母全部小写的字符串
print('lower','A1AAAA'.lower())


# strip 、lstrip、rstrip 可删除字符串开头和结尾的空格，中间内容不会删除,
f = ' jj ll '
print(f.strip())
print(f.rstrip())
print(f.lstrip())

# maketrans  str.maketrans(x[, y[, z]]) -> dict 两组长度相同的字符串生成字典对应关系，
f = str.maketrans('abcdef','123456')
print(str.maketrans('abcdef','123456'))

#translate 返回字符串，根据参数，将字符串惊醒转换
print(str.translate(f))

#partition 、rpartition 将字符串进行分组，按参数字符进行，分成三部分
print(str.partition('de')) #('abc', 'de', 'dedededefg')
print(str.rpartition('de')) #('abcdededede', 'de', 'fg')

#替换S.replace(old, new[, count]) -> str  old=被修改的字符、字符串 new=修改的字符、字符串， count=被替换的次数
print(str.replace('d','D')) #返回：'abcDeDeDeDeDefg'
print(str.replace('d','D',2)) #返回: 'abcDeDedededefg' 设置了count参数 只修改了两个


#获取字符串的长度
print(len(str))

# rsplit / split  S.split(sep=None, maxsplit=-1) -> list of strings 以字符‘b’为分割符号，生成列表
a = 'abcebcegbs'
b = a.split('b')
print(b) # 返回列表:['a', 'ce', 'ceg', 's'] ,以字符‘b’为分割符号，生成列表
print('rsplit',str.rsplit('de'))

# splitlines 按照行('\r', '\r\n', \n')分隔，返回一个包含各行作为元素的列表，如果参数 keepends 为 False，不包含换行符，
# 如果为 True，则保留换行符。
f1 = 'ab \n\c abcd\t\c'
print(f1.splitlines()) # ['ab ', '\\c abcd\t\\c']
print(f1.splitlines(True)) #['ab \n', '\\c abcd\t\\c']

#startswith 用于检查字符串是否是以指定子字符串开头，如果是则返回 True
print(str.startswith('abc')) #True

# swapcase 对字符创中的字母进行大小写转换
print('aBcdE'.swapcase()) #AbCDe

# title 将自妇产中的首字母改为大写,其他字母小写
print('bvcdE'.title())

# upper 将字符串中的字母全部转换为大写
print(str.upper()) #ABCDEDEDEDEDEFG

#zfill 返回指定长度的字符串，原字符串右对齐，前面填充0。
print(str.zfill(20))