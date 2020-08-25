"""
User Interface
"""
from collections import defaultdict
from typing import Dict, List

from prompt_toolkit import prompt
from prompt_toolkit.validation import Validator


# Validators
is_required_validator = Validator(
    lambda x: bool(str(x)),
    error_message='This field is required.',
    move_cursor_to_end=True
)


class UserColumnSettings:
    """Captures and stores user-specified column settings."""

    def __init__(self, columns: List[str]) -> None:
        self.columns = columns
        self.settings = defaultdict(lambda: dict())

    def get_input(self) -> None:
        """Shows input prompt and gets user input."""
        for col in self.columns:
            col_settings = self._process_column(col)
            self.settings[col].update(col_settings)

    def _process_column(self, column_name: str) -> Dict[str, str]:
        """Captures user settings for given column."""
        heading = prompt(
            f'Column heading for {column_name}',
            validator=is_required_validator,
            validate_while_typing=False
        )
        class_name = prompt(f'Class name for {column_name} (optional)')
        return {'heading': heading, 'class_name': class_name}
