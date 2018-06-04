# -*- coding:utf-8 -*-
import shelve,logging
from logging import handlers
#2017-10-18 15:56:26,613 - access - ERROR - account [1234] too many login attempts
#debug()/info()/waring()/error()/critical()
# logging.warning('user [alex] attempted wrong password morethan 3 times')
# logging.critical('server is down')
#
#
# logging.basicConfig(filename = 'example.log',level=logging.DEBUG)
# logging.debug('This message should go to the log file')
# logging.info('So should this')
# logging.warning('And this.too')


# logging.basicConfig(format = '%(asctime)s %(levelname)s %(process)d  %(message)s')
# logging.warning('is when this event was logged')

#LOG = logging.getLogger("chat.gui")
# Logger.setLevel(lel):#指定最低的日志级别，低于lel的级别将被忽略。debug是最低的内置级别，critical为最高
# Logger.addFilter(filt)
# Logger.removeFilter(filt)
# Logger.addHandler(hdlr)
# Logger.removeHandler(hdlr)

#1.生成logger 对象
logger = logging.getLogger("access")
logger.setLevel(logging.DEBUG)
#2.生成handler 对象
ch = logging.StreamHandler()
fh = logging.FileHandler("web.log")
# handlers.RotatingFileHandler #设置日志截断 按文件大小进行，maxBytes为文件最大字节数，backupCount为备份个数
# fh = handlers.RotatingFileHandler("web.log",maxBytes=10,backupCount=10)
# handlers.TimedRotatingFileHandler #设置日志截断 按时间进行，when为时间格式，interval为时间间隔，backupCount为备份个数
# fh = handlers.TimedRotatingFileHandler("web.log",when="S",interval=5, backupCount=10)


#2.1 把handler对象绑定logger
logger.addHandler(ch)
logger.addHandler(fh)

#3.生成formatter 对象
#3.1 把formatter绑定handler对象 account [1234]
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
console_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s [%(lineno)d] - %(message)s")
ch.setFormatter(console_formatter)
fh.setFormatter(file_formatter)

logger.debug('too young to simple')
