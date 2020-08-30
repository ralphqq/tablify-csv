"""
Tests for HTML renderer
"""
from lxml import html
import pytest

from tablify.reader import CSVTableReader
from tablify.renderer import HTMLRenderer
from tablify.ui import UserColumnSettings

CLASS_NAME = 'some-class-name'
HEADINGS = ['Name', 'Year of Birth', 'Instrument Played']


# Fixtures
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


# Tests
def test_result_has_valid_table_headings(html_table):
    headings = html_table.xpath('//th')
    assert html_table.xpath('//table/thead')
    assert len(headings) == len(HEADINGS)
    for i, th in enumerate(headings):
        th.text == HEADINGS[i]


def test_result_has_valid_table_data(html_table, data_and_columns):
    table, columns = data_and_columns
    data = table.data
    rows = html_table.xpath('//tbody/tr')
    assert html_table.xpath('//table/tbody')
    assert len(rows) == len(data)

    for i, row in enumerate(rows):
        record = data[i]
        for k, cell in enumerate(row.xpath('./td')):
            colname = table.columns[k]
            classname = cell.xpath('./@class')

            assert cell.text == str(record[colname])
            if colname == 'birth_year':
                assert classname[0] == CLASS_NAME
            else:
                assert not classname
