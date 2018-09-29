#!/usr/bin/env python
__author__ = 'ricksun'


import datetime
import psutil
import threading


CPU_PERCENT_INTERVAL = 1


class MyThread(threading.Thread):
    def __init__(self, func, args, name='', verb=False):
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args
        self.verb = verb
        self.res = None

    def get_result(self):
        return self.res

    def run(self):
        if self.verb:
            print 'starting', self.name, 'at:', datetime.datetime.now()
        self.res = self.func(*self.args)
        if self.verb:
            print self.name, 'finished at:', datetime.datetime.now()


def get_pro_res(pid):
    pro = psutil.Process(pid)
    cpu_perc = pro.cpu_percent(interval=CPU_PERCENT_INTERVAL)
    mem_byte = pro.memory_info().rss
    return cpu_perc, mem_byte


def process_monitor(pid_list):
    sys_cpu_list = []
    sys_memory_list = []
    pro_cpu_list = []
    pro_memory_list = []

    while True:
        # time.sleep(0.5)
        sys_cpu_ = psutil.cpu_percent()
        sys_cpu_list.append(sys_cpu_)
        # print "cpu: \033[1;31;42m%s%%\033[0m" % sys_cpu_
        # print "sys cpu: %.2f%%" % sys_cpu_
        memory = psutil.virtual_memory()
        # print memory.used
        # print memory.total
        sys_memory_ = float(memory.used) / float(memory.total) * 100
        sys_memory_list.append(sys_memory_)
        # print "sys mem: %.2f%%" % sys_memory_

        print datetime.datetime.now()
        threads = []
        for pid_ in pid_list:
            t = MyThread(get_pro_res, (pid_,), pid_.__str__())
            threads.append(t)

        for thread_ in threads:
            thread_.start()

        for thread_ in threads:
            thread_.join()

        pro_cpu_ = []
        pro_memory_ = []
        for thread_ in threads:
            pro_cpu_.append(thread_.get_result()[0])
            pro_memory_.append(thread_.get_result()[1])

        pro_cpu_list.append(pro_cpu_)
        print "pro cpu (perc):", pro_cpu_list

        pro_memory_list.append(pro_memory_)
        print "pro mem (byte):", pro_memory_list


if __name__ == '__main__':
    pid_list = [1623, 1483]
    process_monitor(pid_list)
