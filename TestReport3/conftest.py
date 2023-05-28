import socket
import getpass
import pytest
from datetime import datetime
from py.xml import html

@pytest.mark.optionalhook
def pytest_html_results_table_header(cells):
    cells.insert(1, html.th('Server Name', class_='sortable server-name', col='server-name'))


@pytest.mark.optionalhook
def pytest_html_results_table_row(report, cells):
    cells.insert(1, html.td(report.server_name, class_='col-server-name'))


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    report.server_name = item.keywords['servername'].kwargs['server']