"""
CLI Command
"""
import asyncio
import logging
from typing import Optional

import typer

from .reader import CSVTableReader
from .renderer import HTMLRenderer
from .ui import UserColumnSettings


logger = logging.getLogger(__name__)


app = typer.Typer()


@app.command('tablify')
def tablify(csv_file: str, output_file: Optional[str] = '') -> None:
    """Converts CSV into HTML table and saves it to output file."""
    try:
        csv_table = CSVTableReader(csv_file)
        user_input = UserColumnSettings(csv_table.columns)
        user_input.get_input()

        html_renderer = HTMLRenderer(csv_table.data, user_input)
        html_table = asyncio.run(html_renderer.render())

        fpath = output_file if output_file else f'{csv_file}.html'
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(html_table)

        logger.info(f'Finished writing converted table to {fpath}')
    except KeyboardInterrupt:
        logger.info('Canceled')
    except Exception as e:
        logger.error(f'An unhandled error occurred: {e}')
