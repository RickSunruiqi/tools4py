#!/usr/bin/env python
__author__ = 'ricksun'


import time
import datetime
import psutil
import threading


def process_monitor(pid_list):
    sys_cpu_list = []
    sys_memory_list = []
    pro_cpu_list = []
    pro_memory_list = []

    while True:
        time.sleep(0.5)
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
        # pro = psutil.pids()
        # # print(pro)

        print datetime.datetime.now()
        pro_cpu_, pro_memory_ = get_pro_res_2(pid_list)
        # print "pro cpu: %.2f%%" % pro_cpu_[0]
        pro_cpu_list.append(pro_cpu_)
        print "pro cpu (perc):", pro_cpu_list
        # p = psutil.Process(pid_list[0])
        # pro_memory_ = p.memory_percent()
        # print "pro mem: %.2f%%" % pro_memory_
        pro_memory_list.append(pro_memory_)
        print "pro mem (byte):", pro_memory_list


def get_pro_res_2(pid_list):
    processes = [psutil.Process(pid=i) for i in pid_list]
    cpu_perc = [p.cpu_percent(interval=0.5) for p in processes]
    # mem_perc = [p.memory_percent() for p in processes]
    mem_byte = [p.memory_info().rss for p in processes]
    return cpu_perc, mem_byte


def get_pro_res(pid):
    pro = psutil.Process(pid)
    cpu_perc = pro.cpu_percent(interval=0.5)
    mem_byte = pro.memory_info().rss
    return cpu_perc, mem_byte


if __name__ == '__main__':
    process_monitor([1,2)
