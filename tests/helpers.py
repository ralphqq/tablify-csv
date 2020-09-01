"""
Helper resources/utilities for tests
"""
import os

# Constants
CLASS_NAME = 'some-class-name'
HEADINGS = ['Name', 'Year of Birth', 'Instrument Played']

TEST_DIR_PATH = os.path.abspath(os.path.dirname(__file__))
TEST_DATA_DIR_PATH = os.path.join(TEST_DIR_PATH, 'data')
