import xlrd
import xlwt
from xlutils.copy import copy
class Operatingexcel():
    def get_excel_dic(self,filename,sheetname):
        # filename 文件名
        # sheetname 表单名
        # 返回字典格式
        dic = {}
        data = xlrd.open_workbook(filename, 'r', encoding_override='utf-8')
        table = data.sheet_by_name(sheetname)
        for i in range(1, table.nrows):
            for y in range(len(table.row_values(0))):
                if table.row_values(i)[y] != "":
                    dic.setdefault(table.row_values(0)[y], []).append(table.row_values(i)[y])
        return dic

    def get_excel_list(self,filename,sheetname):
        # filename 文件名
        # sheetname 表单名
        # 返回列表格式
        list = []
        data = xlrd.open_workbook(filename, 'r', encoding_override='utf-8')
        table = data.sheet_by_name(sheetname)
        for y in range(table.nrows):
            for x in range(len(table.row_values(0))):
                if table.row_values(y)[x] != "":
                    list.append(table.row_values(y)[x])
        return list

    def set_excel_dic(self,dic,filename,sheet_index,start_r):
        # filename 文件名
        # sheet_index第几个工作表格
        # start_r那一列

        x = start_r
        for k in dic.keys():
            list = []
            list.append(k)
            for v in dic[k]:
                list.append(v)
            self.set_excel_list(list,filename,sheet_index,x)
            x = x + 1

    def set_excel_list(self,list,filename,sheet_index,start_r):
        # filename 文件名
        # sheet_index第几个工作表格
        # start_r那一列

        # 读取excel文件
        r_xls = xlrd.open_workbook(filename)
        # 将xlrd的对象转化为xlwt的对象
        excel = copy(r_xls)
        table = excel.get_sheet(sheet_index)
        for y in range(len(list)):
            if str(list[y]).split() !="":
                table.write(y,start_r,str(list[y]).split())
            else:
                continue
        excel.save(filename)