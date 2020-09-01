"""
Unit tests for CLI commands
"""
import pytest
from typer.testing import CliRunner


@pytest.fixture
def runner():
    return CliRunner()


def test_tablify_command(runner):
    pass
