# -*- coding:utf-8 -*-

from core import getter
from config import settings
from core import md5
# 提供管理接口，包括添加账户、用户额度，冻结账户,信息查看等


def info_account(account_name,logger_obj):
    """
    :param account_name:
    :param logger_obj: logging object
    :return: None
    print account information,
    argument is account name
    """
    bank_data = getter.json_data_get(settings.BANK_FILE)
    for i in bank_data[account_name]:
        if i == "passwd":
            continue
        print("%s:%s"%(i,bank_data[account_name][i]))
    logger_obj.info("print account information")
    

def add_account(logger_obj):
    """
    :param logger_obj: logging object
    :return: None
    add account information
    """
    user_moudle = settings.USER_MOD
    bank_data = getter.json_data_get(settings.BANK_FILE)
    
    input_acc_name = input("请输入账户名:").strip()
    
    for i in user_moudle:

        while True:
            val = input("请输入%s 信息:" % i).strip()
            if not val:
                continue
            elif i == "passwd":
                val_passwd = input("请再次输入%s 信息:" % i).strip()
                if val == val_passwd:
                    val = md5.hash_md5(val)
                    user_moudle[i] = val
                    break
                else:
                    logger_obj.info("密码两次结果不一致")
                    continue
            else:
                if user_moudle[i] == int:
                    if val.isdigit() and int(val) >= 0:
                        user_moudle[i] = int(val)
                        break
                    else:
                        logger_obj.info("数据输入有误")
                else:
                    user_moudle[i] = val
                    break

    
    bank_data[input_acc_name] = user_moudle
    getter.json_data_put(bank_data,settings.BANK_FILE)
    logger_obj.info("%s信息添加成功"%input_acc_name)


def increase_credit_limit(account_name,logger_obj):
    """
    :param account_name:
    :return: None
    increase credit limit
    """
    bank_data = getter.json_data_get(settings.BANK_FILE)
    while True:
        limit_imput = input("请输入增加的额度:").strip()
        if not limit_imput:
            continue
        elif limit_imput.isdigit() and int(limit_imput) > 0:
            bank_data[account_name]["limit"] += int(limit_imput)
            bank_data[account_name]["balance"] += int(limit_imput)
            getter.json_data_put(bank_data, settings.BANK_FILE)
            logger_obj.info("increase credit limit %s success"%limit_imput)
            break

        else:
            logger_obj.info("%s账户已冻结" % account_name)


def frozen_account(account_name,logger_obj, status=1):
    """
    :param account_name:
    :param logger_obj:
    :param status:
    :return:
    """
    bank_data = getter.json_data_get(settings.BANK_FILE)
    if status == 1:
        bank_data[account_name]["status"] = 1
        getter.json_data_put(bank_data, settings.BANK_FILE)
        logger_obj.info("%s账户已冻结" % account_name)
    else:
        if bank_data[account_name]["status"] == 0:
            logger_obj.info("%s账户为解冻状态，无需解冻" % account_name)
        else:
            bank_data[account_name]["status"] = 0
            getter.json_data_put(bank_data, settings.BANK_FILE)
            logger_obj.info("%s账户已解冻" % account_name)


#add_account()