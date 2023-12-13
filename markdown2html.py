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

    # Parsing the markdown file and writing html to a new html file
    with open(md_file, "r", encoding='UTF-8') as markdown:
        with open(html_file, "w", encoding='UTF-8') as html:
            ol_open = False
            ul_open = False
            p_open = False
            while True:
                line = markdown.readline()

                # Checks if we are in an ul
                if ul_open and not line.startswith("-"):
                    html.write("</ul>\n")
                    ul_open = False

                # Checks if we are in an ol
                if ol_open and not line.startswith("*"):
                    html.write("</ol>\n")
                    ol_open = False

                # Checks if we are in a paragraph
                if p_open and (line.startswith("-") or line.startswith("*") or
                               line.startswith("#") or line.startswith("\n")):
                    html.write("</p>\n")
                    p_open = False

                # Reaches the EOF
                if not line:
                    break

                # Generates Headings
                if line.startswith("#"):
                    count = line.count("#")
                    text = line.rsplit('# ', 1)[1].strip()
                    html.write(f"<h{count}>{text}</h{count}>\n")

                # Generates unordered listing
                elif line.startswith("-"):
                    if not ul_open:
                        html.write("<ul>\n")
                        ul_open = True
                    text = line.rsplit('- ', 1)[1].strip()
                    html.write(f"<li>{text}</li>\n")

                # Generates ordered listing
                elif line.startswith('*'):
                    if not ol_open:
                        html.write("<ol>\n")
                        ol_open = True
                    text = line.rsplit('* ', 1)[1].strip()
                    html.write(f"<li>{text}</li>\n")

                # Generates paragraphs
                elif not line.startswith("\n"):
                    if not p_open:
                        html.write("<p>\n")
                        p_open = True
                    else:
                        html.write("<br/>\n")
                    text = line
                    html.write(text)

    # Exits after sucessful program execution
    sys.exit()


if __name__ == "__main__":
    main()
