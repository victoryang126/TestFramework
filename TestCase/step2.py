import pytest
import datetime
test_step = 0
@pytest.fixture(scope="function")
def timestamp():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")


@pytest.mark.parametrize("input, expected", [("input1", "expected1"), ("input2", "expected2")])
def test_example(input, expected, timestamp):
    global test_step

    # 模拟执行测试步骤
    action = f"Action for test step {test_step}"
    result = "PASS" if input == expected else "FAIL"
    actual_result = f"Actual result for test step {test_step}"

    # 构建测试结果的 HTML 表格行
    test_data = [
        timestamp,
        test_step,
        action,
        expected,
        actual_result,
        result,
        timestamp
    ]

    # 递增 test_step
    test_step += 1

    # 断言检查
    assert input == expected, f"Input: {input}, Expected: {expected}"

    # 返回测试数据
    return test_data


if __name__ == "__main__":
    pytest.main(['-v','step2.py'  ,'--html=step2.html','--self-contained-html'])
