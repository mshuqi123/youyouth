# coding:utf-8
import os
import xlsxwriter,time
import platform
from pyecharts import Line
from PIL import Image
from pyecharts_snapshot.main import make_a_snapshot
from pyecharts import Bar
from pyecharts_snapshot.main import make_a_snapshot
class GenerateReport():
    @staticmethod
    def get_mem_data():
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        performance_data = os.path.join(base_dir, 'data')
        image_path = performance_data + "\\result.png"
        html_path = "%s\\memory_report.html" % (performance_data)
        hfile = ('%s\\memory_data.txt' % (performance_data))
        fp = open(hfile, "r")
        # fp = open(r'D:\moxiu\youyang\data\xin.txt', 'r')
        meminfo_data = fp.readlines()
        case_name_list = []
        for i in range(len(meminfo_data)):
            j = meminfo_data[i].replace('\n', '').split(',')
            case_name_list.append(j[0:1][0])
        heap_size_list = []
        for i in range(len(meminfo_data)):
            j = meminfo_data[i].replace('\n', '').split(',')
            heap_size_list.append(float(j[1:2][0]))
        heap_alloc_list = []
        for i in range(len(meminfo_data)):
            j = meminfo_data[i].replace('\n', '').split(',')
            heap_alloc_list.append(float(j[2:3][0]))
        heap_free_list = []
        for i in range(len(meminfo_data)):
            j = meminfo_data[i].replace('\n', '').split(',')
            heap_free_list.append(float(j[3:4][0]))
        bar = Line("有样__内存数据图形报表", "图表纵轴为数据大小，横轴为case名称，直线为平均值")
        bar.add("heap_size", case_name_list, heap_size_list, label_color=['#B22222'], mark_line=["average"],
                mark_point=["max", "min"], xaxis_interval=0, xaxis_rotate=90)
        bar.add("heap_alloc", case_name_list, heap_alloc_list, label_color=['#008080'], mark_line=["average"],
                mark_point=["max", "min"], xaxis_interval=0, xaxis_rotate=90)
        bar.add("heap_free", case_name_list, heap_free_list, label_color=['#483D8B'], mark_line=["average"],
                mark_point=["max", "min"], xaxis_interval=0, xaxis_rotate=90)
        bar.use_theme("vintage")
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        performance_data = os.path.join(base_dir, 'data')
        bar.render('%s\\memory_report.html' % (performance_data))
        make_a_snapshot(html_path,image_path)
        im = Image.open(image_path)
        out = im.resize((800, 400), Image.ANTIALIAS)
        out.save(image_path)
if __name__=="__main__":
    GenerateReport.get_mem_data()
