# coding:utf-8
import os
import xlsxwriter
import platform
from pyecharts import Line
from pyecharts import Bar
from pyecharts_snapshot.main import make_a_snapshot
class excelReports():
    def GenerateXls(self):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        performance_data = os.path.join(base_dir, 'data')
        # workbook = xlsxwriter.Workbook(r"D:\moxiu\youyang\data\cl_sj.xlsx")
        workbook = xlsxwriter.Workbook('%s\\memory.xlsx' % (performance_data))
        cfile = ('%s\\memory_data.txt' % (performance_data))
        fp3 = open(cfile, "r")
        meminfo_data = fp3.readlines()
        new = []
        for i in range(len(meminfo_data)):
            d_list = []
            j = meminfo_data[i].replace('\n', '').split(',')
            d_list.append(j[0:1][0])
            values = j[1:4]
            for value in values:
                d_list.append(float(value))
            new.append(d_list)
        worksheet = workbook.add_worksheet('数据表')
        bold = workbook.add_format({'bold': 1})
        headings = [u'用例名称', 'heap_size', 'heap_alloc', 'heap_free']
        # 写入表头
        worksheet.write_row('A1', headings, bold)
        # 写入数据
        for j in range(len(new)):
            worksheet.write_row('A%d' % (j + 2), new[j])
        chart_col = workbook.add_chart({'type': 'line'})
        """
        设置线条的颜色值
        """
        chart_col.add_series({
            'name': 'heap_size',
            'categories': '=数据表!$A$2:$A$%d'% (len(new)+1),
            'values': '=数据表!$B$2:$B$%d'% (len(new)+1),
            'line': {'color': 'red'},
        })

        chart_col.add_series({
            'name': 'heap_alloc',
            'categories': '=数据表!$A$2:$A$%d'% (len(new)+1),
            'values': '=数据表!$C$2:$C$%d'% (len(new)+1),
            'line': {'color': 'green'},
        })

        chart_col.add_series({
            'name': 'heap_free',
            'categories': '=数据表!$A$2:$A$%d'% (len(new)+1),
            'values': '=数据表!$D$2:$D$%d'% (len(new)+1),
            'line': {'color': 'blue'},
        })

        # 设置图表的title 和 x，y轴信息
        chart_col.set_title({'name': u'有样主流程case内存数据图形报表'})
        chart_col.set_x_axis({'name': u'case名称'})
        chart_col.set_y_axis({'name': u'内存占用大小'})
        # 设置图表的风格
        chart_col.set_style(1)
        # 图表插入
        worksheet.insert_chart('A%d' % (len(new) + 10), chart_col, {'x_offset': 25, 'y_offset': 10})
        workbook.close()
        fp3.close()
if __name__=="__main__":
    a = excelReports()
    a.GenerateXls()
