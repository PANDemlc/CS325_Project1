import pytest
import os
from unittest.mock import mock_open, patch
from module_2.processFiles import open_file

# Test when the input.txt file does not exist
def test_open_file_no_exist(capfd):  # capfd captures print outputs
    # Simulate a file not found error within the function.
    with patch('builtins.open', side_effect=FileNotFoundError("Input file 'input.txt' doesn't exist.")):
        open_file('input.txt')
        out, err = capfd.readouterr()
        # Test that function is correctly catching the error and diplaying user feedback in std out
        assert "Input file 'input.txt' doesn't exist." in out

# Test when input.txt exists but is empty
def test_open_file_empty():
    with patch('builtins.open', mock_open(read_data='')) as mocked_file:
        with patch('module_2.processFiles.get_text') as mocked_get_text:
            open_file('input.txt')
            mocked_file.assert_called_once_with('input.txt', 'r')
            # Ensure that get_text is not being called when file is blank (no text scraping should take place if there is no URL)
            mocked_get_text.assert_not_called()

# Test when input.txt has invalid URLs
def test_open_file_invalid_urls(capfd): # Added lines 19-23 so the function sees invalid URLs
    invalid_urls = "http//invalid-url\nhttp://\nhttps://"
    expected_messages = ["Invalid URL: http//invalid-url", "Invalid URL: http://", "Invalid URL: https://"]
    
    with patch('builtins.open', mock_open(read_data=invalid_urls)):
        open_file('input.txt')
        out, err = capfd.readouterr()

    # Check that each expected message appears in the output
    for message in expected_messages:
        assert message in out

# Make temp file for testing
def setup_file(contents):
    with open('test_input.txt', 'w') as f:
        f.write(contents)

# Remove temp file for testing
def remove_file():
    if os.path.exists('test_input.txt'):
        os.remove('test_input.txt')

# Test handling valid URLs
def test_open_file_with_urls(capfd):
    setup_file('http://example.com\nhttps://example.com')
    open_file('test_input.txt')
    out, err = capfd.readouterr()
    remove_file()