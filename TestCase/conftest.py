import pytest
from datetime import datetime


@pytest.fixture(scope='session')
def timestamp():
    """
    返回当前时间的字符串表示，精确到毫秒。
    """
    now = datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]


@pytest.fixture(scope='function')
def test_step(request):
    """
    用于记录测试步骤的计数器。
    """
    if not hasattr(request, 'session_step'):
        request.session_step = 1
    else:
        request.session_step += 1

    return request.session_step


def pytest_html_results_table_header(cells):
    """
    在HTML报告中添加自定义表头
    """
    cells.insert(0, 'Timestamps')
    cells.insert(1, 'TestSteps')
    cells.insert(2, 'Action')
    cells.insert(3, 'ExpectResult')
    cells.insert(4, 'ActualResult')
    cells.insert(5, 'Result')


def pytest_html_results_table_row(report, cells):
    """
    在HTML报告中添加自定义表格行
    """
    test_step = getattr(report, 'test_step', '-')
    action = getattr(report, 'action', '-')
    expect_result = getattr(report, 'expect_result', '-')
    actual_result = getattr(report, 'actual_result', '-')
    result = getattr(report, 'result', '-')
    timestamp = getattr(report, 'timestamp', '-')

    cells.insert(0, str(timestamp))
    cells.insert(1, str(test_step))
    cells.insert(2, str(action))
    cells.insert(3, str(expect_result))
    cells.insert(4, str(actual_result))
    cells.insert(5, str(result))


def pytest_runtest_protocol(item, nextitem):
    """
    Pytest hook implementation to capture test reports and add custom information.
    """
    item.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
    item.test_step = getattr(item.function, 'test_step', None)
    item.action = getattr(item.function, 'action', None)
    item.expect_result = getattr(item.function, 'expect_result', None)
    item.actual_result = getattr(item.function, 'actual_result', None)
    return None


def pytest_html_report_title(report):
    """
    在HTML报告中添加自定义标题
    """
    report.title = "自定义测试报告"
