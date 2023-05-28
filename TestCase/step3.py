
import datetime

import pytest
import pytest
import datetime
import pytest
import datetime
import pytest
import datetime
import pytest

import pytest

@pytest.mark.parametrize("timestamps, steps, action, expect, actual, result", [
    ("2023-05-27 10:00:00", "Step 1", "Action 111111111TGhhhhhhhhhhhhhhhhhhhhfyhuihidishf1111111111111111111111111111111111111111"*10, "Expected value 1", "Actual value 1", "Pass"),
    ("2023-05-27 11:00:00", "Step 2", "Action 2", "Expected value 2", "Actual value 2", "Fail"),
])
def test_example(timestamps, steps, action, expect, actual, result):

    assert expect == actual


if __name__ == "__main__":
    pytest.main(['-v','step3.py'  ,'--html=../Report/step3.html','--self-contained-html'])