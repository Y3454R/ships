import requests
import html2text
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

def fetch_dynamic_page(url):
    """
    Fetches a dynamic webpage using Selenium to render JavaScript.

    Args:
        url (str): The URL of the dynamic webpage to fetch.

    Returns:
        str: HTML content after JavaScript has been executed.
    """
    # Setup Chrome WebDriver for headless mode
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run in headless mode (no GUI)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    # Open the page
    driver.get(url)

    # Wait for the page to fully load (adjust the sleep time as necessary)
    time.sleep(3)

    # Get the rendered page content after JavaScript has executed
    page_content = driver.page_source
    driver.quit()  # Close the driver

    return page_content

def convert_webpage_to_ascii(url, ignore_links=True, ignore_images=True, is_dynamic=False):
    """
    Converts a webpage to an ASCII-like text representation.

    Args:
        url (str): The URL of the webpage to convert.
        ignore_links (bool): Whether to ignore links in the output.
        ignore_images (bool): Whether to ignore images in the output.
        is_dynamic (bool): Flag to determine if the webpage is dynamic (needs JS rendering).

    Returns:
        str: ASCII-style representation of the webpage.
    """
    try:
        # Fetch the HTML content from dynamic or static page
        if is_dynamic:
            html_content = fetch_dynamic_page(url)
        else:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            html_content = response.text

        # Convert HTML to ASCII
        converter = html2text.HTML2Text()
        converter.ignore_links = ignore_links
        converter.ignore_images = ignore_images
        ascii_content = converter.handle(html_content)

        return ascii_content

    except requests.exceptions.RequestException as e:
        return f"Error fetching the webpage: {e}"

# Example usage
url = input("Enter the URL to convert: ")
is_dynamic = input("Is this a dynamic page (requires JavaScript)? (y/n): ").strip().lower() == 'y'

ascii_content = convert_webpage_to_ascii(url, is_dynamic=is_dynamic)

# Print the ASCII content or save it to a file
output_file = input("Enter output file name (e.g., output.txt): ")
with open(output_file, "w") as file:
    file.write(ascii_content)

print(f"ASCII output saved to {output_file}")
