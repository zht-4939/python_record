"""
类和对象
创建类
class 类名:（类名首字母一般大写，大驼峰，多个单词时首字母都要大写）
    类的属性（成员变量）
    类的行为（成员方法）

创建类对象
对象 = 类名()（类的实例化）
对象名.属性 =
对象名.方法()

类内部的函数称为方法，类外部的函数称为函数
成员方法
def 函数名称(self, 形参1, 形参2...)
    方法体
self变量：在方法内部想要调用成员变量和成员方法必须使用self
"""

"""
魔术方法（python类的内置方法，__名称__是魔术方法的命名规范）

__init__构造方法：
def __init__(self, 参数1, 参数2...):（有在类中定义属性的功能，所以可以在类中不定义属性）
    self.属性1 = 参数1
    self.属性2 = 参数2
    ...
对象1 = 类名(参数1, 参数2...) （使用__init__快速构造方法可以快速设置对象属性）
使用场景：1、在类内部定义属性  2、实例化时快速传入对象的属性值

__str__字符串方法：
def __str__(self):
    return f"输出内容"
使用场景：1、print(对象名)，没有设置__str__时会返回对象所在内存地址，设置后返回的是__str__设置的返回值 
          2、print(str(对象名))，没有设置__str__时会返回对象所在内存地址，设置后返回的是__str__设置的返回值 

__lt__小于符号比较方法：
def __lt__(self, other):
    return self.属性名 < other.属性名
使用场景：比较两个对象时（print(对象名1 < 对象名2)），可以通过__lt__设置两个对象的比较内容

__le__小于等于符号比较方法：
def __le__(self, other):
    return self.属性名 <= other.属性名
使用场景：比较两个对象时（print(对象名1 <= 对象名2)），可以通过__le__设置两个对象的比较内容   

__eq__等于符号比较方法：
def __eq__(self, other):
    return self.属性名 == other.属性名
使用场景：比较两个对象时（print(对象名1 == 对象名2)），可以通过__lt__设置两个对象的比较内容
"""

"""
面向对象的三大特性：封装、继承、多态

封装（将现实事物在类中描述为属性和方法即为封装）
私有成员
现实事物有部分属性和行为是不公开对使用者开放的，这些属性和行为就是私有属性和私有行为，提供仅供内部使用的属性和方法
私有成员定义：__私有成员名称
类对象无法使用私有对象

继承
单继承
class 类名(父类名)
多继承
class 类名(父类名1, 父类名2...)
如果不同的父类有相同的属性名，则先继承的优先级最高，子类调用属性时显示的是先继承父类的属性
复写父类成员，直接在子类重新定义进行覆盖
子类内部调用父类成员：1、父类名称.属性名称/父类名称.方法名称(self) 2、super().属性名称/super().方法名称()

多态：同一个行为使用不同对象获得不同状态
如：定义函数，通过类型注解声明需要父类对象，实际传入子类对象进行工作，从而获得不同的工作状态
步骤：1、设计一个父类（制定标准，不需要有详细设计）2、设计多个子类（进行详细设计）
      3、定义函数，参数类型注解来源父类，调用父类方法4、多个子类实例化获取对象
      5、调用函数，参数为子类对象
抽象类：包含抽象方法的类，没有具体实现方法（pass）称之为抽象方法
"""

"""
类型注解：1、开发人员可以确认变量类型 2、开发工具可以确认变量类型并给出提示
变量类型注解（适用变量、容器、类：调用时对象类型为对应的类）
var: str = '123456'
list: list = [1, 2, 3]/list: list[int] = [1, 2, 3]
变量名: 类型 = 值/在注释中，# type:类型
var = '123456'  # type: str

函数类型注解：参数注解、返回值注解
def 函数名(参数1: 类型, 参数2: 类型...) -> 返回值类型: 

混合类型注解：使用Union包
list: list[Union[str, int]] = [1, 2, "123"]
"""

"""
设计模式：单例模式、工厂模式
单例模式指一个类只获取唯一的类实例对象，持续复用该对象，可以节省内存和创建对象的开销
class Str:
    pass

str1 = Str()     # 创建一个实例化对象，在其他.py文件调用时使用（from .py文件名 import str1）

工厂模式将对象的创建由使用原生类本身创建转换到特定的工厂方法来创建
class Factory:
    def 函数名(self, p_type):
        if p_type == 'w'
            return 类名1()
        elif p_type == 'r'
            return 类名2()

"""