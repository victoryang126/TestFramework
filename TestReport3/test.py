import pytest

import pytest

@pytest.mark.servername(server='my_server_name')
def test_function():
    print("111")
# do your test

if __name__ == "__main__":
    pytest.main(['-v','test.py'  ,'--html=../Report/test.html','--self-contained-html'])
