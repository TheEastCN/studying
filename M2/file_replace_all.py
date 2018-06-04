# -*- coding:utf-8 -*-

import os


def replace_file(file_name, old_str, new_str):
    file_new_name = ''.join([file_name, '_new'])
    with open(file_name, 'r', encoding='utf-8') as file_old, open(file_new_name, 'w', encoding='utf-8') as file_new:
        for line in file_old:
            if old_str in line:
                rep_line = line.replace(old_str, new_str)
                file_new.write(rep_line)
            else:
                file_new.write(line)

    os.remove(file_name)
    os.rename(file_new_name, file_name)


replace_file('将进酒.txt', '.', '。')
