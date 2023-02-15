"""
异常捕获：出现异常后捕获到并继续执行代码，系统不会因为异常崩溃
try:
    预测会出现异常的代码
except:
    提示异常或异常解决代码


捕获指定的异常
try:
    预测会出现异常的代码
except NameError（异常名称） as e:（e为别名，保存异常信息）
    提示异常或异常解决代码


捕获多个异常
try:
    预测会出现异常的代码
except (异常名称1, 异常名称2) as e:（e为别名，保存异常信息）
    提示异常或异常解决代码


捕获所有异常
try:
    预测会出现异常的代码
except Exception as e:
    提示异常或异常解决代码


else/finally
try:
    预测会出现异常的代码
except:
    提示异常或异常解决代码
else:
    没有出现异常时执行代码
finally:
    不论有没有异常都要执行代码
"""

"""
异常传递：异常可以进行传递，比如函数嵌套调用
"""

"""
模块导入
import time（导入time.py文件的全部功能）
time.sleep(5)（调用时需要层级调用）

from time import sleep（导入time.py文件的sleep功能）
sleep(5)

import time as t（起别名）
t.sleep(5)
"""

"""
自定义模块导入
__main__变量：（控制模块中的部分代码在调用时不能执行，在模块中直接执行可以成功执行）
if __name__ = '__main__':（在自定义模块中执行时，name为main，在主模块中调用时name为模块名称）
    在模块中想要独立执行的代码
__all__变量：（为列表，在导入模块的全部功能时，调用的是__all__变量中的所有功能，模块中有的__all__变量没有的功能不能被导入）
from time import *
"""

"""
模块包：包含很多模块文件和一个__init__.py文件，如果没有__init__.py文件，只是一个文件夹
模块包导入
import 模块包.模块文件名   调用：模块包.模块文件名.功能名()
from 模块包 import 模块文件名   调用：模块文件名.功能名()
from 模块包.模块文件名 import 功能名   调用：功能名()
from 模块包 import * （在__init__.py文件中定义__all__变量，导入的所有功能只是__all__变量列表中的模块文件）
"""

"""
第三方包
终端安装第三方包（在线安装）：pip install 包名
网络优化：pip install -i https://pypi.tuna.tsinghua.edu.cn/simple 包名（清华大学镜像网）
pycharm安装第三方包：通过ctrl+alt+s进入项目设置页面，点击加号可以添加第三方包
ps：py文件名不能和第三方包名称一样，否则导入第三方包时调用的是.py文件
"""