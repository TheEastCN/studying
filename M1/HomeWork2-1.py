# -*- coding:utf-8 -*-

# 可依次选择进入各子菜单
# 可从任意一层往回退到上一层
# 可从任意一层退出程序
# 所需新知识点：列表、字典
# 1.完成需求/条---25分
# 2.只用一个while循环，且整体代码量少于15行，得分90.
menu = {
    '北京': {
        '海淀': {
            '五道口': {
                'soho': {},
                '网易': {},
                'google': {}
            },
            '中关村': {
                '爱奇艺': {},
                '汽车之家': {},
                'youku': {},
            },
            '上地': {
                '百度': {},
            },
        },
        '昌平': {
            '沙河': {
                '老男孩': {},
                '北航': {},
            },
            '天通苑': {},
            '回龙观': {},
        },
        '朝阳': {},
        '东城': {},
    },
    '上海': {
        '闵行': {
            "人民广场": {
                '炸鸡店': {}
            }
        },
        '闸北': {
            '火车站': {
                '携程': {}
            }
        },
        '浦东': {},
    },
    '山东': {},
}


dic_menu = menu
upper_menu = []

while True:
    for level_key in dic_menu:
        print(level_key)
    choice = input('请输入菜单名,退出程序请输入Q,返回上一层请输入B:').strip()
    if not choice:
        continue
    elif choice in dic_menu.keys():
        upper_menu.append(dic_menu)
        dic_menu = dic_menu[choice]
    elif choice.upper() == 'B':
        if len(upper_menu) >0:
            dic_menu = upper_menu.pop()
        else:
            print('已经是最顶层')
    elif choice.upper() == 'Q':
        exit('退出系统')
    else:
        print('\033[1;31m输入有误，请输入显示内容\033[0m')
