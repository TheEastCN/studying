# -*- coding:utf-8 -*-

import os
import logging


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

USER_FILE = "%s/%s/%s"%(BASE_DIR,"account","luffy.json" )
BANK_FILE = "%s/%s/%s"%(BASE_DIR,"account","BANK.json" )
LOG_LEVEL = logging.INFO

LOG_TYPES = {
    'transaction': 'transactions.log',
    'access': 'access.log'
}

PRODUCTS = [
 {"name": "computer", "price": 4999},
 {"name": "mouse", "price": 199},
 {"name": "yacht", "price": 2000000},
 {"name": "Iphone", "price": 8999},
 {"name": "House", "price": 5000000},
 {"name": "Tesla", "price": 750000}
]


USER_MOD = {"account":str, "passwd":str, "status":int,"cardno":str, "limit":int, "balance":int}
