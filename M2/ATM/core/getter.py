# -*- coding:utf-8 -*-

import json

def json_data_put(data_obj,file_name):
    with open(file_name, "w", encoding="utf-8") as put_file:
        data = json.dump(data_obj,put_file)

    return data

def json_data_get(file_name):
    with open(file_name, "r+", encoding="utf-8") as get_file:
        data = json.load(get_file)
    return data