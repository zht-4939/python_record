"""
闭包使用场景
无需定义全局变量即可实现通过函数持续访问修改某个值，有额外的内存占用
"""


"""
使用闭包实现ATM小案例
"""
def account_create(account_amount = 0):       # 定义外部函数
    def atm(num, deposit=True):           # 定义内部函数
        nonlocal account_amount           # 想要修改外部函数变量需要用nonlocal声明外部变量
        if deposit:
            account_amount += num
            print(f"存款，+{num}，账号余额：{account_amount}")
        else:
            account_amount -= num
            print(f"存款，-{num}，账号余额：{account_amount}")
    return atm                     # 外部函数返回内部函数

atm = account_create()              # atm返回值是内部函数

atm(100)            # 调用内部函数
atm(200)
atm(100, False)


"""
装饰器：
使用创建一个闭包函数，在闭包函数内调用目标函数，可以达到不改动目标函数的同时增加额外的功能
"""
"""
装饰器高级写法
"""
def outer(func):    # 定义外部函数，参数要传入目标函数名
    def inner():           # 定义内部函数
        print("我要睡觉了...")    # 修改目标函数代码
        func()            # 传入参数后调用目标函数
        print("我醒来了...")
    return inner       # 返回内部函数


def sleep():           # 定义目标函数
    import time
    import random
    print("睡眠中")
    time.sleep(random.randint(1, 5))

f1 = outer(sleep)
f1()

"""
装饰器高级写法
"""
def outer(func):    # 定义外部函数，参数为目标函数名
    def inner():           # 定义内部函数
        print("我要睡觉了...")    # 修改目标函数代码
        func()            # 调用目标函数
        print("我醒来了...")
    return inner       # 返回内部函数

@outer              # @outer装饰器，在执行目标函数时执行的是外部代码
def sleep():           # 定义目标函数
    import time
    import random
    print("睡眠中")
    time.sleep(random.randint(1, 5))

sleep()

"""
进程：程序在操作系统内运行，成为一个运行进程，进程之间内存格力
线程：进程内部有多个线程进行工作
并行执行：多任务并行执行（进程）、多线程并行执行
并行执行使用threading包
"""

import threading
import time
def sing():
    while True:
        print("唱歌")
        time.sleep(1)

def dance():
    while True:
        print("跳舞")
        time.sleep(1)

thread_sing = threading.Thread(target=sing)    # 创建线程对象，target传入的是执行目标任务名
thread_dance = threading.Thread(target=dance)

thread_sing.start()    # 线程执行
thread_dance.start()

"""
 正则表达式：使用正则表达式验证目标是否符合规则
"""