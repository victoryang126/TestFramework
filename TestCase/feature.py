
import pytest


"""
@pytest.feature()
scope 作用域
    function在函数的前后执行
    class
    package/session 在整个项目前后执行
autouse 自动执行，默认是false
ids 当使用params参数化时，给每一个值设置一个变量名
name 给



"""
@pytest.fixture(scope='function',autouse=True)
def execute_feature():
    print("Execute auto before ")
    yield
    print("Execute auto  after")


@pytest.fixture(scope='function')
def execute_feature_manually():
    print("Execute Manually before ")
    yield
    print("Execute manually after ")

def test_example():
    """
    Test the example function.
    """
    print("Execute")
    # result = 3
    # assert result == 42

def test_example2(execute_feature_manually):
    """
    Test the example function.
    """
    print("Execute")
    # result = 3
    # assert result == 42


if __name__ == "__main__":
    pytest.main(['-vs','feature.py'  ,'--html=../Report/report.html','--self-contained-html'])

