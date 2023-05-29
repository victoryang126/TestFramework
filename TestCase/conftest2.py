
import pytest
import datetime



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
    '''



    html += '''
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
        extra.append(pytest_html.extras.html(generate_html_table()))
        # print(extra.html)
        report.extra = extra