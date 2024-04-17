import pytest
import os
from unittest.mock import mock_open, patch
from module_2.processFiles import open_file

# Test when the input.txt file does not exist
def test_open_file_no_exist(capfd):  # capfd captures print outputs
    with patch('builtins.open', side_effect=FileNotFoundError("Input file 'input.txt' doesn't exist.")):
        open_file('input.txt')
        out, err = capfd.readouterr()
        assert "Input file 'input.txt' doesn't exist." in out

# Test when input.txt exists but is empty
def test_open_file_empty():
    with patch('builtins.open', mock_open(read_data='')) as mocked_file:
        with patch('module_2.processFiles.get_text') as mocked_get_text:
            open_file('input.txt')
            mocked_file.assert_called_once_with('input.txt', 'r')
            mocked_get_text.assert_not_called()

# Test when input.txt has invalid URLs
def test_open_file_invalid_urls(capfd):
    invalid_urls = "http//invalid-url\nhttp://\nhttps://"
    with patch('builtins.open', mock_open(read_data=invalid_urls)):
        open_file('input.txt')
        out, err = capfd.readouterr()

def setup_file(contents):
    with open('test_input.txt', 'w') as f:
        f.write(contents)

def remove_file():
    if os.path.exists('test_input.txt'):
        os.remove('test_input.txt')

# Optional: Test handling valid URLs (would normally require mocking network responses)
def test_open_file_with_urls(capfd):
    setup_file('http://example.com\nhttps://example.com')
    open_file('test_input.txt')
    out, err = capfd.readouterr()
    remove_file()