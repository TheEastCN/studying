#_*_coding:utf-8_*_

# import os
#
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath("将进酒.txt")))
# print(BASE_DIR)

import configparser
# config = configparser.ConfigParser()
#
# config.read("1.cfg")
# a = config.sections()
# print(a,type(a))
# b = config["client"]
#
# print(b["port"])
#
# op = config.options("client")
# print(op)
#
# item_list = config.items("mysqld")
# print(item_list)
#
# val1 = config.get("mysqld",'socket')
# print(val1)
# sec = config.remove_section('mycnf')
# config.write(open('1.cfg','w'))
#
#
# # sec1 = config.has_section('wupeiqi')
# #sec2 = config.add_section('wyd')
# # config.write(open('1.cfg','w'))
# # config.remove_section('wyd')
#
# config.set('wyd','IP',"127.0.1.1")
# config.write(open('1.cfg','w'))

config = configparser.ConfigParser()

config.read('1.cfg')

op = config.sections()
print(op)

src = config.set('mysqld','default-time-zone','+00:00')
config.write(open('1.cfg','w'))

#explicit_defaults_for_timestamp = true
config.remove_option('mysqld','explicit_defaults_for_timestamp')
config.write(open('1.cfg','w'))

config.set('DEFAULT','character-set-server', 'utf8')
config.write(open('1.cfg','w'))