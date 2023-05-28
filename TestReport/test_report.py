
from prettytable import PrettyTable
import pytest
import datetime


@pytest.fixture(scope="session", autouse=True)
def timestamp():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]

@pytest.fixture(scope="function", autouse=True)
def test_steps(request, timestamp):
    test_table = PrettyTable()
    test_table.field_names = ['Timestamps', 'Step', 'Action', 'ExpectResult', 'ActualResult', 'Result']
    count = 1  # 步骤计数器

    def save_test_steps(action, expect_result, actual_result, result):
        nonlocal count  # 使用非本地变量
        test_step = {
            'Timestamps': timestamp,
            'Step': count,
            'Action': action,
            'ExpectResult': expect_result,
            'ActualResult': actual_result,
            'Result': result
        }
        count += 1  # 计数器递增
        test_table.add_row(test_step.values())
        request.node.test_table = test_table

    yield save_test_steps

    if hasattr(request.node, 'test_table'):
        test_table = request.node.test_table
        print(test_table)

"""
请帮我用pytest搭建一个测试框架，需要在报告里面的每个TestCase下显示Timestamps TestSteps,Action Expect, Actual,Result,Timestamps 用函数获取当前的时间，具体到ms，TestSteps 需要是数字递增显示
"""
def test_example(test_steps):
    test_steps("Action 1", "Expect 1", "Actual 1", "Pass")
    print("This is a test")
    test_steps("Action 2", "Expect 2", "Actual 2", "Fail")

def test_another_example(test_steps):
    test_steps("Action 3", "Expect 3", "Actual 3", "Pass")
    test_steps("Action 4", "Expect 4", "Actual 4", "Pass")
    # assert result == 'Failed'
if __name__ == "__main__":
    pytest.main(['-v','test_report.py'  ,'--html=../Report/test_report.html','--self-contained-html'])
