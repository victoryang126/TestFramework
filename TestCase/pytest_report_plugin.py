import datetime
import pytest
from _pytest.runner import TestReport
from _pytest.config import hookimpl

@pytest.hookimpl(tryfirst=True)
def pytest_runtest_protocol(item, nextitem):
    item.session.results[item.nodeid] = CustomTestReport()
    return None

@pytest.hookimpl(tryfirst=True)
def pytest_runtest_logreport(report):
    if report.when == 'call':
        report_timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        report.test_metadata = {
            'Timestamps': report_timestamp,
            'TestSteps': report.nodeid,
            'ExpectResult': report.keywords.get('expect_result', ''),
            'ActualResult': report.keywords.get('actual_result', ''),
            'Result': report.outcome
        }
    return None

class CustomTestReport(TestReport):
    pass
