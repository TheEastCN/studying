# -*- coding:utf-8 -*-

import logging
import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from config import settings

def logger(log_obj):

    logger = logging.getLogger(log_obj)
    logger.setLevel(settings.LOG_LEVEL)

    console_handle = logging.StreamHandler()
    

    log_file =  "%s/logs/%s" %(settings.BASE_DIR, settings.LOG_TYPES[log_obj])


    file_handle =logging.FileHandler(log_file)
    file_handle.setLevel(settings.LOG_LEVEL)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    console_handle.setFormatter(formatter)
    file_handle.setFormatter(formatter)

    logger.addHandler(console_handle)
    logger.addHandler(file_handle)
    
    return logger