# import pytest
# from datetime import datetime
# from py.xml import html
#
# # 初始化测试报告
# report_rows = []
#
# # 添加一行数据到测试报告
# def add_row_to_report(test_step, action, expect_result, actual_result, result):
#     now = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
#     row = (now, test_step, action, expect_result, actual_result, result)
#     report_rows.append(row)
#
#
# # 生成测试报告
# @pytest.mark.hookwrapper
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     rep = outcome.get_result()
#     if rep.when == "call":
#         if rep.failed:
#             result = "失败"
#         else:
#             result = "通过"
#         add_row_to_report(None, None, None, None, result)
#
# # 生成HTML测试报告
# @pytest.mark.hookwrapper
# def pytest_html_results_table_header(cells):
#     cells.insert(0, html.th("Timestamps"))
#     cells.append(html.th("Timestamps"))
#
# @pytest.mark.hookwrapper
# def pytest_html_results_table_row(report, cells):
#     cells.insert(0, html.td(report.when))
#     cells.append(html.td(report.when))
#
# @pytest.mark.hookwrapper
# def pytest_html_results_table_footer(cells):
#     pass
#
# # 生成测试报告文件
# @pytest.mark.hookwrapper
# def pytest_terminal_summary(terminalreporter, exitstatus, config):
#     if report_rows:
#         headers = ["Timestamps", "TestSteps", "Action", "ExpectResult", "ActualResult", "Result"]
#         rows = [headers] + report_rows
#         html_table = html.table(
#             [html.tr([html.th(cell) for cell in row]) for row in rows[1:]],
#             [html.tr([html.td(cell) for cell in row]) for row in rows[1:]]
#         )
#         with open("test_report.html", "w") as f:
#             f.write(html.html(
#                 html.head(html.title("Test Report")),
#                 html.body(html_table)
#             ))
