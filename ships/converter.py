import requests
import html2text


def convert_webpage_to_ascii(url, ignore_links=True, ignore_images=True):
    """
    Converts a webpage to an ASCII-like text representation.
    
    Args:
        url (str): The URL of the webpage to convert.
        ignore_links (bool): Whether to ignore links in the output.
        ignore_images (bool): Whether to ignore images in the output.
    
    Returns:
        str: ASCII-style representation of the webpage.
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        html_content = response.text

        # Convert HTML to ASCII-like text
        converter = html2text.HTML2Text()
        converter.ignore_links = ignore_links
        converter.ignore_images = ignore_images

        return converter.handle(html_content)
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Error fetching the webpage: {e}")
