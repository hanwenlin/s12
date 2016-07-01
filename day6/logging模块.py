import  logging
# logging.warning("user [zhangjun] attempted wrong password more than 3 times")
# logging.critical("server is down")
'''输出
WARNING:root:user [zhangjun] attempted wrong password more than 3 times
CRITICAL:root:server is down
'''
logging.basicConfig(filename='example.log',level=logging.INFO,
                    format='%(asctime)s %(message)s',datefmt='%m/%d/%Y %I:%M:%S %p')
logging.debug("this is should go to the log file")
logging.info('So should this')
logging.warning('And this .too')
