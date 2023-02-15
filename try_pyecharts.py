"""
pyecharts是一个可视化模块包，需要先使用pip导入该包
"""

"""
使用pyecharts包生成折线图，可以进行全局配置选项设置、系列配置选项设置
"""

from pyecharts.charts import Line
from pyecharts.options import TitleOpts
Line = Line()
# 设置x轴
Line.add_xaxis(["中国", "美国", "英国"])
# 设置x轴
Line.add_yaxis("GDP", ["30", "20", "10"])
# 设置全局配置项
Line.set_global_opts(
    title_opts=TitleOpts
)

# 通过render方法将代码生成折线图，在当前目录下生成一个html文件，可以使用浏览器查看折线图
Line.render()


