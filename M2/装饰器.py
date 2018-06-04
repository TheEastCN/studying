# -*- coding:utf-8 -*-

user_status = False


def login(auth_type):
    def outer(fun):
        def inner(*args, **kwargs):
            _username = 'wyd'
            _pasword = 'wyd123'
            global user_status
            if auth_type == 'qq':
                
                if user_status is False:
        
                    user_input = input('user:').strip()
                    passwd_input = input('passwd:').strip()
        
                    if user_input == _username and passwd_input == _pasword:
                        user_status = True
                        print('welcome %s !' % user_input)
                    else:
                        print('user/passwd Error!')
            else:
                print('only support qq !')
            if user_status:
                print('用户已登录，验证通过')
                fun(*args, **kwargs)
        return inner
    return outer


@login('qq')
def index(style):

    print('--index--')
    print(style)


@login('qq')
def choice():
    print('--choice--')


index('首页')
choice()
