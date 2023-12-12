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

    # Checking if number of CLI arguments is wright
    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py README.md README.html",
              file=sys.stderr)
        sys.exit(1)

    md_file = sys.argv[1]
    html_file = sys.argv[2]

    # Checking if markdown file exists
    if not os.path.isfile(md_file):
        print(f"Missing {md_file}", file=sys.stderr)
        sys.exit(1)

    # Parsing the markdown file and writing headings to a new html file
    with open(md_file, "r", encoding='UTF-8') as markdown:
        with open(html_file, "w", encoding='UTF-8') as html:
            while True:
                line = markdown.readline()
                if not line:
                    break
                if line.startswith("#"):
                    count = line.count("#")
                    text = line.rsplit('# ', 1)[1].strip()
                    html.write(f"<h{count}>{text}</h{count}>\n")

    # Exits after sucessful program execution
    sys.exit()


if __name__ == "__main__":
    main()
