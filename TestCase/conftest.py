
import pytest
import datetime
from HTMLTable import  HTMLTable
def read_template_html(file_path):
    with open(file_path, 'r') as file:
        template_html = file.read()
    return template_html


test_steps_list = []

@pytest.fixture(scope="session", autouse=True)
def timestamp():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]

@pytest.fixture(scope="function", autouse=True)
def test_steps(request, timestamp):
    count = len(test_steps_list) + 1  # 步骤计数器
    print(test_steps_list)
    def save_test_steps(action, expect_result, actual_result, result):
        nonlocal count  # 使用非本地变量
        test_step = {
            'Timestamps': timestamp,
            'TestSteps': count,
            'Action': action,
            'Expect': expect_result,
            'Actual': actual_result,
            'Result': result
        }
        test_steps_list.append(test_step)

    yield save_test_steps

# @pytest.fixture(scope="function", autouse=True)
# def test_step(request,action,expect_result,actual_result,result):
#     timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
#     test_step = {
#         'Timestamps': timestamp,
#         'TestSteps': 0,
#         'Action': action,
#         'ExpectResult': expect_result,
#         'ActualResult': actual_result,
#         'Result': result
#     }
#     test_steps_list.append(test_step)

def generate_customer_table():
    table = HTMLTable()
    # table.append_rows('')
    table.append_header_rows((('Timestamps','TestSteps','Action','Expect','Actual','Result'),))
    for test_step in test_steps_list:
        print(test_step)
        table.append_data_rows(((test_step["Timestamps"],test_step["TestSteps"],test_step["Action"],test_step["Expect"],test_step["Actual"],test_step["Result"]),))
    table_style = {
    "border-collapse": "collapse",
    "width": "100%",
    "background-color": "#f2f2f2"
    }
    table.set_style(table_style)
    # print(table.to_html())
    return f"<p>{table.to_html()}</p>"

def generate_html_table():
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
      {% for test_step in test_steps_list %}
        <tr>
            <td>{{ test_step['Timestamps'] }}</td>
            <td>{{ test_step['Action'] }}</td>
            <td>{{ test_step['ExpectResult'] }}</td>
            <td>{{ test_step['ActualResult'] }}</td>
            <td>{{ test_step['Result'] }}</td>
        </tr>
    {% endfor %}
    </table>
    </p>
    '''
    return html




@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    # print(report)
    extra = getattr(report, 'extra', [])
    if report.when == 'call':
        #默认的stdout暂时不知道如何删除
        # extra.append(pytest_html.extras.html(generate_html_table()))
        extra.append(pytest_html.extras.html(generate_customer_table()))
        # print(extra.html)
        report.extra = extra