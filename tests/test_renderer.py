"""
Tests for HTML renderer
"""
import pytest

from tests.helpers import CLASS_NAME, HEADINGS


def test_result_has_valid_table_headings(html_table):
    headings = html_table.xpath("//th")
    assert html_table.xpath("//table/thead")
    assert len(headings) == len(HEADINGS)
    for i, th in enumerate(headings):
        th.text == HEADINGS[i]


def test_result_has_valid_table_data(html_table, data_and_columns):
    table, columns = data_and_columns
    data = table.data
    rows = html_table.xpath("//tbody/tr")
    assert html_table.xpath("//table/tbody")
    assert len(rows) == len(data)

    for i, row in enumerate(rows):
        record = data[i]
        for k, cell in enumerate(row.xpath("./td")):
            colname = table.columns[k]
            classname = cell.xpath("./@class")

            assert cell.text == str(record[colname])
            if colname == "birth_year":
                assert classname[0] == CLASS_NAME
            else:
                assert not classname
