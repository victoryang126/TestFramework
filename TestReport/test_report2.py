import pytest
import datetime
from jinja2 import Template

@pytest.fixture(scope="session", autouse=True)
def timestamp():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]

@pytest.fixture(scope="function", autouse=True)
def test_steps(request, timestamp):
    test_steps_list = []

    def save_test_steps(action, expect_result, actual_result, result):
        test_step = {
            'Timestamps': timestamp,
            'Action': action,
            'ExpectResult': expect_result,
            'ActualResult': actual_result,
            'Result': result
        }
        test_steps_list.append(test_step)

    yield save_test_steps

    if hasattr(request.node, 'rep_extra'):
        request.node.rep_extra = {
            'test_steps': test_steps_list
        }

def pytest_html_report_title(report):
    report.title = "Custom Report"

def pytest_html_results_table_header(cells):
    cells.insert(2, "Timestamps")
    cells.insert(3, "Action")
    cells.insert(4, "ExpectResult")
    cells.insert(5, "ActualResult")
    cells.insert(6, "Result")

def pytest_html_results_table_row(report, cells):
    if hasattr(report, 'rep_extra'):
        test_steps = report.rep_extra.get('test_steps', [])
        cells.insert(2, '\n'.join([step['Timestamps'] for step in test_steps]))
        cells.insert(3, '\n'.join([step['Action'] for step in test_steps]))
        cells.insert(4, '\n'.join([step['ExpectResult'] for step in test_steps]))
        cells.insert(5, '\n'.join([step['ActualResult'] for step in test_steps]))
        cells.insert(6, '\n'.join([step['Result'] for step in test_steps]))

def pytest_configure(config):
    config.addinivalue_line(
        "markers", "test_steps(action, expect_result, actual_result, result): Add test steps information to the report"
    )

def pytest_html_report_html(report, config):
    template = Template(open("custom_report.html").read())
    report.extra = template.render(reports=[report])

def test_example(test_steps):
    test_steps("Action 1", "Expect 1", "Actual 1", "Pass")
    test_steps("Action 2", "Expect 2", "Actual 2", "Fail")

def test_another_example(test_steps):
    test_steps("Action 3", "Expect 3", "Actual 3", "Pass")
    test_steps("Action 4", "Expect 4", "Actual 4", "Pass")

if __name__ == "__main__":
    pytest.main(['-v','test_report2.py'  ,'--html=../Report/test_report.html','--self-contained-html'])
