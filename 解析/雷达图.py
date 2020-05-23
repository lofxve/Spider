import pyecharts.options as opts
from pyecharts.charts import Radar

"""
Gallery 使用 pyecharts 1.1.0
参考地址: https://echarts.baidu.com/examples/editor.html?c=radar

目前无法实现的功能:

1、雷达图周围的图例的 textStyle 暂时无法设置背景颜色
"""
arr=["销售（sales）", "管理（Administration）", "信息技术（Information Technology）", "客服（Customer Support）", "研发（Development）", "市场（Marketing）"]
value = [[4300, 10000, 28000, 35000, 50000, 19000]]
valuemax =[6500, 16000, 30000, 38000, 52000, 25000]

def draw(arr,value,valuemax,name):
    radar=Radar(init_opts=opts.InitOpts(width="1280px", height="720px", bg_color="#CCCCCC"))
    v_max=[list(z)for z in zip(arr,valuemax)]
    radar.add_schema(
        schema=[
            opts.RadarIndicatorItem(name=k, max_=v)for k,v in v_max
        ],
        splitarea_opt=opts.SplitAreaOpts(
            is_show=True, areastyle_opts=opts.AreaStyleOpts(opacity=1)
        ),
        textstyle_opts=opts.TextStyleOpts(color="#fff"),
    )
    radar.add(
        series_name=name,
        data=value,
        linestyle_opts=opts.LineStyleOpts(color="#CD0000"),
    )
    radar.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    radar.set_global_opts(
        title_opts=opts.TitleOpts(title=name), legend_opts=opts.LegendOpts()
    )
    radar.render("{0}.html".format(name))
draw(arr,value,valuemax,"data/清华大学")