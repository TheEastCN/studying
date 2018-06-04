# -*- coding:utf-8 -*-

def md5(str):
    import hashlib
    hex_md5 = hashlib.md5()
    hex_md5.update(str)
    return  hex_md5.hexdigest()

print(md5(bytes('aaa',encoding='utf-8')))