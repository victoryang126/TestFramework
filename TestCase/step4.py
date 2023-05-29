import pytest

# def test_example(timestamp, test_step):
#     # 执行测试步骤
#     action = "执行动作"
#     expect_result = "期望结果"
#     actual_result = "实际结果"
#     result = "通过"
#
#     # 获取当前时间戳
#     current_timestamp = timestamp
#
#     # 在报告中显示测试步骤的信息
#     print_test_step(test_step, action, expect_result, actual_result, result, current_timestamp)
#
#     assert result == "通过"
#
#
# def print_test_step(step, action, expect_result, actual_result, result, timestamp):
#     """
#     打印测试步骤的信息。
#     """
#     print(f"Test Step: {step}")
#     print(f"Action: {action}")
#     print(f"Expect Result: {expect_result}")
#     print(f"Actual Result: {actual_result}")
#     print(f"Result: {result}")
#     print(f"Timestamp: {timestamp}")
#
#
# import pytest
#
#
# @pytest.mark.parametrize("action, expect_result, actual_result, result", [
#     ("执行动作1", "期望结果1", "实际结果1", "通过"),
#     ("执行动作2", "期望结果2", "实际结果2", "通过"),
# ])
# def test_example(timestamp, test_step, action, expect_result, actual_result, result):
#     # 获取当前时间戳
#     current_timestamp = timestamp
#
#     # 在报告中显示测试步骤的信息
#     print_test_step(test_step, action, expect_result, actual_result, result, current_timestamp)
#
#     assert result == "通过"
#
#
# def print_test_step(step, action, expect_result, actual_result, result, timestamp):
#     """
#     打印测试步骤的信息。
#     """
#     table_row = f"<tr><td>{step}</td><td>{action}</td><td>{expect_result}</td><td>{actual_result}</td><td>{result}</td><td>{timestamp}</td></tr>"
#     pytest_html = pytest.config.pluginmanager.getplugin("html")
#     pytest_html._add_html(pytest_html.extras.table([table_row], ['Test Steps', 'Action', 'Expect Result', 'Actual Result', 'Result', 'Timestamps']))

def test_example(timestamp, test_step):
    # 执行测试步骤
    action = "执行动作"
    expect_result = "期望结果"
    actual_result = "实际结果"
    result = "通过"

    # 获取当前时间戳
    current_timestamp = timestamp

    # 在报告中显示测试步骤的信息
    print_test_step(test_step, action, expect_result, actual_result, result, current_timestamp)

    assert result == "通过"


def print_test_step(step, action, expect_result, actual_result, result, timestamp):
    """
    打印测试步骤的信息。
    """
    print(f"Test Step: {step}")
    print(f"Action: {action}")
    print(f"Expect Result: {expect_result}")
    print(f"Actual Result: {actual_result}")
    print(f"Result: {result}")
    print(f"Timestamp: {timestamp}")


if __name__ == "__main__":
    pytest.main(['-v','step4.py'  ,'--html=step4.html','--self-contained-html'])