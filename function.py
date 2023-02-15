"""
print()
print(内容, 内容2, ...)   eg: print("输入内容为：", 10, 变量名)
print("字符串1", end='')  输出内容后不换行
print()   换行

input()
str = input("字符串1：")   ps：input()获取数据是字符串类型数据

random随机函数使用
import random
random.randint(num1, num2)   获取从num1到num2的随机数

range()序列函数使用
range(num2)   表示获取从0开始到num2的序列数，不包含num2
range(num1, num2)     表示获取从num1开始到num2的序列数，不包含num2
range(num1, num2, step)     表示获取从num1开始到num2，步长为step的序列数，不包含num2
"""

"""
函数定义：
def 函数名(传入参数):
    函数体
    return
函数调用：
函数名(参数)
进入函数代码：ctrl+鼠标左键
"""

"""
函数参数：
函数定义时的参数是形参
函数调用时的参数是实参
函数多种参数：
位置参数（实参根据位置分别传参给形参）
关键字参数（在调用函数时传参指定形参：函数名(参数1="", 参数2=""... )）
不定长参数（不确认）
def 函数名(*args):（调用函数时传参可以通过位置参数传任意多个参数，传入的参数以元组形式组成）
    函数体
def 函数名(**kwargs):（调用函数时传参可以通过关键字参数传任意多个参数，传入的参数以字典形式组成）
    函数体
缺省参数（在定义函数时，给形参传入参数，该形参设置了默认值，设置的默认值参数要放到最后）
函数作为参数传递
def 函数名1(函数名2):（定义函数时，参数为另一函数，传入的是计算逻辑；函数嵌套是在函数内部调用另一函数）
    a = 函数名2(参数1, 参数2)
函数名1(函数名2)
"""

"""
函数返回值：
return 变量名1, 变量名2, 变量名3...（多返回值） 
函数没有规定返回值时，返回值是None
"""

"""
函数说明文档：
在函数体前用使用多行注释，可以写明参数含义
函数嵌套调用
"""

"""
函数变量
局部变量：在函数内部定义的变量是局部变量，函数执行后局部变量释放
全局变量：在函数外部定义的变量是全局变量，函数可以使用全局变量
函数内部修改全局变量：使用global关键字（global 变量名），声明后可以修改全局变量
"""

"""
匿名函数（无名称，只能临时调用一次）
lambda x, y（形参）: 函数体（只能一行）
"""



