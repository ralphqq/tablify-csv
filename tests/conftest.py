"""
Test suite-wide fixtures

Fixtures:
"""
import os

import pytest


TEST_DIR_PATH = os.path.abspath(os.path.dirname(__file__))
TEST_DATA_DIR_PATH = os.path.join(TEST_DIR_PATH, 'data')


@pytest.fixture
def csv_filename():
    return os.path.join(TEST_DATA_DIR_PATH, 'valid_data.csv')

@pytest.fixture
def invalid_csv_filename():
    return os.path.join(TEST_DATA_DIR_PATH, 'invalid_data.csv')
