import datetime

import pytest
import logging

def test_not():
    print(1)

@pytest.mark.servername(server='my_server_name')
def test_function():
    print("111")


def print_html_table(data):
    # 构建HTML表格
    table = "<table>"
    for row in data:
        table += "<tr>"
        for cell in row:
            table += "<td>{}</td>".format(cell)
        table += "</tr>"
    table += "</table>"

    # 打印HTML表格
    print(table)

# 示例数据
data = [
    ['Header 1', 'Header 2', 'Header 3'],
    ['Value 1', 'Value 2', 'Value 3'],
    ['Value 4', 'Value 5', 'Value 6']
]

# 打印HTML表格

def test_addition():
    print_html_table(data)

def test_subtraction():
    print(12234)
    assert 5 - 3 == 2


if __name__ == "__main__":
    pytest.main(['-v','pytest_hook.py'  ,'--html=../Report/test_report_hook.html','--self-contained-html'])
