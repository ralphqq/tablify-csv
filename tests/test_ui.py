"""
Tests on user input class
"""
from collections import defaultdict

import pytest

from tablify.ui import UserColumnSettings


COLUMN_NAMES = ['col1', 'col2', 'col3']
SIDE_EFFECT = [
    {'heading': 'Col 1', 'class_name': 'col-class'},
    {'heading': 'Col 2', 'class_name': 'col-class'},
    {'heading': 'Col 3', 'class_name': 'col-class-active'},
]

# Fixtures
@pytest.fixture
def user_input():
    return UserColumnSettings(COLUMN_NAMES)


@pytest.fixture
def mocked_process_column(mocker):
    mocked_method = mocker.patch.object(
        UserColumnSettings,
        '_process_column'
    )
    mocked_method.side_effect = SIDE_EFFECT
    return mocked_method


# Tests
def test_default_settings_dict(user_input):
    assert isinstance(user_input.settings, defaultdict)


def test_valid_user_inputs(user_input, mocked_process_column):
    user_input.get_input()

    assert mocked_process_column.call_count == len(COLUMN_NAMES)
    for i, col_name in enumerate(COLUMN_NAMES):
        assert user_input.settings[col_name] == SIDE_EFFECT[i]


def test_does_not_store_columns_with_no_user_settings(user_input, mocked_process_column):
    NEW_SIDE_EFFECT = list(SIDE_EFFECT)
    NEW_SIDE_EFFECT[2] = None# Empty settings for `col3`
    mocked_process_column.side_effect = NEW_SIDE_EFFECT

    user_input.get_input()

    assert 'col3' not in user_input.settings
