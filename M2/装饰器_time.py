# -*- coding:utf-8 -*-

import time
# 一：编写3个函数，每个函数执行的时间是不一样的，
#
# 提示：可以使用time.sleep(2)，让程序sleep 2s或更多，
# 二：编写装饰器，为每个函数加上统计运行时间的功能
#
# 提示：在函数开始执行时加上start=time.time()就可纪录当前执行的时间戳，函数执行结束后在time.time() - start就可以拿到执行所用时间
# 三：编写装饰器，为函数加上认证的功能，即要求认证成功后才能执行函数
#
# 四：编写装饰器，为多个函数加上认证的功能（用户的账号密码来源于文件），要求登录成功一次，后续的函数都无需再输入用户名和密码
#
# 提示：从文件中读出字符串形式的字典，可以用eval('{"name":"egon","password":"123"}')转成字典格式

user_status = False

def time_comp(time_type):
    def outer(func):

        def inner(*args, **kwargs):

            _username = 'wyd'
            _pasword = 'wyd123'
            global user_status
            if user_status is False:
                user_input = input('user:').strip()
                passwd_input = input('passwd:').strip()
                if user_input == _username and passwd_input == _pasword:
                    user_status = True
                    print('welcome %s !' % user_input)
                else:
                    print('user/passwd Error!')
            if user_status:
                print('用户已登录，验证通过')
                start_time = time.time()
                func(*args, **kwargs)
                print(time.time() - start_time)

        return inner
    return outer


@time_comp('S')
def calc(arg):
    time.sleep(2)
    print(arg)


@time_comp('S')
def sayhi(name):
    time.sleep(2)
    print('Hi,%s' % name)


@time_comp('M')
def sayby(name):
    time.sleep(2)
    print('By,%s' % name)


calc('wyd')
sayhi('wyd')
sayby('wyd')
