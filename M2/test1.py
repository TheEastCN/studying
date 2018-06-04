# -*- coding:utf-8 -*-

title = [
    "staff_id",
    "name",
    "age",
    "phone",
    "dept",
    "enroll_date"]


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


#get_info('add', 'Alex Li,25,134435344,IT,2015‐10‐29')
res = get_info('',None)
print(res)