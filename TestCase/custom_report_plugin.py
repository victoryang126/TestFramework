# from pytest_html import html
from _pytest.config import Config

def pytest_html_results_table_header(cells):
    cells.insert(0, 'Timestamps')
    cells.insert(1, 'TestSteps')
    cells.insert(2, 'ExpectResult')
    cells.insert(3, 'ActualResult')
    cells.insert(4, 'Result')

def pytest_html_results_table_row(report, cells):
    cells.insert(0, report.timestamp)
    cells.insert(1, report.test_steps)
    cells.insert(2, report.expect_result)
    cells.insert(3, report.actual_result)
    cells.insert(4, report.result)

