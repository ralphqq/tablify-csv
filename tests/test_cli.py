"""
Unit tests for CLI commands
"""
from unittest.mock import AsyncMock, call, MagicMock

import pytest
from typer.testing import CliRunner

from tablify.cli import app


INPUT_FILENAME = "data.csv"


@pytest.fixture
def runner():
    return CliRunner()


@pytest.fixture
def mocked_calls(mocker, data_and_columns, html_render_result):
    csv_table, columns = data_and_columns

    mocked_csv_table = mocker.patch(
        "tablify.cli.CSVTableReader", return_value=csv_table
    )
    mocked_columns = mocker.patch(
        "tablify.cli.UserColumnSettings", return_value=columns
    )
    mocked_columns.return_value.get_input = MagicMock()
    mocked_async_render = mocker.patch(
        "tablify.cli.HTMLRenderer.render", new_callable=AsyncMock
    )
    mocked_async_render.return_value = html_render_result

    mocked_save = mocker.patch("tablify.cli.save_to_file")

    return (
        mocked_csv_table,
        mocked_columns,
        mocked_async_render,
        mocked_save,
    )


def test_tablify_command_with_no_output_file(runner, mocked_calls):
    mocked_csv_table, _, _, mocked_save = mocked_calls
    output_file = f"{INPUT_FILENAME}.html"

    result = runner.invoke(app, INPUT_FILENAME)

    assert result.exit_code == 0
    mocked_csv_table.assert_called_once_with(INPUT_FILENAME)
    assert output_file in mocked_save.call_args.args


def test_tablify_command_with_output_file(runner, mocked_calls):
    _, _, _, mocked_save = mocked_calls
    actual_output_file = "converted_table.html"

    result = runner.invoke(
        app, [INPUT_FILENAME, "--output-file", actual_output_file]
    )

    assert result.exit_code == 0
    assert actual_output_file in mocked_save.call_args.args


def test_tablify_command_errors(runner, mocked_calls):
    _, _, mocked_async_render, _ = mocked_calls
    mocked_async_render.side_effect = ValueError
    result = runner.invoke(app, INPUT_FILENAME)
    assert result.exit_code == 1


def test_tablify_command_keyboard_interrupt(runner, mocked_calls, caplog):
    _, mocked_columns, _, _ = mocked_calls
    mocked_columns.return_value.get_input.side_effect = KeyboardInterrupt

    result = runner.invoke(app, INPUT_FILENAME)

    assert result.exit_code == 0
    assert "Canceled" in caplog.text
