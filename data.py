'''
数据容器：列表list、元组tuple、字符串string、集合set、字典dict
'''

"""
列表（可以修改）
变量名称 = [元素, 元素2, 元素3...](元素可以是任意数据类型)

空列表
变量名称 = []
变量名称 = list()

通过索引取列表数据
变量名称 = 列表名称[0]（正向获取时索引从0开始递增，反向获取时索引从-1开始递减）
通过索引取嵌套列表数据
变量名称 = 列表名称[0][1]

列表常用操作
查找元素下标：list名.index(元素)
通过下标修改元素：list名[下标] = "元素值"
插入元素：list名.insert(下标, 元素)
元素追加：list名.append(元素)
容器追加：list名.extend(容器名称)
元素删除：del list名[下标]
移除取出元素：list名.pop(下标)
删除列表中第一个匹配的元素：list名.remove(元素)
清空列表内容：list名.clear()
统计元素在列表内数量：list名.count(元素)
统计列表长度：len(list名)
"""

"""
元组（不可以修改，元组内部的 列表元素可以修改）
变量名称 = (元素, 元素2, 元素3...)(元素可以是任意数据类型)
单个元素的元组定义：变量名称 = (元素,)

空元组
变量名称 = ()
变量名称 = tuple()

通过索引取元组数据
变量名称 = 元组名称[0]（正向获取时索引从0开始递增，反向获取时索引从-1开始递减）
通过索引取嵌套元组数据
变量名称 = 元组名称[0][1]

元组常用操作
查找元素下标：tuple名.index(元素)
统计元素在元组内数量：tuple名.count(元素)
统计元组长度：len(tuple名)
"""

"""
字符串（不可以修改）

通过索引取字符串数据
变量名称 = 字符串名称[0]（正向获取时索引从0开始递增，反向获取时索引从-1开始递减）

字符串常用操作
查找元素下标：string名.index(元素)
字符串替换：string名.replace(旧元素, 新元素)（替换后返回的是新的字符串，旧的字符串不能修改）
字符串分隔：string名.split(元素)（获取的是列表）
字符串规整：string名.strip()（不传入参数去除首尾空格，传入参数去除首尾参数）
统计元素在字符串内数量：string名.count(元素)
统计字符串长度：len(string名)
"""

"""
序列：列表、元组、字符串都算是序列
序列切片：序列名[起始位置:结束位置:步长]
ps：起始可省略，从头开始；结束可省略，到尾结束,取到结束位置的前一位；步长为1时可省略（步长为-1时倒序执行）
"""

"""
集合（无序不可以重复，允许修改）
变量名称 = {元素, 元素2, 元素3...}(元素可以是任意数据类型)

空集合
变量名称 = set()

集合常用操作
添加不存在的元素：set名.add(元素)
移除元素：set名.remove(元素)
随机取出元素：set名.pop()（原本的集合不存在取出的元素）
清空集合：set名.clear()
取两个集合的差集：set1名.difference(set2名)（获取集合1中集合2不存在的新集合）
消除2个集合差集：set1名.difference_update(set2名)（集合1消除和集合2相同的元素）
两个集合合并：set1名.union(set2名)
集合元素数量：len(set名)
集合可以用for进行遍历，while不可以因为不能用下标
"""

"""
字典（key不能重复，可以修改）
变量名称 = {key1: value1, key2: value2...}（key和value可以为任意数据类型，其中key不能是字典）

空字典
变量名称 = {}
变量名称 = dict()

字典基本操作
获取value值：dict名[key]
新增元素：dict名[key] = value（key在字典不存在）
更新元素：dict名[key] = value（key在字典存在）
删除元素：dict名.pop(key)
清除元素：dict名.clear()
获取所有的key：dict名.keys()
统计字典元素数量：len(dict名)
"""

"""
容器类型对比：
列表、元组、字符串支持索引，集合、字典不支持索引
列表、元组、字符串可存在重复数据，集合、字典不支持重复数据
元组、字符串不可修改，列表、集合、字典可以修改
通用操作：
len()、max()（取最大值，字符串比较字母，字典比较key值）、min()（取最小值，字符串比较字母，字典比较key值）
字符排序：通过字符对应的ASCII码值进行大小比较，字符串组合排序是通过对一位一位进行比较

list()、tuple()、str()、set()：所有数据容器转换不同类型

sorted(序列, [reserse = True])：进行排序，如果有[reserse = True]则是降序
"""

"""
json数据格式（json是用来做数据交互的，比如python语言和c语言进行交互，可以通过json语言交互）：字典/列表嵌套字典
json转换
import json（需要导入一个JSON包，调用JSON包中方法）
json.dumps(列表嵌套字典格式数据变量名, ensure_ascii=False)（ensure_ascii在数据有中文时设置为False，表示不根据ascii码编码）
json.loads(json数据变量)（JSON转换为python数据格式）
"""