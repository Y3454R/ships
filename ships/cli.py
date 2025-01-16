import argparse
from .converter import convert_webpage_to_ascii


def main():
    parser = argparse.ArgumentParser(description="Convert a webpage to ASCII structure.")
    parser.add_argument("url", help="The URL of the webpage to convert.")
    parser.add_argument("-o", "--output", help="File to save the ASCII output.", default=None)
    parser.add_argument("--ignore-links", action="store_true", help="Ignore links in the output.", default=False)
    parser.add_argument("--ignore-images", action="store_true", help="Ignore images in the output.", default=False)
    args = parser.parse_args()

    try:
        ascii_output = convert_webpage_to_ascii(
            url=args.url,
            ignore_links=args.ignore_links,
            ignore_images=args.ignore_images,
        )

        if args.output:
            with open(args.output, "w") as f:
                f.write(ascii_output)
            print(f"ASCII output saved to {args.output}")
        else:
            print(ascii_output)
    except Exception as e:
        print(f"An error occurred: {e}")
