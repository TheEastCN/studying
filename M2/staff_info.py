# -*- coding:utf-8 -*-
import os
from prettytable import PrettyTable

title = [
    "id",
    "name",
    "age",
    "phone",
    "dept",
    "enroll_date"]

def file_exist(file_name):
    if os.path.exists(file_name) is False:
        file_create = open(file_name, 'w', encoding='utf-8')
        file_create.close()
    

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
    # change_type 语句类型del/update/add（字符串）, change_field  条件字段 字符串(添加数据为添加的数据), old_str 在change_type为del 时，为判断条件的值, new_str=None
    
    staff_file = open('staff.txt', 'r+', encoding='utf-8')
    global data
    data = staff_file.readlines()
    data_list = []
    line_sort = {}
    for i in data:
        data_list.append(i.strip('\n').split(','))
    
    if change_type.upper() == 'UPDATE':
        if type(change_field) is list:
            change_index = []
            for field_i in change_field:
                change_index.append(title.index(field_i))
            for line in data_list:
                if line[change_index[0]] == old_str:
                    line[change_index[1]] = new_str
        else:
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
            return  False
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
    return data_list

def where_func(res, operator_type, operator_char, statement_where, statement_value):
    count = 0
    where_index = title.index(statement_where)
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

def fillter_func(statement_fillter, statement_where, operator_char, statement_value, fillter_type):
    # statement_fillter 参数为展示的字段字符串,statement_where 判断条件字段字符串，statement_value
    # 为需要比较的数据,fillter_type 为筛选的类型（查询，修改，删除，新增等）
    if statement_fillter == '*':
        print_filed = title
    else:
        print_filed = statement_fillter.split(',')
    table = PrettyTable(print_filed)
    count = 0
    where_index = title.index(statement_where)
    res = get_info('',None)
    if operator_char == '=':
        for res_info in res:
            if res_info[where_index] == statement_value:
                #print_info(print_filed, res_info)
                find_relation = []
                for i in print_filed:
                    title_index = title.index(i)
                    find_relation.append(res_info[title_index])
                table.add_row(find_relation)
                count += 1
    elif operator_char == '>':
        for res_info in res:
            if res_info[where_index] > statement_value:
                #print_info(print_filed, res_info)
                find_relation = []
                for i in print_filed:
                    title_index = title.index(i)
                    find_relation.append(res_info[title_index])
                table.add_row(find_relation)
                count += 1
    elif operator_char == '<':
        for res_info in res:
            if res_info[where_index] < statement_value:
                #print_info(print_filed, res_info)
                find_relation = []
                for i in print_filed:
                    title_index = title.index(i)
                    find_relation.append(res_info[title_index])
                table.add_row(find_relation)
                count += 1

    elif operator_char == 'like':
        for res_info in res:
            if statement_value in res_info[where_index]:
                #print_info(print_filed, res_info)
                find_relation = []
                for i in print_filed:
                    title_index = title.index(i)
                    find_relation.append(res_info[title_index])
                table.add_row(find_relation)
                count += 1
    print(table)
    print('%s数据%s条' % (fillter_type, count))
    return table


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
                    'find')
            elif find_statement[6] == '<':
                fillter_func(
                    find_statement[1],
                    find_statement[5],
                    find_statement[6],
                    find_statement[7],
                    'find')
            elif find_statement[6] == '>':
                fillter_func(
                    find_statement[1],
                    find_statement[5],
                    find_statement[6],
                    find_statement[7],
                    'find')

            elif find_statement[6] == 'like':
                fillter_func(
                    find_statement[1],
                    find_statement[5],
                    find_statement[6],
                    find_statement[7],
                    'find')
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

            result_list = get_info(' ', None)
            where_func(result_list, 'delete', find_statement[5], find_statement[4], find_statement[6])
            get_info('del', find_statement[4], old_str=find_statement[6])

        else:
            print(
                '\033[1;31mSorry,Grammar Error!Please choice the statement!\033[0m')
    else:
        print(
            '\033[1;31mSorry,Grammar Error!Verify that the statement contains a positive value space!\033[0m')


def add_grammar(find_statement):
    # 查询语句函数，find_statement为将输入字符串语句转换后的列表，长度为8
    if len(find_statement) == 3 :
        if find_statement[1] == 'staff_table':
            if len(','.join(find_statement[2])) == 5:
                result_list = get_info(' ', None)
                res_bool = get_info('add', find_statement[2])
                if not res_bool:
                    print('add 1 条数据成功')
                else:
                    print('add 数据失败')
            else:
                print('数据缺失')
        else:
            print(
                '\033[1;31mSorry,Grammar Error!Please choice the statement!\033[0m')
    elif len(find_statement) == 4 :
        add_list = find_statement[3].split(',')
        add_list[0] = find_statement[2] + ' ' + find_statement[3].split(',')[0]
        if find_statement[1] == 'staff_table':
            if len(add_list) == 5:
                result_list = get_info(' ', None)
                get_info('add', ','.join(add_list))
                print('add数据成功')
            else:
                print('数据缺失')
        else:
            print(
                '\033[1;31mSorry,Grammar Error!Please choice the statement!\033[0m')
    else:
        print(
            '\033[1;31mSorry,Grammar Error!Verify that the statement contains a positive value space!\033[0m')


def update_grammar(find_statement):
    # 查询语句函数，find_statement为将输入字符串语句转换后的列表，长度为8

    if len(find_statement) == 10:
        if find_statement[2].upper() == 'SET' and find_statement[6].upper() == 'WHERE':

            result_list = get_info(' ', None)
            where_func(result_list, 'update', find_statement[8], find_statement[7], find_statement[9])
            if find_statement[3] == find_statement[7]:
               get_info('update', find_statement[7], find_statement[9], find_statement[5])
            else:
                get_info('update', [find_statement[7],find_statement[3]], find_statement[9], find_statement[5])

        else:
            print(
                '\033[1;31mSorry,Grammar Error!Please choice the statement!\033[0m')
    elif len(find_statement) > 10 :

        if find_statement[8] == 'name' and find_statement[3] == 'name':
            find_statement[5] = find_statement[5] + ' ' + find_statement[6]
            find_statement[10] = find_statement[10] + ' ' + find_statement[11]
            find_statement.remove(find_statement[6])
            find_statement.remove(find_statement[-1])

            result_list = get_info(' ', None)
            where_func(result_list, 'update', find_statement[8], find_statement[7], find_statement[9])
            if find_statement[3] == find_statement[7]:
                get_info('update', find_statement[7], find_statement[9], find_statement[5])
            else:
                get_info('update', [find_statement[7], find_statement[3]], find_statement[9], find_statement[5])

        elif find_statement[7] == 'name':
            find_statement[9] = find_statement[9] + ' ' + find_statement[10]
            result_list = get_info(' ', None)
            where_func(result_list, 'update', find_statement[8], find_statement[7], find_statement[9])
            if find_statement[3] == find_statement[7]:
                get_info('update', find_statement[7], find_statement[9], find_statement[5])
            else:
                get_info('update', [find_statement[7], find_statement[3]], find_statement[9], find_statement[5])

        elif find_statement[3] == 'name':

            find_statement[5] = find_statement[5] + ' ' + find_statement[6]
            find_statement.remove(find_statement[6])
            result_list = get_info(' ', None)
            where_func(result_list, 'update', find_statement[8], find_statement[7], find_statement[9])
            if find_statement[3] == find_statement[7]:
                get_info('update', find_statement[7], find_statement[9], find_statement[5])
            else:
                get_info('update', [find_statement[7], find_statement[3]], find_statement[9], find_statement[5])

    else:
        print(
            '\033[1;31mSorry,Grammar Error!Verify that the statement contains a positive value space!\033[0m')


def main_opre():
    file_exist('staff.txt')
    exit_flag = False
    while not exit_flag:
        input_sql = input('SQL>').strip()
        if not input_sql:
            continue
        else:
            input_list = input_sql.split()
            if input_list[0].upper() == 'UPDATE':
                update_grammar(input_list)
            elif input_list[0].upper() == 'FIND':
                find_grammar(input_list)
            elif input_list[0].upper() == 'DEL' or input_list[0].upper() == 'DELETE':
                del_grammar(input_list)
            elif input_list[0].upper() == 'ADD':
                add_grammar(input_list)
            elif input_sql.upper() == 'EXIT':
                exit_flag = True
                break
            else:
                print('\033[1;31mSorry,Grammar Error!\033[0m')
    
main_opre()


