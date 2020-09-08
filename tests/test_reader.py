"""
Unit tests for CSVTableReader classs
"""
import pytest

from tablify.reader import CSVTableReader


def test_successfully_reads_valid_csv_table(csv_filename):
    csv_table = CSVTableReader(csv_filename)

    assert csv_table.csv_file == csv_filename
    assert set(csv_table.columns) == set(["name", "birth_year", "instrument"])
    assert len(csv_table.data) == 4


def test_throws_value_error_if_no_data_found(invalid_csv_filename):
    with pytest.raises(ValueError):
        CSVTableReader(invalid_csv_filename)
