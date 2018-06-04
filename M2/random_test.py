# -*- coding:utf-8 -*-

import random
import string


random_len = 6
#s = random.sample(string.ascii_lowercase + string.ascii_uppercase + string.digits,6)
int_random_low = int(random.randint(1,4))
int_random_up = int(random.randint(1,random_len-int_random_low-1))
random_lowercase = random.sample(string.ascii_lowercase,int_random_low)
random_uppercase = random.sample(string.ascii_uppercase,int_random_up)
random_digit = random.sample(string.digits,random_len-int_random_low-int_random_up)
print(''.join(random_lowercase+random_uppercase+random_digit))