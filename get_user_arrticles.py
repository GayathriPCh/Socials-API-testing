#This is a base for scraping Medium posts. A testing file . Later i integrated this code into the app.py. So you dont need to run this. 
import time  # Import the time module for handling delays
from selenium import webdriver  # Import the Selenium WebDriver for browser automation
from selenium.webdriver.common.by import By  # Import By from Selenium to locate elements
from bs4 import BeautifulSoup  # Import BeautifulSoup for HTML parsing
import requests  # Import the requests library for making HTTP requests

def get_latest_medium_post_url(username):
    url = f"https://medium.com/@{username}/latest"  # Construct the URL for the latest posts of the given Medium username
    driver = webdriver.Chrome()  # Initialize a Chrome WebDriver instance (ensure chromedriver is accessible)
    driver.get(url)  # Open the URL in the browser controlled by WebDriver
    time.sleep(5)  # Wait for 5 seconds to ensure the page loads completely

    # Find the latest article link using XPath
    article_link = driver.find_element(By.XPATH, '//h2/ancestor::a')
    post_url = article_link.get_attribute('href')  # Get the href attribute of the link

    driver.quit()  # Close the WebDriver instance
    return post_url  # Return the URL of the latest Medium post

def get_medium_post_content(post_url):
    response = requests.get(post_url)  # Make an HTTP GET request to fetch the Medium post content
    
    if response.status_code != 200:
        raise Exception(f"Failed to retrieve Medium post. Status code: {response.status_code}")  # Raise an exception if the request fails
    
    soup = BeautifulSoup(response.content, 'html.parser')  # Parse the HTML content using BeautifulSoup
    
    # Medium article content is usually within <article> tags
    article_content = soup.find('article')  # Find the article tag in the parsed HTML
    if not article_content:
        return "No content found."  # Return if no article content is found

    paragraphs = article_content.find_all('p')  # Find all paragraphs within the article content
    content = "\n\n".join(paragraph.get_text() for paragraph in paragraphs)  # Join paragraphs into a single string

    return content  # Return the content of the Medium post

if __name__ == "__main__":
    username = "randomusername"  # Replace with the Medium username you want to fetch posts from
    try:
        post_url = get_latest_medium_post_url(username)  # Get the URL of the latest Medium post
        if post_url:
            content = get_medium_post_content(post_url)  # Get the content of the Medium post
            print(f"Latest Post URL: {post_url}")  # Print the URL of the latest Medium post
            print(f"Content:\n{content}")  # Print the content of the latest Medium post
        else:
            print("No post URL found.")  # Print if no post URL is found
    except Exception as e:
        print(f"An error occurred: {e}")  # Print any exceptions that occur during execution
