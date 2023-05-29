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
        action = getattr(item.function, 'action', 'N/A')
        expect = getattr(item.function, 'expect', 'N/A')
        actual = getattr(item.function, 'actual', 'N/A')
        result = report.outcome.capitalize()
        data = {
            'timestamps': timestamp_value,
            'teststeps': teststep_value,
            'action': action,
            'expect': expect,
            'actual': actual,
            'result': result
        }
        extra.append(pytest_html.extras.html(generate_html_table([data])))
        report.extra = extra


@pytest.mark.html
def test_case_example(timestamp, teststep):
    action = "Perform some action"
    expect = "Expected value"
    actual = "Actual value"
    result = "Passed" if expect == actual else "Failed"

    setattr(test_case_example, 'action', action)
    setattr(test_case_example, 'expect', expect)
    setattr(test_case_example, 'actual', actual)

    assert expect == actual, "Assertion failed"


@pytest.mark.html
def test_case_another_example(timestamp, teststep):
    action = "Perform another action"
    expect = "Another expected value"
    actual = "Another actual value"
    result = "Passed" if expect == actual else "Failed"

    setattr(test_case_another_example, 'action', action)
    setattr(test_case_another_example, 'expect', expect)
    setattr(test_case_another_example, 'actual', actual)

    assert expect == actual, "Assertion failed"




if __name__ == "__main__":
    pytest.main(['-v','test_report.py','--html=test_report.html'])
