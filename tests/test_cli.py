"""
Unit tests for CLI commands
"""
from unittest.mock import AsyncMock, MagicMock, patch, mock_open

import pytest
from typer.testing import CliRunner

from tablify.cli import app


@pytest.fixture
def runner():
    return CliRunner()


@pytest.fixture
def mocked_calls(mocker, data_and_columns, html_table):
    csv_table, columns = data_and_columns

    mocked_csv_table = mocker.patch(
        'tablify.cli.CSVTableReader',
        return_value=csv_table
    )
    mocked_columns = mocker.patch(
        'tablify.cli.UserColumnSettings',
        return_value=columns
    )
    mocked_columns.get_input = MagicMock()
    mocked_async_render = patch(
        'tablify.cli.HTMLRenderer.render',
        new_callable=AsyncMock
    )
    mocked_async_render.return_value = html_table
    # Mock open()


def test_tablify_cli_command(runner):
    pass
