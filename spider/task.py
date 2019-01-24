import sched
import os
import time

schedule = sched.scheduler(time.time,time.sleep)

def execute_command(cmd, inc):
    print('执行程序')
    os.system(cmd)
    schedule.enter(inc, 0, execute_command, (cmd, inc))

def main(cmd, inc):
    schedule.enter(0, 0, execute_command, (cmd, inc))
    schedule.run()

if __name__ == '__main__':
    main('netstat -an',20) 