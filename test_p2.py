import os
import pytest
from unittest.mock import patch, Mock
from module_1.scrapText import get_text
from module_2.processFiles import make_file

def test_get_text_no_title():
    # Create a mock response object with HTML content that does not include a title element
    mock_response = Mock()
    mock_response.content = """
    <html>
        <body>
            <div data-testid="prism-article-body">This is the body of the article.</div>
        </body>
    </html>
    """
    
    # Use patch to replace the requests.get function with a mock that returns the mock_response
    with patch('requests.get', return_value=mock_response):
        # Call the function with a mock URL (the actual value doesn't matter because of the mock)
        url = "http://example.com/article-with-no-title"
        title, body = get_text(url)
        
        # Assert that the function returns "No Title" for the title
        assert title == "No Title"
        

def test_get_text_no_body():
    # Create a mock response object with HTML content that includes the title but no body element
    mock_response = Mock()
    mock_response.content = """
    <html>
        <body>
            <div data-testid="prism-headline">This is the title of the article.</div>
            <!-- No data-testid="prism-article-body" element in the HTML -->
        </body>
    </html>
    """

    # Use patch to replace the requests.get function with a mock that returns the mock_response
    with patch('requests.get', return_value=mock_response):
        # Call the function with a mock URL (the actual value doesn't matter because of the mock)
        url = "http://example.com/article-with-no-body"
        title, body = get_text(url)

        # Assert that the function returns the correct title
        assert title == "This is the title of the article."
        # Assert that the function returns an empty string for the body
        assert body == ""

def test_make_file_writes_title_and_body_to_file():
    # Define test data
    title = "Test Article Title"
    body = "This is the body of the test article."
    expected_content = f"{title}\n{body}"

    # Define the folder and file paths
    processed_folder = os.path.join("Data", "processed")
    file_path = os.path.join(processed_folder, f"{title}.txt")

    # Ensure the processed folder exists
    os.makedirs(processed_folder, exist_ok=True)

    # Call the function to write the title and body to a file
    make_file(title, body)

    # Read the file content
    with open(file_path, "r") as file:
        file_content = file.read()

    # Verify that the file content matches the expected content
    assert file_content == expected_content

    # Cleanup: Remove the file after the test
    os.remove(file_path)


def test_make_file_existing_name():
    # Define the test title and body
    title = "Existing Article"
    body = "This is the body of the existing article."

    # Define the folder and file paths
    processed_folder = os.path.join("Data", "processed")
    os.makedirs(processed_folder, exist_ok=True)

    # Create a file with the same title to simulate an existing file
    existing_file_path = os.path.join(processed_folder, f"{title}.txt")
    with open(existing_file_path, "w") as file:
        file.write("This file already exists.")

    # Call the make_file function
    make_file(title, body)

    # Define a suffix variable and construct the expected filename
    suffix = 1
    expected_file_path = os.path.join(processed_folder, f"{title}-{suffix}.txt")

    # Increment suffix until the expected file is found
    while not os.path.exists(expected_file_path):
        suffix += 1
        expected_file_path = os.path.join(processed_folder, f"{title}-{suffix}.txt")

    # Read the content of the new file
    with open(expected_file_path, "r") as file:
        file_content = file.read()

    # Expected content is the combination of title and body
    expected_content = f"{title}\n{body}"
    assert file_content == expected_content

    # Cleanup: Remove the files created during the test
    os.remove(existing_file_path)
    os.remove(expected_file_path)

