#!/usr/bin/python3
"""A script converting Markdown markup language files into HTML files"""

import os
import sys


def main():
    """The main function running the script

    Raises:
            "Usage: ./markdown2html.py README.md README.html" to STDERR:
            If the number of arguments in the CLI is different of 2
            "Missing <filename>" to STDERR: If the Markdown file doesn’t exist
    """

    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py README.md README.html",
              file=sys.stderr)
        sys.exit(1)

    md_file = sys.argv[1]
    if not os.path.isfile(md_file):
        print(f"Missing {md_file}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
