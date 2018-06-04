# -*- coding:utf-8 -*-

import time


def time_format():
	t = time.time()
	local_time = time.localtime(t)
	str_time = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
	return  str_time

def logger(filename,channel='file'):
	count = 1
	line_count = '['+ str(count) +']'
	file_log =  open(filename, 'a+', encoding='utf-8')
	while True:
		if channel == 'file':
			line = yield
			
			log_format = ' '.join([time_format(),line_count,line])
			file_log.write(log_format)
		elif channel == 'terminal':
			line = yield
			log_format = ' '.join([time_format(), line_count, line])
			print(log_format)
		elif channel == 'both':
			line = yield
			log_format = ' '.join([time_format(), line_count, line])
			file_log.write(log_format)
			print(log_format)
		count += 1


log_obj = logger(filename="web.log",channel='both')
log_obj.__next__()
log_obj.send('user alex login success')


	

		