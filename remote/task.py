from multiprocessing import Process
import os
import time

def run_proc(process_name):
    print('running subprocess %s(%s)......' % (process_name, os.getpid()))
    count = 100
    for i in range(count):
        print("*** {} ***".format(i))
        time.sleep(1)
    os.mkdir(str(count))
    print('sub process end')


if __name__ == '__main__':
    print('Process %s' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('sub process beginning')
    p.start()
    # p.join()
    # print('sub process end')
    print('Process end')
