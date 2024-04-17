# scrapText.py
# Braden Burgener

# The SOLID principle I inlcuded was S (Single Responsibility Principle)
# Each function has a specific, focused responsibility
# Code is more maintainable and easy to understand with compartmentalization of functions into specific responsibilities

import requests
from bs4 import BeautifulSoup
from module_3.chatgptAPI import get_ai_response

enableAPI = True

# Takes in a url of an ABC sports news article
# Outputs the title and body as a pair of strings
def get_text(url):
    try:
        # Fetch the HTML content from the URL
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Locate the title and body elements in the HTML content
        title_element = soup.find("div", attrs={"data-testid": "prism-headline"})
        body_element = soup.find("div", attrs={"data-testid": "prism-article-body"})

        # Determine the title and body based on the found elements
        title = title_element.get_text(separator="\n") if title_element else "No Title"
        body = body_element.get_text(separator="\n") if body_element else ""

        # If enableAPI is True, process the body through AI
        if enableAPI:
            ai_response = get_ai_response(body)
            return title, ai_response
        else:
            return title, body


    except Exception as e:
        # Handle exceptions by returning an error message and an empty string for the body
        return f"Error: {e}", ""
