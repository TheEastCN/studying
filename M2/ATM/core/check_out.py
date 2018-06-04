# -*- coding:utf-8 -*-

from core import getter
from config import settings
from core import md5


def check_out(money, username, passwd, username_in,logger_obj):
    """
    :param money: repayment amount
    :param username: Transfer accounts
    :param passwd: pay password
    :param username_in: transfer into the account
    :param logger_obj: logging object
    :return: None

    """
    if username_in is None:
        username_in = input("Please enter the transfer account:").strip()
    if money is None:
        money = input("Please enter the amount of transfer:").strip()
    if passwd is None:
        passwd = input("Please enter the payment password:").strip()
    bank_data = getter.json_data_get(settings.BANK_FILE)
    # pay_data = getter.json_data_get(settings.PAY_FILE)
    if bank_data[username]["passwd"] == md5.hash_md5(passwd):
        if int(money) < bank_data[username]["balance"]:
            bank_data[username]["balance"] -= int(money)
            bank_data[username_in]["balance"] += int(money)
            getter.json_data_put(bank_data, settings.BANK_FILE)
            logger_obj.info('%s扣款成功' % username)
            logger_obj.info('%s入账成功' % username_in)
        else:
            logger_obj.error('%s账户余额不足' % username)
    else:
        logger_obj.error('%s支付密码错误' % username)


def with_draw(money, username,logger_obj):
    """
    :param money:
    :param username:
    :param logger_obj:
    :return:
    """
    bank_data = getter.json_data_get(settings.BANK_FILE)
    
    card_balance = bank_data[username]["balance"]
    if money is None:
        money =  input("Please enter the withdrawal amount:").strip()
    cash_adv_money = int(money) * 1.05
    if cash_adv_money <= card_balance:
        service_charge = int(money) * 0.05
        bank_data[username]["balance"] = card_balance - cash_adv_money
        getter.json_data_put(bank_data, settings.BANK_FILE)
        logger_obj.info("%s 取现%s,手续费%s" % (username, money, service_charge))
    else:
        logger_obj.error("余额不足")


def repay(username,logger_obj):
    """
    :param username:
    :param logger_obj:
    :return:
    """
    bank_data = getter.json_data_get(settings.BANK_FILE)
    debt = bank_data[username]["limit"] - bank_data[username]["balance"]
    print("欠款：%s" % debt)
    while True:
        repay_money = input("请输入还款金额:").strip()
        if not repay_money:
            continue
        elif repay_money.isdigit() and int(repay_money) > 0:
            bank_data[username]["balance"] += int(repay_money)
            getter.json_data_put(bank_data, settings.BANK_FILE)
            debt = bank_data[username]["limit"] - bank_data[username]["balance"]
            if debt == 0:
                logger_obj.info("欠款已还清")
                break
            else:
                logger_obj.info("已还金额：%s,欠款:%s" % (repay_money, debt))
                break
        else:
            logger_obj.error("输入额度错误")



