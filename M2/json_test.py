# -*- coding:utf-8 -*-

import json,re,time,hashlib

def md5(str):
    import hashlib
    has_mad = hashlib.md5()
    has_mad.update(str)
    return  has_mad.hexdigest()

input_name = input('username:').strip()
input_pw = input('passwd:').strip()

file_name = input_name + '.json'
file_json2 = open(file_name,'r+',encoding='utf-8')
json_data = json.load(file_json2)
file_json2.close()

json_data['password'] = md5(bytes(input_pw,encoding='utf-8'))
print(json_data)

file_json1 = open(file_name,'w',encoding='utf-8')
json.dump(json_data,file_json1)
file_json1.close()
#'password': 'abc'
if input_pw == json_data['password']:
    print('login success')
time_local = time.strftime('%Y-%m-%d',time.localtime())
if time_local < json_data['expire_date']:
    print('time_local:%s expire_date:%s'%(time_local,json_data['expire_date']))



