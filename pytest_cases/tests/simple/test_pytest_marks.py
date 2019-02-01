import pytest

from pytest_cases.main import get_pytest_marks_on_case_func, get_marked_parameter_for_case


@pytest.mark.skipif(True, reason="why")
def case_func():
    pass


def test_get_pytest_marks():
    """
    Tests that we are able to correctly retrieve the marks on case_func
    :return:
    """
    # extract the marks from a case function
    marks = get_pytest_marks_on_case_func(case_func)
    assert len(marks) == 1

    # transform a parameter into a marked parameter
    dummy_case = (1, 2, 3)
    marked_param = get_marked_parameter_for_case(dummy_case, marks=marks)