# -*- coding:utf-8 -*-
import sys
menu = {'北京': {'海淀': {'五道口': {'soho': {}, '网易': {}, 'google': {}}, '中关村': {'爱奇艺': {}, '汽车之家': {}, 'youku': {}, }, '上地': {'百度': {}, }, }, '昌平': {'沙河': {'老男孩': {}, '北航': {}, }, '天通苑': {}, '回龙观': {}, }, '朝阳': {}, '东城': {}, }, '上海': {'闵行': {"人民广场": {'炸鸡店': {}}}, '闸北': {'火车战': {'携程': {}}}, '浦东': {}, }, '山东': {},}
this_layer = menu
while True:
    choice = input("1.若列表非空：你可选择的有%s或返回上层[back]或退出[quit]；\n2.若列表为空：\
    你可以返回上层[back]或退出[quit]否则自动退出\n3.选择错误程序会自动退出\n--->你的选择为:" % [x for x in this_layer.keys()])
    if (not this_layer and choice != "back" and choice != "quit") or (choice not in this_layer.keys() and choice != "back" and choice != "quit"):
        sys.exit("程序已退出")
    elif choice == "back":
        this_layer = this_layer_upper_levels
    elif choice == "quit":
        sys.exit("程序已退出")
    else:
        this_layer_upper_levels = this_layer
        this_layer = this_layer[choice]
