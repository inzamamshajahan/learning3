import pytest
import source.my_functions as my_functions
import time

def test_add():
    result = my_functions.add(1, 4)
    assert result == 5

def test_divide():
    result = my_functions.divide(10, 5)
    assert result == 2

def test_divide_by_zero1():
    with pytest.raises(ZeroDivisionError):
        my_functions.divide1(10, 0)

def test_divide_by_zero():
    with pytest.raises(ValueError):
        my_functions.divide(10, 0)

def test_add_strings():
    result = my_functions.add("I like ", "Paneer")
    assert result == "I like Paneer"

@pytest.mark.slow
def test_very_slow():
    time.sleep(5)
    result = my_functions.divide(10, 5)
    assert result == 2

"""
# we can run just tests which are marked to a particular mark using the below query:
pytest -m slow
=========================================================== test session starts ============================================================
platform linux -- Python 3.10.13, pytest-8.3.2, pluggy-1.5.0
rootdir: /workspaces/codespaces-blank/learning3
plugins: anyio-4.4.0, bdd-7.2.0
collected 12 items / 11 deselected / 1 selected                                                                                            

tests/test_my_functions.py .                                                                                                         [100%]

============================================================= warnings summary =============================================================
tests/test_my_functions.py:25
  /workspaces/codespaces-blank/learning3/tests/test_my_functions.py:25: PytestUnknownMarkWarning: Unknown pytest.mark.slow - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/stable/how-to/mark.html
    @pytest.mark.slow

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=============================================== 1 passed, 11 deselected, 1 warning in 5.03s ================================================
@inzamamshajahan ➜ /workspaces/codespaces-blank/learning3 (main) $ 
"""

@pytest.mark.skip(reason = "This feature is currently broken")
def test_add():
    result = my_functions.add(1, 4)
    assert result == 5

"""
# If we add the above mark, then that test will be skipped
@inzamamshajahan ➜ /workspaces/codespaces-blank/learning3 (main) $ pytest tests/test_my_functions.py -v
=========================================================== test session starts ============================================================
platform linux -- Python 3.10.13, pytest-8.3.2, pluggy-1.5.0 -- /usr/local/python/3.10.13/bin/python3
cachedir: .pytest_cache
rootdir: /workspaces/codespaces-blank/learning3
plugins: anyio-4.4.0, bdd-7.2.0
collected 6 items                                                                                                                          

tests/test_my_functions.py::test_add SKIPPED (This feature is currently broken)                                                      [ 16%]
tests/test_my_functions.py::test_divide PASSED                                                                                       [ 33%]
tests/test_my_functions.py::test_divide_by_zero1 PASSED                                                                              [ 50%]
tests/test_my_functions.py::test_divide_by_zero PASSED                                                                               [ 66%]
tests/test_my_functions.py::test_add_strings PASSED                                                                                  [ 83%]
tests/test_my_functions.py::test_very_slow PASSED                                                                                    [100%]

============================================================= warnings summary =============================================================
tests/test_my_functions.py:25
  /workspaces/codespaces-blank/learning3/tests/test_my_functions.py:25: PytestUnknownMarkWarning: Unknown pytest.mark.slow - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/stable/how-to/mark.html
    @pytest.mark.slow

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
================================================= 5 passed, 1 skipped, 1 warning in 5.03s ==================================================
@inzamamshajahan ➜ /workspaces/codespaces-blank/learning3 (main) $ 
"""
@pytest.mark.xfail(reason = "We know we cannot devide by zero")
def test_divide_zero_broken():
    my_functions.divide(4, 0)

"""
@inzamamshajahan ➜ /workspaces/codespaces-blank/learning3 (main) $ pytest tests/test_my_functions.py -v
=========================================================== test session starts ============================================================
platform linux -- Python 3.10.13, pytest-8.3.2, pluggy-1.5.0 -- /usr/local/python/3.10.13/bin/python3
cachedir: .pytest_cache
rootdir: /workspaces/codespaces-blank/learning3
plugins: anyio-4.4.0, bdd-7.2.0
collected 7 items                                                                                                                          

tests/test_my_functions.py::test_add SKIPPED (This feature is currently broken)                                                      [ 14%]
tests/test_my_functions.py::test_divide PASSED                                                                                       [ 28%]
tests/test_my_functions.py::test_divide_by_zero1 PASSED                                                                              [ 42%]
tests/test_my_functions.py::test_divide_by_zero PASSED                                                                               [ 57%]
tests/test_my_functions.py::test_add_strings PASSED                                                                                  [ 71%]
tests/test_my_functions.py::test_very_slow PASSED                                                                                    [ 85%]
tests/test_my_functions.py::test_divide_zero_broken XFAIL (We know we cannot devide by zero)                                         [100%]

============================================================= warnings summary =============================================================
tests/test_my_functions.py:25
  /workspaces/codespaces-blank/learning3/tests/test_my_functions.py:25: PytestUnknownMarkWarning: Unknown pytest.mark.slow - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/stable/how-to/mark.html
    @pytest.mark.slow

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
============================================ 5 passed, 1 skipped, 1 xfailed, 1 warning in 5.06s ============================================
@inzamamshajahan ➜ /workspaces/codespaces-blank/learning3 (main) $ 
"""
