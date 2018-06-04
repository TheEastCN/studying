# -*- coding:utf-8 -*-

from prettytable import PrettyTable

title = [
    "staff_id",
    "name",
    "age",
    "phone",
    "dept",
    "enroll_date"]


# def get_info():
#     # 获取文件内数据
#     staff_file = open('staff.txt', 'r+', encoding='utf-8')
#     data_list = []
#     for data in staff_file:
#
#         data_list.append(data.strip('\n').split(','))
#
#     staff_file.close()
#     return data_list

def get_info(change_type, change_field, old_str=None, new_str=None):
    # 获取文件内数据
    
    staff_file = open('staff.txt', 'r+', encoding='utf-8')
    global data
    data = staff_file.readlines()
    data_list = []
    line_sort = {}
    for i in data:
        data_list.append(i.strip('\n').split(','))
    
    if change_type.upper() == 'UPDATE':
        change_index = title.index(change_field)
        for line in data_list:
            if line[change_index] == old_str:
                line[change_index] = new_str
        
        data = []
        for list_i in data_list:
            data_str = ','.join(list_i)
            data.append(data_str)
    
    elif change_type.upper() == 'ADD':
        
        for line in data_list:
            line_sort[int(line[0])] = line[3]
        
        staff_id_max = int(max(line_sort.keys()))
        staff_id_max += 1
        list_add = (str(staff_id_max) + ',' + change_field).split(',')
        if list_add[3] not in line_sort.values():
            data_list.append(list_add)
            data = []
        else:
            print('\033[1;31m phone violate the only constraint!\033[0m')
        for list_i in data_list:
            data_str = ','.join(list_i)
            data.append(data_str)
    elif change_type.upper() == 'DEL' or change_type.upper() == 'DELETE':
        for line in data_list:
            change_index = title.index(change_field)
            if line[change_index] == old_str:
                data_list.remove(line)
        
        data = []
        for list_i in data_list:
            data_str = ','.join(list_i)
            data.append(data_str)
    else:
        staff_file.close()
        return data_list
    
    staff_file.seek(0)
    staff_file.truncate()
    staff_file.write('\n'.join(data))
    staff_file.close()


# def print_info(print_filed, res_info):
#     # 获取展示字段的数据，并打印结果
#     #print_filed 为表头展示字段 列表类型，res_info 为信息表中每行数据列表类型
#     table = PrettyTable(print_filed)
#     find_relation = []
#     for i in print_filed:
#         title_index = title.index(i)
#         find_relation.append(res_info[title_index])
#     table.add_row(find_relation)
#     print(table)

def where_func(res, operator_type, operator_char, where_index, statement_value):
    count = 0
    if operator_char == '=':
        for res_info in res:
            if res_info[where_index] == statement_value:
                count += 1
    elif operator_char == '>':
        for res_info in res:
            if res_info[where_index] == statement_value:
                count += 1
    elif operator_char == '<':
        for res_info in res:
            if res_info[where_index] == statement_value:
                count += 1
    
    elif operator_char == 'like':
        for res_info in res:
            if res_info[where_index] == statement_value:
                count += 1
                
    print('%s数据%s条' % (operator_type, count))


def fillter_func(
        statement_fillter,
        statement_where,
        operator_char,
        statement_value,
        fillter_type):
    # statement_fillter 参数为展示的字段字符串,statement_where 判断条件字段字符串，statement_value
    # 为需要比较的数据,fillter_type 为筛选的类型（查询，修改，删除，新增等）
    
    print_filed = statement_fillter.split(',')
    
    where_index = title.index(statement_where)
    res = get_info('', None)
    where_res = where_func(res, operator_char, where_index, statement_value, print_filed)
    print('%s数据%s条' % (fillter_type,where_res))
    
    


def find_grammar(find_statement):
    # 查询语句函数，find_statement为将输入字符串语句转换后的列表，长度为8
    if len(find_statement) == 8:
        if find_statement[2] == 'from' and find_statement[4] == 'where':
            
            if find_statement[6] == '=':
                fillter_func(
                    find_statement[1],
                    find_statement[5],
                    find_statement[6],
                    find_statement[7],
                    '查询')
            elif find_statement[6] == '<':
                fillter_func(
                    find_statement[1],
                    find_statement[5],
                    find_statement[6],
                    find_statement[7],
                    '查询')
            elif find_statement[6] == '>':
                fillter_func(
                    find_statement[1],
                    find_statement[5],
                    find_statement[6],
                    find_statement[7],
                    '查询')
            
            elif find_statement[6] == 'like':
                fillter_func(
                    find_statement[1],
                    find_statement[5],
                    find_statement[6],
                    find_statement[7],
                    '查询')
            else:
                print('运算符错误')
        else:
            print(
                '\033[1;31mSorry,Grammar Error!Please choice the statement!\033[0m')
    else:
        print(
            '\033[1;31mSorry,Grammar Error!Verify that the statement contains a positive value space!\033[0m')


def del_grammar(find_statement):
    # 查询语句函数，find_statement为将输入字符串语句转换后的列表，长度为8
    if len(find_statement) == 7:
        if find_statement[1] == 'from' and find_statement[3] == 'where':
            
            if find_statement[5] == '=':
                get_info('del', find_statement[4])
                fillter_func(
                    ''.join(title),
                    find_statement[4],
                    find_statement[5],
                    find_statement[6],
                    '删除')
            
            elif find_statement[5] == '<':
                fillter_func(
                    ''.join(title),
                    find_statement[4],
                    find_statement[5],
                    find_statement[6],
                    '删除')
            elif find_statement[5] == '>':
                fillter_func(
                    ''.join(title),
                    find_statement[4],
                    find_statement[5],
                    find_statement[6],
                    '删除')
            
            elif find_statement[5] == 'like':
                fillter_func(
                    ''.join(title),
                    find_statement[4],
                    find_statement[5],
                    find_statement[6],
                    '删除')
            else:
                print('运算符错误')
        else:
            print(
                '\033[1;31mSorry,Grammar Error!Please choice the statement!\033[0m')
    else:
        print(
            '\033[1;31mSorry,Grammar Error!Verify that the statement contains a positive value space!\033[0m')


def main_opre():
    exit_flag = False
    while not exit_flag:
        input_sql = input('SQL>').strip()
        if not input_sql:
            continue
        else:
            input_list = input_sql.split()
            if input_list[0].upper() == 'UPDATE':
                pass
            elif input_list[0].upper() == 'FIND':
                find_grammar(input_list)
            elif input_list[0].upper() == 'DEL' or input_list[0].upper() == 'DELETE':
                pass
            elif input_list[0].upper() == 'ADD':
                pass
            elif input_sql.upper() == 'EXIT':
                exit_flag = True
                break
            else:
                print('\033[1;31mSorry,Grammar Error!\033[0m')


main_opre()


