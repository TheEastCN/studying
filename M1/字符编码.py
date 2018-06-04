# -*- coding:utf-8 -*-

s = '路飞学城'
print(type(s))

s1 =s.encode('utf-8')
print(type(s1))

# - 将字符串转换成utf - 8的字符编码的字节，再将转换的字节重新转换为utf - 8的字符编码的字符串
#
# - 将字符串转换成gbk的字符编码的字节，再将转换的字节重新转换为utf - 8的字符编码的字符串
#
s2 = '中二'
s3 = s2.encode('utf-8').decode('utf-8')

s4 = s2.encode('gbk').decode('gbk').encode('utf-8').decode('utf-8')
print(s4)