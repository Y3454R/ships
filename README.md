# Ships: Webpage to ASCII Converter

## Overview

`Ships` is a tool that converts webpages into an ASCII-like text representation. The tool supports both static and dynamic webpages. It uses the `html2text` library to convert static HTML pages and Selenium to render and fetch content from JavaScript-rendered pages.

## Features

- Converts static webpages into ASCII format.
- Supports dynamic content loading with Selenium and WebDriver.
- Exports the result to a text file.
- Customizable to ignore links and images during conversion.

## Installation

### Prerequisites

Make sure you have Python 3.6 or above installed.

### Install the Dependencies

Clone the repository and install the required dependencies using `pip`:

```bash
git clone https://github.com/Y3454R/ships.git
cd ships
pip install -r requirements.txt
```

## Usage

### Command Line Interface (CLI)

To use the tool from the command line:

```bash
python -m ships.cli <URL> -o <output_file.txt>
```

- `<URL>`: The URL of the webpage you want to convert.
- `-o <output_file.txt>`: The file where the ASCII output will be saved. If not provided, the result is printed to the console.

#### Example Usage:

1. Convert a webpage to ASCII and save it to a file:

```bash
python -m ships.cli https://example.com -o output.txt
```

2. View the ASCII representation directly in the terminal:

```bash
python -m ships.cli https://example.com
```

### Dynamic Page Support

For websites with JavaScript content, you can fetch the dynamically rendered HTML using Selenium. The tool uses Chrome in headless mode for this purpose.

## Acknowledgements

- [html2text](https://github.com/Alir3z4/html2text)
- [Selenium](https://www.selenium.dev/documentation/en/)
- [Webdriver Manager](https://github.com/SergeyPirogov/webdriver_manager)

## Future Ideas

### Image to ASCII Conversion

In the future, we plan to extend `Ships` to support converting images to ASCII art. This would allow users to take images (such as UI mockups or website screenshots) and convert them into an ASCII representation. This can be useful for:

- Generating ASCII-style mockups for design sharing.
- Converting graphical content to simple, text-based formats.

<!-- ### Additional Features:
1. **Tag Filtering**: Allow users to extract and convert specific HTML tags (e.g., `<nav>`, `<header>`) into ASCII format.
2. **Markdown Output**: Provide the option to save the ASCII output in Markdown format, which is widely used for documentation.
3. **Themes**: Customize ASCII output with simple themes (e.g., box-style layouts for better visual presentation).
4. **GUI Interface**: Add a GUI for non-programmers to make it easier to use the tool without the command line.
5. **User-defined Styles**: Allow users to define their custom styles for the ASCII output.
6. **Support for More Formats**: Extend the tool to support converting other types of content into ASCII-like formats, such as PDF files or Word documents. -->

### **Future Plans**:

- **Image to ASCII Support**: We will include a feature to convert images into ASCII format. This will be beneficial for generating text-based representations of images such as screenshots, UI designs, or even artistic renderings.
