# ships/__init__.py

"""
ships: A Python package for converting webpages and images to ASCII format.

This package provides the functionality to convert a webpage or image into an ASCII-like representation.
It includes core logic for converting HTML to ASCII and a command-line interface (CLI).
"""

from .converter import convert_webpage_to_ascii
from .cli import main
