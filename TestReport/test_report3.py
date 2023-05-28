import pytest
import datetime
from HTMLTable import HTMLTable
# 定义一个全局变量，用于存储测试步骤信息
test_steps_list = []

@pytest.fixture(scope="session", autouse=True)
def timestamp():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]

@pytest.fixture(scope="function", autouse=True)
def test_steps(request, timestamp):
    count = len(test_steps_list) + 1  # 步骤计数器

    def save_test_steps(action, expect_result, actual_result, result):
        nonlocal count  # 使用非本地变量
        test_step = {
            'Timestamps': timestamp,
            'Step': count,
            'Action': action,
            'ExpectResult': expect_result,
            'ActualResult': actual_result,
            'Result': result
        }
        test_steps_list.append(test_step)
        print(test_steps_list)
    yield save_test_steps

def generate_custom_report():
    html_content = """
    <html>
        <head>
            <title>Custom HTML Report</title>
            <style>
                table {
                    border-collapse: collapse;
                    width: 100%;
                }
                th, td {
                    border: 1px solid black;
                    padding: 8px;
                }
                th {
                    background-color: #f2f2f2;
                }
            </style>
        </head>
        <body>
            <h1>Custom HTML Report</h1>
            {% for test_step in test_steps_list %}
            <h2>Test Step {{ test_step['Step'] }}</h2>
            <table>
                <tr>
                    <th>Timestamps</th>
                    <th>Action</th>
                    <th>ExpectResult</th>
                    <th>ActualResult</th>
                    <th>Result</th>
                </tr>
                <tr>
                    <td>{{ test_step['Timestamps'] }}</td>
                    <td>{{ test_step['Action'] }}</td>
                    <td>{{ test_step['ExpectResult'] }}</td>
                    <td>{{ test_step['ActualResult'] }}</td>
                    <td>{{ test_step['Result'] }}</td>
                </tr>
            </table>
            {% endfor %}
        </body>
    </html>
    """

    with open('custom_report.html', 'w') as file:
        file.write(html_content)

def pytest_sessionfinish(session, exitstatus):
    # 在测试会话结束后生成自定义的报告
    generate_custom_report()

def test_example(test_steps):
    test_steps("Action 1", "Expect 1", "Actual 1", "Pass")
    test_steps("Action 2", "Expect 2", "Actual 2", "Fail")

def test_another_example(test_steps):
    test_steps("Action 3", "Expect 3", "Actual 3", "Pass")
    test_steps("Action 4", "Expect 4", "Actual 4", "Pass")

if __name__ == "__main__":
    pytest.main(['-v','test_report3.py'  ,'--html=../Report/test_report.html','--self-contained-html'])
