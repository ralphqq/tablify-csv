"""
Test suite-wide fixtures

Fixtures:
    csv_filename
    data_and_columns
    html_table
"""
import os

from lxml import html
import pytest

from tablify.reader import CSVTableReader
from tablify.renderer import HTMLRenderer
from tablify.ui import UserColumnSettings
from tests.helpers import (
    CLASS_NAME,
    TEST_DATA_DIR_PATH,
    TEST_DIR_PATH,
    HEADINGS,
)


@pytest.fixture
def csv_filename():
    return os.path.join(TEST_DATA_DIR_PATH, 'valid_data.csv')

@pytest.fixture
def invalid_csv_filename():
    return os.path.join(TEST_DATA_DIR_PATH, 'invalid_data.csv')


@pytest.fixture
def data_and_columns(csv_filename):
    csv_table = CSVTableReader(csv_filename)

    col_names = csv_table.columns
    col_settings = {
        col_names[i]: {'heading': HEADINGS[i]} for i in range(len(col_names))
    }
    col_settings['birth_year']['class_name'] = CLASS_NAME

    columns = UserColumnSettings(col_names)
    columns.settings = col_settings

    return csv_table, columns


@pytest.fixture
async def html_table(data_and_columns):
    table, columns = data_and_columns
    html_renderer = HTMLRenderer(table.data, columns)
    result = await html_renderer.render()
    yield html.fromstring(result)
