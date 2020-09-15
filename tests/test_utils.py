"""
Unit tests for miscellaneous utility functions
"""
from unittest.mock import mock_open

import pytest

from tablify.utils import save_to_file


@pytest.fixture
def mocked_open(mocker):
    m = mock_open()
    return mocker.patch("tablify.utils.open", m)


def test_saving_to_file(mocked_open):
    filepath = "path-to-file.txt"
    save_to_file("contents", filepath)
    mocked_open.assert_called_once_with(filepath, "w", encoding="utf-8")
