# -*- coding:utf-8 -*-

import os
import time
from core import getter
from core import md5
from config import settings

user_status = False
pay_status = False

def login(logger):
    def outter(func):
        def inner(*args, **kwargs):
            global user_status
            count = 0
            if not user_status:

                while count < 3:
                    user_input = input("user:").strip()
                    global user_input
                    passwd_input = input("passwd:").strip()

                    file_name = "%s/account/%s.json" % (
                        settings.BASE_DIR, user_input)
                    if os.path.exists(file_name):

                        data = getter.json_data_get(file_name)

                        #username = data.keys
                        passwd = data[user_input]['password']
                        if user_input in data.keys() and md5.hash_md5(passwd_input) == passwd:
                            local_time = time.strftime(
                                "%Y-%m-%d", time.localtime())

                            if data[user_input]["expire_date"] > local_time and data[user_input]["status"] == 0:
                                user_status = True
                                logger.info("user loggin")
                                func(*args, **kwargs)
                            else:
                                logger.error("expire_date or status error")

                        else:
                            logger.error('user/passwd input Error')
                    count += 1

            else:
                logger.info('user loggin')
                func(*args, **kwargs)
        return inner
    return outter

def pay_author(logger):
    def outter(func):
        def inner(*args,**kwargs):
            while True:
                pay_account = input("Please enter your account name:").strip()
                global pay_account
                pay_passwd = input("Please enter your account password:").strip()
                if not pay_account:
                    continue
                else:

                    data = getter.json_data_get(settings.BANK_FILE)
                    count = 0
                    if pay_account in data.keys():
                        if not pay_status:
                            while count < 3:

                                pay_passwd_file = data[pay_account]["passwd"]

                                if md5.hash_md5(pay_passwd) == pay_passwd_file:
                                    logger.info('Payment password verified successfully')
                                    func(*args,**kwargs)
                                else:
                                    logger.error(
                                        "Payment password error.The account will be locked after 3 errors!")
                                count += 1
                        else:
                            func(*args, **kwargs)
                    else:
                        logger.error('Account does not exist')
        return inner
    return outter
#
# def json_data(file_name):
#     with open(file_name, "r+", encoding="utf-8") as login_file:
#         data = json.dump(login_file)
#     return data
