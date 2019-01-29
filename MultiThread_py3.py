#!/usr/bin/env python

import threading
from time import sleep, ctime

action_list = ['A', 'B', 'C']


class MyThread(threading.Thread):
    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args

    def run(self):
        self.func(*self.args)


def action(name, nloop, nsec):
    print('start loop ', name, 'at:', ctime())
    for i in range(nloop):
        print('action ', name, 'at:', ctime())
        sleep(nsec)
    print('loop', name, 'done at:', ctime())


def main():
    print('starting at:', ctime())
    threads = []
    nloops = list(range(len(action_list)))

    for i in nloops:
        t = MyThread(action, (action_list[i], (i+1)*2, i+1), action.__name__)
        threads.append(t)

    for i in nloops:
        threads[i].start()

    for i in nloops:
        threads[i].join()

    print('all DONE at:', ctime())


if __name__ == '__main__':
    main()
