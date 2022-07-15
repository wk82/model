#CDN公共源rsync同步文件python代码
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

import os
import commands
import threading
import Queue
import logging

thread_num = 5

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='sync.log',
                    filemode='w')


class SyncThread(threading.Thread):
    def __init__(self, queue, flag):
        threading.Thread.__init__(self)
        self.queue = queue
        self.flag = flag

    def run(self):
        while True:
            domain = self.queue.get()

            if not os.path.isdir(base_dir):
                os.makedirs(base_dir)
            if self.flag == 'PULL':
                module_dir = module + '/' + domain
                # pull
                # rsync -rltpgoDz 1.1.1.1::app/123.com /data/app/
                CMD_SYNC = 'rsync -rltpgoDz ' + module_dir + ' ' + base_dir
                logging.info('[' + self.flag + '] ' + CMD_SYNC)
            elif self.flag == 'PUSH':
                # push
                # rsync -rltpgoDz /data/app/123.com 1.1.1.1::app
                data_dir = base_dir + '/' + domain
                CMD_SYNC = 'rsync -rltpgoDz ' + data_dir + ' ' + module
                logging.info('[' + self.flag + '] ' + CMD_SYNC)
            else:
                # push-all
                # domain_file
                # /data/app_new/abc.com
                # /data/app/123.com
                CMD_SYNC = 'rsync -rltpgoDz ' + domain + ' ' + module
                logging.info('[' + self.flag + '] ' + CMD_SYNC)
            status, _ = commands.getstatusoutput(CMD_SYNC)
            if status == 0:
                logging.info('[' + domain + ']' + ' Sync Complete !')
            self.queue.task_done()


def py_sync(domain_file, flag):
    queue = Queue.Queue()
    # threads = []
    with open(domain_file, 'r') as df:
        for domain in df:
            if domain.strip() == '':
                break
            queue.put(domain.rstrip('\n'))

    for it in range(thread_num):
        it = SyncThread(queue, flag)
        it.setDaemon(True)
        it.start()
        # threads.append(it)

    # for t in threads:
    #     t.join()
    queue.join()


'''
    flag:
    1. pull: rsync -rltpgoDz module/domain  base_dir
    2. push: rsync -rltpgoDz base_dir+domain  module
    3. ala:  else:
                # domain_file：
                # /data/app_new/abc.com
                # /data/app/123.com
             rsync -rltpgoDz $i module
'''

pull = 'PULL'
push = 'PUSH'
ala = 'ALL'

base_dir = ' /data/app/'
#module = '123.206.94.62::app'
module = '139.199.20.118::app'

# pyf : domain_file
if __name__ == '__main__':
    py_sync('pyf', pull)
