# -*- coding:utf-8 -*-

from core import logger
from core import check_out
from core import acc_manage
from core import shopping_cart
from core import user_login
from config import settings

logger_obj_acce = logger.logger('access')
logger_obj_trans = logger.logger('transaction')
main_menu = {1: "购物车", 2: "ATM"}
atm_menu = {
    1: "信息查询",
    2: "还款",
    3: "取现",
    4: "账户新增",
    5: "增额",
    6: "账户冻结",
    7: "转账"}


@user_login.pay_author(logger_obj_acce)
def atm_main():
    while True:
        print("ATM 功能选择".center(20, '-'))
        for key in atm_menu:
            print("%s. %s" % (key, atm_menu[key]))
        input_atm = input("请选择功能,退出请输入Q:").strip()
        if not input_atm:
            continue
        elif input_atm.isdigit() and int(input_atm) == 1:
            # 1:"信息查询",2:"还款",3:"取现",4:"账户新增",5:"增额",6:"账户冻结",7:"转账"
            acc_manage.info_account(user_login.pay_account, logger_obj_trans)
        elif input_atm.isdigit() and int(input_atm) == 2:
            check_out.repay(user_login.pay_account, logger_obj_trans)
        elif input_atm.isdigit() and int(input_atm) == 3:
            check_out.with_draw(None, user_login.pay_account, logger_obj_trans)
        elif input_atm.isdigit() and int(input_atm) == 4:
            acc_manage.add_account(logger_obj_trans)
        elif input_atm.isdigit() and int(input_atm) == 5:
            acc_manage.increase_credit_limit(
                user_login.pay_account, logger_obj_trans)
        elif input_atm.isdigit() and int(input_atm) == 6:
            acc_manage.frozen_account(
                user_login.pay_account, logger_obj_trans, status=1)
        elif input_atm.isdigit() and int(input_atm) == 7:
            check_out.check_out(
                None,
                user_login.pay_account,
                None,
                None,
                logger_obj_trans)
        elif input_atm.upper() == "Q":
            exit("Program aborted")


@user_login.login(logger_obj_acce)
def shop_main():
    shopping_cart.shopping_cart(settings.PRODUCTS, logger_obj_trans)


def menu():

    while True:

        for choice_outter in main_menu:
            print("%s.%s" % (choice_outter, main_menu[choice_outter]))

        choice_val = input("请选择功能,退出请按Q:").strip()
        if not choice_val:
            continue
        elif choice_val.isdigit() and int(choice_val) == 1:

            shop_main()
        elif choice_val.isdigit() and int(choice_val) == 2:

            atm_main()

        elif choice_val.upper() == "Q":
            exit("Program aborted")


menu()
