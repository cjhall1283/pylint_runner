# pylint: disable=missing-docstring,no-value-for-parameter
import os
import pylint_runner.main as runner
from nose.tools import assert_raises, assert_equal


def test_get_files():
    # make sure we use root of pylint_runner module
    os.chdir(os.path.dirname(os.path.realpath(__file__)) + '/../')
    actual = runner.get_files_from_dir(os.curdir)
    expected = ['pylint_runner/__init__.py', 'pylint_runner/main.py',
                'setup.py', 'tests/__init__.py', 'tests/test_runner.py',
                'tests/tests/dummy.py']
    _assert_list_equals(expected, actual)


def test_get_files_current_dir():
    path = os.path.dirname(os.path.realpath(__file__))
    actual = runner.get_files_from_dir(path)
    expected = [path+'/__init__.py', path+'/test_runner.py',
                path+'/tests/dummy.py']
    _assert_list_equals(expected, actual)


def test_runner():
    with assert_raises(SystemExit) as context_manager:
        runner.runner(error=open(os.devnull, 'w'))
    assert_equal(context_manager.exception.code, 0)


def _assert_list_equals(list1, list2):
    assert_equal(len(list1), len(list2))
    assert_equal(sorted(list1), sorted(list2))