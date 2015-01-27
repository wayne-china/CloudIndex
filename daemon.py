#-- coding=utf-8

import os
import sys


def daemonize(stdin='/dev/null',stdout= '/dev/null', stderr= 'dev/null'):
    '''Fork当前进程为守护进程，重定向标准文件描述符
        （默认情况下定向到/dev/null）
    '''
    #Perform first fork.
    try:
        pid = os.fork()
        if pid > 0:
            sys.exit(0)  #first parent out
    except OSError, e:
        sys.stderr.write("fork #1 failed: (%d) %s\n" %(e.errno, e.strerror))
        sys.exit(1)

    #从母体环境脱离
    os.chdir("/home/ec2-user/F2E.im")
    os.umask(0)
    os.setsid()
    #执行第二次fork
    try:
        pid = os.fork()
        if pid > 0:
            sys.exit(0) #second parent out
    except OSError, e:
        sys.stderr.write("fork #2 failed: (%d) %s]n" %(e.errno,e.strerror))
        sys.exit(1)

    #进程已经是守护进程了，重定向标准文件描述符
    for f in sys.stdout, sys.stderr: f.flush()
    si = file(stdin, 'r')
    so = file(stdout,'a+')
    se = file(stderr,'a+',0)
    os.dup2(si.fileno(), sys.stdin.fileno())
    os.dup2(so.fileno(), sys.stdout.fileno())
    os.dup2(se.fileno(), sys.stderr.fileno())

