import pytest
from _pytest.runner import TestReport


@pytest.hookimpl(tryfirst=True)
def pytest_runtest_makereport(item, call):
    """
    Pytest hook implementation to capture test reports and add custom information.
    """
    # 调用原始的测试报告生成函数
    report = pytest.hook.pytest_runtest_makereport(item=item, call=call)

    # 检查测试用例的执行结果是否为“failed”或“error”
    if report.when == 'call' and (report.failed or report.skipped or report.outcome == 'error'):
        # 获取测试用例的输出信息
        captured_output = call.get_report_log()

        # 添加自定义信息到报告中
        report.sections.append(('Captured Output', format_output_table(captured_output)))

    return report


def format_output_table(output):
    """
    Format captured output as an HTML table.
    """
    if output:
        # 创建HTML表格的头部
        table_html = '<table>'
        table_html += '<tr><th>Output</th></tr>'

        # 添加每行输出作为表格的行
        for line in output.split('\n'):
            table_html += f'<tr><td>{line}</td></tr>'

        # 关闭HTML表格
        table_html += '</table>'

        return table_html

    return ''


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
    cells.insert(0, 'Test Steps')


def pytest_html_results_table_row(report, cells):
    """
    在HTML报告中添加自定义表格行
    """
    if "test_step" in report.keywords:
        cells.insert(0, str(report.keywords["test_step"]))
    else:
        cells.insert(0, "-")


def pytest_html_results_table_html(report, data):
    """
    在HTML报告中添加自定义表格
    """
    if report.passed:
        del data[:]


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):
    """
    Pytest hook implementation to capture test reports and add custom information.
    """
    outcome = yield
    report = outcome.get_result()

    if report.when == 'call':
        if hasattr(report, 'keywords') and 'test_step' in report.keywords:
            report.keywords['test_step'] = report.keywords['test_step'].args[0]


def pytest_html_report_title(report):
    """
    在HTML报告中添加自定义标题
    """
    report.title = "自定义测试报告"


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

def test_example(timestamp, test_step):
    # 执行测试步骤
    action = "执行动作"
    expect_result = "期望结果"
    actual_result = "实际结果"
    result = "通过"

    # 在报告中显示测试步骤的信息
    print_test_step(test_step, action, expect_result, actual_result, result, timestamp)

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



import pytest
from datetime import datetime
from py.xml import html

import pytest
import datetime


def generate_html_table(data):
    html = '''
        <p>
        <style>
             table {
              border-collapse: collapse;
              width: 100%;
              background-color: #f2f2f2;
           }

            th, td {
              border: 1px solid #ddd;
              padding: 8px;
              text-align: left;
           }

           #test_steps th {
              #background-color: #FFF5EE;
              color: #000000;
           }

           tr.pass {
              background-color: #c9ecc9;
           }

           tr.fail {
              background-color: #f8caca;
           }

           tr.tbd {
              background-color: #fdfdc4;
           }
        </style>
        <table id="test_steps">
          <tr>
            <th>Timestamps</th>
            <th>TestSteps</th>
            <th>Action</th>
            <th>Expect</th>
            <th>Actual</th>
            <th>Result</th>
          </tr>
    '''

    for item in data:
        html += f'''
            <tr class="{item['result'].lower()}">
                <td>{item['timestamps']}</td>
                <td>{item['teststeps']}</td>
                <td>{item['action']}</td>
                <td>{item['expect']}</td>
                <td>{item['actual']}</td>
                <td>{item['result']}</td>
            </tr>
        '''

    html += '''
        </table>
        </p>
    '''

    return html


@pytest.fixture(scope='session')
def timestamp():
    def get_timestamp():
        return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
    return get_timestamp


@pytest.fixture(scope='function')
def teststep(request):
    def get_teststep():
        if 'teststep' not in request.session:
            request.session['teststep'] = 1
        else:
            request.session['teststep'] += 1
        return request.session['teststep']
    return get_teststep


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call':
        timestamp_value = item.funcargs['timestamp']()
        teststep_value = item.funcargs['teststep']()
        extra.append(('Timestamps', timestamp_value))
        extra.append(('TestSteps', teststep_value))
        extra.append(('Action', item.function.__name__))
        extra.append(('Expect', 'Expectation Value'))
        extra.append(('Actual', 'Actual Value'))
        extra.append(('Result', report.outcome.capitalize()))
        report.extra = extra


@pytest.mark.html
def test_case_example(timestamp, teststep):
    assert 1 + 1 == 2


@pytest.mark.html
def test_case_another_example(timestamp, teststep):
    assert 2 * 2 == 4





if __name__ == "__main__":
    pytest.main(['-v','test_report.py','--html=test_report.html'])
