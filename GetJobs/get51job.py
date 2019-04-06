# @File    : get51job.py
# @Date    : 2019-04-06
# @Author  : shengjia

import urllib
import re
import io
import xlwt


# get code
def get_content(page):
    url = 'http://search.51job.com/list/000000,000000,0000,00,9,99,php,2,' + str(page) + '.html'
    a = urllib.urlopen(url)  # open website
    html = a.read().decode('gbk')  # read code and transfer unicode
    return html


def get(html):
    reg = re.compile(
        r'class="t1 ">.*? <a target="_blank" title="(.*?)".*? <span class="t2"><a target="_blank" title="(.*?)".*?<span class="t3">(.*?)</span>.*?<span class="t4">(.*?)</span>.*? <span class="t5">(.*?)</span>',
        re.S)
    items = re.findall(reg, html)
    return items


def excel_write(items, index):
    for item in items:
        for i in range(0, 5):
            ws.write(index, i, item[i])

        print(index)
        index += 1


newTable = "test.xls"
wb = xlwt.Workbook(encoding='utf-8')
ws = wb.add_sheet('sheet1')
headData = ['Position', 'Company', 'Address', 'Salary', 'Date']
for colnum in range(0, 5):
    ws.write(0, colnum, headData[colnum], xlwt.easyxf('font:bold on'))

for each in range(1, 10):
    index = (each - 1) * 50 + 1
    excel_write(get(get_content(each)), index)

wb.save(newTable)

