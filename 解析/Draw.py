from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.charts import Pie
from pyecharts.charts import Line
from pyecharts.charts import Graph
from pyecharts.charts import WordCloud
from pyecharts.commons.utils import JsCode
from pyecharts.charts import Radar
from pyecharts.charts import PictorialBar
from pyecharts.charts import EffectScatter
from pyecharts.globals import SymbolType
def rinse(lista):
    arrt = []
    value = []
    for i in range(20):
        arrt.append(lista[i][0])
        value.append(lista[i][1])
    return arrt,value
# 饼图
def drawpie(attr,value,name):
    list1 = [list(z) for z in zip(attr,value)]
    # 图表初始化配置
    init_opts = opts.InitOpts(page_title=name)

    pie = Pie(init_opts=init_opts)
    # 标题配置
    title = opts.TitleOpts(title=name,
                           pos_left='center')
    # 图例配置
    legend_opts = opts.LegendOpts(orient="vertical",
                                  pos_top="20%",
                                  pos_left="15%")

    # 工具箱配置
    # feature = opts.ToolBoxFeatureOpts(save_as_image=True, restore=True, data_view=True, data_zoom=True)
    # 工具箱配置
    toolbox_opts = opts.ToolboxOpts(orient="vertical",
                                    pos_top="25%",
                                    pos_right="15%"
                                    )

    pie.set_global_opts(title_opts=title,
                        legend_opts=legend_opts,
                        toolbox_opts=toolbox_opts
                        )
    # 标签配置项
    pie.add("",
            list1,
            radius=[30, 75],
            center=['50%', '70%'],
            rosetype="area",
            label_opts=opts.LabelOpts(
                position="outside",
                formatter="{b|{b}: }{c}  {per|{d}%}  ",
                background_color="#eee",
                border_color="#aaa",
                border_width=1,
                border_radius=4,
                rich={
                    "a": {"color": "#999", "lineHeight": 22, "align": "center"},
                    "abg": {
                        "backgroundColor": "#e3e3e3",
                        "width": "100%",
                        "align": "right",
                        "height": 22,
                        "borderRadius": [4, 4, 0, 0],
                    },
                    "hr": {
                        "borderColor": "#aaa",
                        "width": "100%",
                        "borderWidth": 0.5,
                        "height": 0,
                    },
                    "b": {"fontSize": 16, "lineHeight": 33},
                    "per": {
                        "color": "#eee",
                        "backgroundColor": "#334455",
                        "padding": [2, 4],
                        "borderRadius": 2,
                    },
                },
            ),

     )

    pie.render('{0}.html'.format(name))
# 趋势图
def drawline(arrt,value,name):

    # 图表初始化配置
    init_opts = opts.InitOpts(page_title=name)

    line = Line(init_opts=init_opts)
    # 标题配置
    title = opts.TitleOpts(title=name,
                           pos_left="10%")
    # 图例配置
    legend_opts = opts.LegendOpts(orient="horizontal",
                                  pos_top="5%",
                                  pos_right="15%")

    # 工具箱配置
    # feature = opts.ToolBoxFeatureOpts(save_as_image=True, restore=True, data_view=True, data_zoom=True)
    # 工具箱配置
    toolbox_opts = opts.ToolboxOpts(orient="vertical",
                                    pos_bottom="15%",
                                    pos_left="90%",
                                    )

    line.set_global_opts(title_opts=title,
                         legend_opts=legend_opts,
                         toolbox_opts=toolbox_opts,
                         datazoom_opts = opts.DataZoomOpts(orient="vertical"),
                         )
    line.add_xaxis(arrt, )
    line.add_yaxis(name, value, is_smooth=True, linestyle_opts=opts.LineStyleOpts(color="#E83132", width="4"))
    line.render('{0}.html'.format(name))
# 词云图
def drawWordCloud(words,name):
    # 图表初始化配置
    init_opts = opts.InitOpts(page_title=name)

    wc = WordCloud(init_opts=init_opts)
    # 标题配置
    title = opts.TitleOpts(title=name,
                           pos_left="50%")
    toolbox_opts = opts.ToolboxOpts(orient="vertical",
                                    pos_bottom="40%",
                                    pos_left="90%",
                                    )

    wc.set_global_opts(title_opts=title,
                       toolbox_opts=toolbox_opts,
                       )
    wc.add("",
           words,
           word_size_range=[20, 300],
           shape="diamond",
           textstyle_opts=opts.TextStyleOpts(font_family="cursive"),
           )
    wc.render("{0}.html".format(name))
# 柱状图
def drawbar(arrt,value,name):
    # 图表初始化配置
    init_opts = opts.InitOpts(page_title = name,
                              height="700px")
    bar = Bar(init_opts=init_opts)
    # 标题配置
    title = opts.TitleOpts(title=name,
                           pos_left='center')
    # 图例配置
    legend_opts = opts.LegendOpts(
                                  pos_top="5%",
                                  pos_left="15%")
    # 工具箱配置
    # feature = opts.ToolBoxFeatureOpts(save_as_image=True, restore=True, data_view=True, data_zoom=True)
    # 工具箱配置
    toolbox_opts = opts.ToolboxOpts(
                                    pos_top="5%",
                                    pos_right="30%"
                                    )
    bar.set_global_opts(title_opts=title,
                        legend_opts=legend_opts,
                        toolbox_opts=toolbox_opts,
                        # 区域缩放配置项
                        datazoom_opts=opts.DataZoomOpts(),
                        )

    # add_yaxis

    bar.add_xaxis(arrt)
    # 渐变色
    bar.add_yaxis("",
                  value,
                  gap="0%",
                  category_gap="30%",
                  # 自定义颜色
                  itemstyle_opts=opts.ItemStyleOpts(color=JsCode(
                      """new echarts.graphic.LinearGradient(0, 0, 1, 0,
                                              [{
                                                  offset: 0,
                                                  color: 'rgb(39, 117, 182)'
                                              },
                                              {
                                                  offset: 0.5,
                                                  color: 'rgb(147, 181,207)'
                                              },
                                              {
                                                  offset: 1,
                                                  color: 'rgb(35, 118, 183)'
                                              }], false)"""
                  )),
                  )
    bar.set_series_opts(
        label_opts=opts.LabelOpts(is_show=False),
        markline_opts=opts.MarkLineOpts(
            data=[
                opts.MarkLineItem(type_="min", name="最小值"),
                opts.MarkLineItem(type_="max", name="最大值"),
                opts.MarkLineItem(type_="average", name="平均值"),
            ]
        ),

        markpoint_opts=opts.MarkPointOpts(
            data=[
                opts.MarkPointItem(type_="max", name="最大值"),
                opts.MarkPointItem(type_="min", name="最小值"),
                opts.MarkPointItem(type_="average", name="平均值"),
            ]
        ),
    )
    bar.render('{0}.html'.format(name))
# 地图
def drawGraph(nodes,links,name):
    # 图表初始化配置
    init_opts = opts.InitOpts(page_title=name,
                              height="700px")
    g = Graph(init_opts=init_opts)
    # 标题配置
    title = opts.TitleOpts(title=name,
                           pos_left='center')
    # 图例配置
    legend_opts = opts.LegendOpts(
                                    pos_top="5%",
                                    pos_left="15%"
                                    )
    # 工具箱配置
    # 工具箱配置
    toolbox_opts = opts.ToolboxOpts()
    g.set_global_opts(title_opts=title,
                      legend_opts=legend_opts,
                      toolbox_opts=toolbox_opts,
                      )

    g.add("", nodes, links, repulsion=8000,linestyle_opts=opts.LineStyleOpts(curve=0.2),)
    g.render("{0}.html".format(name))
# 雷达图
def drawRadar(arr, value, valuemax, name):
    radar = Radar(init_opts=opts.InitOpts(width="1280px", height="720px", bg_color="#CCCCCC"))
    v_max = [list(z) for z in zip(arr, valuemax)]
    radar.add_schema(
        schema=[
            opts.RadarIndicatorItem(name=k, max_=v) for k, v in v_max
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
    # arr = ["销售（sales）", "管理（Administration）", "信息技术（Information Technology）", "客服（Customer Support）",
    #        "研发（Development）",
    #        "市场（Marketing）"]
    # value = [[4300, 10000, 28000, 35000, 50000, 19000]]
    # valuemax = [6500, 16000, 30000, 38000, 52000, 25000]
    # draw(arr, value, valuemax, "data/清华大学")
# 象形图
def drawPictorialBar(location,values,name):
    c = (
        PictorialBar()
        .add_xaxis(location)
        .add_yaxis(
            "",
            values,
            label_opts=opts.LabelOpts(is_show=False),
            symbol_size=22,
            symbol_repeat="fixed",
            symbol_offset=[0, -5],
            is_symbol_clip=True,
            # symbol='image://https://github.githubassets.com/images/spinners/octocat-spinner-32.gif'
            symbol='image://http://weizhendong.top/images/1.png'
        )
        .reversal_axis()
        .set_global_opts(
            title_opts=opts.TitleOpts(title=name),
            xaxis_opts=opts.AxisOpts(is_show=False),
            yaxis_opts=opts.AxisOpts(
                axistick_opts=opts.AxisTickOpts(is_show=False),
                axisline_opts=opts.AxisLineOpts(
                    linestyle_opts=opts.LineStyleOpts(opacity=0)
                ),
            ),
        )
        .render("{0}.html".format(name))
    )
# location = ["山西", "四川", "西藏", "北京", "上海", "内蒙古", "云南", "黑龙江", "广东", "福建"]
# values = [13, 42, 67, 81, 86, 94, 166, 220, 249, 262]
# drawPictorialBar(location,values,"llalal")

# 涟漪图
def drawEffectScatter(arr,value,name):
    c1 = EffectScatter()
    c1.add_xaxis(xaxis_data=arr)
    c1.add_yaxis(series_name=name,
                 y_axis=value,
                 # symbol='image://http://weizhendong.top/images/1.png',
                 symbol=SymbolType.ARROW,
                 # label_opts=opts.LabelOpts(is_show=False)
                 )
    c1.set_global_opts(
        title_opts=opts.TitleOpts(title=name),
        datazoom_opts=opts.DataZoomOpts(),
    )
    c1.render("{0}.html".format(name))