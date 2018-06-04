# -*- coding:utf-8 -*-

import os
from core import getter
from core import check_out
from config import settings
from core import user_login



def print_shop_cart(func,logger_obj):
    for i in range(len(func['product'])):
        logger_obj.info('商品:%s\t单价:%s' % (func['product'][i], func['price'][i]))
        
def comp_money(shopping_record):
    data = getter.json_data_get(shopping_record)
    shop_money = 0
    for i in data:
        shop_money += data[i]["count"] * data[i]["price"]
    print(shop_money)
    return shop_money


def shopping_cart(products,logger_obj):
    file_name = "%s/account/%s_shop_cart.json" % (settings.BASE_DIR, user_login.user_input)
    if os.path.exists(file_name):
        shop_cart = getter.json_data_get(file_name)
    else:
        shop_cart = {}
    
    while True:
        for goods_key, goods_value in enumerate(products):
            print(
                '%s\t%s\t%s\t' %
                (goods_key,
                 goods_value['name'],
                 goods_value['price']))
            
        choice = input('请输入产品编号进行购买,退出请输入Q:').strip()

        if not choice:
            continue
        elif choice.isdigit() and 0 <= int(choice) < len(products):
            good_buy = products[int(choice)]
            if good_buy['name'] in shop_cart.keys():
                count = shop_cart[good_buy['name']]["count"]  + 1
                shop_cart[good_buy['name']]["count"] = count
                logger_obj.info('已经商品%s添加进购物车' % good_buy['name'])
            else:
                shop_cart[good_buy['name']] = {"count": 1, "price": good_buy['price']}
                logger_obj.info('已经商品 %s 添加进购物车' % good_buy['name'])
                
        elif  choice.upper() == "Q":
            print("1. 结账")
            print("2. 保存退出")
            input_choice = input('请选择:')
            
            getter.json_data_put(shop_cart, file_name)
            if int(input_choice) == 1:
                print(shop_cart)
                out_money = comp_money(file_name)
                logger_obj.info("本次共消费%s元"%out_money)
                pay_account = input("请输入支付账号:").strip()
                pay_passwd = input("请输入支付密码:").strip()
                check_out.check_out(out_money, pay_account, pay_passwd,"tesla",logger_obj)
                shop_cart = { }
                logger_obj.info("购物车已无商品")
                getter.json_data_put(shop_cart, file_name)
                exit()
            elif int(input_choice) == 2:
               
                exit()
                logger_obj.info("保存退出购物结束")
