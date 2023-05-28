import pytest
import datetime
from py.xml import html
@pytest.fixture(scope="session", autouse=True)
def timestamp():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]

@pytest.fixture(scope="function", autouse=True)
def test_steps(request, timestamp):
    test_steps_counter = 0
    test_steps_list = []

    def save_test_steps(action, expect, actual, result):
        nonlocal test_steps_counter
        test_steps_counter += 1
        test_step = {
            'Timestamps': timestamp,
            'TestSteps': test_steps_counter,
            'Action': action,
            'Expect': expect,
            'Actual': actual,
            'Result': result
        }
        test_steps_list.append(test_step)

    request.node.test_steps_list = test_steps_list
    yield save_test_steps

def pytest_html_results_table_header(cells):
    cells.insert(2, 'Timestamps')
    cells.insert(3, 'TestSteps')
    cells.insert(4, 'Action')
    cells.insert(5, 'Expect')
    cells.insert(6, 'Actual')
    cells.insert(7, 'Result')

def pytest_html_results_table_row(report, cells):
    if hasattr(report, 'test_steps_list'):
        test_steps = report.test_steps_list
        timestamps = '\n'.join([step['Timestamps'] for step in test_steps])
        test_steps = '\n'.join([str(step['TestSteps']) for step in test_steps])
        actions = '\n'.join([step['Action'] for step in test_steps])
        expects = '\n'.join([step['Expect'] for step in test_steps])
        actuals = '\n'.join([step['Actual'] for step in test_steps])
        results = '\n'.join([step['Result'] for step in test_steps])

        cells.insert(2, html.td(timestamps))
        cells.insert(3, html.td(test_steps))
        cells.insert(4, html.td(actions))
        cells.insert(5, html.td(expects))
        cells.insert(6, html.td(actuals))
        cells.insert(7, html.td(results))

def test_example(test_steps):
    test_steps("Action 1", "Expect 1", "Actual 1", "Pass")
    test_steps("Action 2", "Expect 2", "Actual 2", "Fail")

def test_another_example(test_steps):
    test_steps("Action 3", "Expect 3", "Actual 3", "Pass")
    test_steps("Action 4", "Expect 4", "Actual 4", "Pass")


if __name__ == "__main__":
    pytest.main(['-v','test_report4.py'  ,'--html=../Report/test_report.html','--self-contained-html'])
