# scrapText.py
# Braden Burgener

# The SOLID principle I inlcuded was S (Single Responsibility Principle)
# Each function has a specific, focused responsibility
# Code is more maintainable and easy to understand with compartmentalization of functions into specific responsibilities

import requests
from bs4 import BeautifulSoup
from module_3.chatgptAPI import get_ai_response

# Takes in a url of an ABC sports news article
# Outputs the title and body as a pair of strings
def get_text(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Using the structure of sports articles from ABC news, finds the title and body text of the article
        title_ = soup.find("div", attrs={"data-testid": "prism-headline"})
        body_ = soup.find("div", attrs={"data-testid": "prism-article-body"})

        if title_ and body_:
            title = title_.get_text(separator="\n")
            body = body_.get_text(separator="\n")
            ai_response = get_ai_response(body)
            return title, ai_response
        elif body_:
            body = body_.get_text(separator="\n")
            title = "No Title"
            ai_response = get_ai_response(body)
            return title, ai_response
        else:
            return "No text found in URL", ""
    except Exception as e:
        return f"Error: {e}", ""