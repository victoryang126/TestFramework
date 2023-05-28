import pytest

@pytest.mark.expect_result("Pass")
@pytest.mark.actual_result("Pass")
def test_example():
    assert 2 + 2 == 4

@pytest.mark.expect_result("Fail")
@pytest.mark.actual_result("Pass")
def test_another_example():
    assert 2 + 2 == 5

@pytest.mark.expect_result("Pass")
@pytest.mark.actual_result("Pass")
def test_one_more_example():
    assert 2 * 2 == 4

if __name__ == "__main__":
    pytest.main(['-v','step4.py'  ,'--html=../Report/report.html','--self-contained-html'])