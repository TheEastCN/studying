# -*- coding:utf-8 -*-

import hashlib
from core import getter


def hash_md5(str):

    md5 = hashlib.md5()
    md5.update(bytes(str, encoding='utf-8'))

    return md5.hexdigest()


def diff_md5(account, passwd,file_name):
    md5_new = hash_md5(passwd)
    data = getter.json_data_get(file_name)
    if data[account]['password'] == md5_new:
        return True
    else:
        return  False

