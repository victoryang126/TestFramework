import pytest
from pytest_html import extras
import datetime

# def test_step(action,expect_result,actual_result,result):
#     timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
#     test_step = {
#         'Timestamps': timestamp,
#         'Step': 0,
#         'Action': action,
#         'ExpectResult': expect_result,
#         'ActualResult': actual_result,
#         'Result': result
#     }
#     test_steps_list.append(test_step)

@pytest.mark.parametrize("input, expected", [("input1", "input1"), ("input2", "expected2")])
def test_example(input, expected):
    pass
    # 执行测试步骤
    # print(input,expected)
    # 添加自定义 HTML 内容
    # extra_html = extras.html('<div>Additional HTML</div>')
    # request.node.report.extra_html.append(extra_html)

    # 断言检查
    # assert input == expected, "Test failed"

# def test_extra(extra):
#     extra.append(extras.html("""<td>2023-05-27 15:30:22.123</td>
#     <td>1</td>
#     <td>Click button</td>
#     <td>Button is visible</td>
#     <td>Button is visible</td>
#     <td>PASS</td>"""))
def test_example(test_steps):
    test_steps("Action 1", "Expect 1", "Actual 1", "Pass")
    test_steps("Action 2", "Expect 2", "Actual 2", "Fail")

def test_another_example(test_steps):
    test_steps("Action 3", "Expect 3", "Actual 3", "Pass")
    test_steps("Action 4", "Expect 4", "Actual 4", "Pass")
# def test_another_example2(test_step):
#     test_step("Action 3", "Expect 3", "Actual 3", "Pass")
#     test_step("Action 4", "Expect 4", "Actual 4", "Pass")
if __name__ == "__main__":
    pytest.main(['-vs','step.py' ,'--html=step.html','--self-contained-html'
                 ])
