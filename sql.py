"""
python语句操作MySQL数据库软件
需要使用第三方库：pymysql
pip install pymysql
"""
from pymysql import Connection
# 获取到MySQL数据库的链接对象
coon = Connection(
    host='localhost',   # 主机名（或IP地址）
    port=3306,      # 接口，默认3306
    user='root',    # 账户名
    password='123456'   # 密码
    # autocommit=True    # 默认提交，添加后在执行插入语句不需要commit()方法
)
# 打印MySQL数据库软件信息
print(coon.get_server_info())
# 获取游标对象
cursor = coon.cursor()
coon.select_db("数据库名")   # 选择数据库
# 使用游标对象，执行sql语句
cursor.execute("CREATE TABLE 表名(id int, info varchar(255))")
cursor.execute("select * from 表名")
results = cursor.fetchall()   # 获取结果，显示为元组形式
for r in results:
    print(r)
cursor.execute("insert into 表名(列名) values(值)")
# 插入语句需要进行确认
coon.commit()
# 关闭到数据库的连接
coon.close()