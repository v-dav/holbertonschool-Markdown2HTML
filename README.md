# Markdown to HTML

![Python Version](https://img.shields.io/badge/Python-3.7%20%2B-blue.svg)
![PEP8 Compliant](https://img.shields.io/badge/PEP8-Compliant-green.svg)

![Convert-Markdown-to-HTML-in-Java-using-REST-API](https://github.com/v-dav/holbertonschool-Markdown2HTML/assets/115344057/158d9cd3-b04f-4865-8065-def1dea37197)


## 🧐 Project Overview

Welcome to the "Markdown to HTML" project! In this project, you'll learn how to convert Markdown files into HTML. You'll utilize Python 3.7 or higher, ensuring PEP 8 style compliance. This project is designed to strengthen your Python skills while introducing you to the intricacies of parsing and processing text.

## 🌱 Learning Objectives

By the end of this project, you'll be able to:

- Understand and use Python 3.7 or higher
- Convert Markdown files into HTML
- Follow the PEP 8 style guide
- Document your modules effectively
- Ensure that your code is executable and follows best practices

## ⚙️ Requirements

To successfully run this project, make sure you have:

- Python 3.7 or higher installed
- PEP 8 compliant style (you can use a tool like `autopep8` for formatting)
- Executable files with the shebang `#!/usr/bin/python3`
- A well-documented README.md file at the root of your project
- Modules that adhere to PEP 8 and include proper documentation
- Code that is not executed when imported (use `if __name__ == "__main__":`)


## 🧑🏻‍💻 Usage
The script takes two arguments from the CLI:

- First argument is the name of the Markdown file
- Second argument is the output file name

```python
python3 markdown2html.py README.md README.html
```
        
## 🧐 Supported Markdown Syntax
   
- **Headings**


| Markdown | HTML Generated |
| -------- | -------- |
| # Heading level 1    | ```<h1>Heading level 1</h1>```    |
| ## Heading level 2   | ```<h2>Heading level 2</h1>```    |
| ### Heading level 3    | ```<h3>Heading level 1</h1>```    |
| #### Heading level 4    | ```<h4>Heading level 1</h4>```   |
| ##### Heading level 5   | ```<h5>Heading level 1</h5>```    |
| ###### Heading level 6    | ```<h6>Heading level 1</h6>```    |

- **Unordered listing**

➤ Markdown

\- Hello

\- Bye

➤ HTML Generated
````
<ul>
    <li>Hello</li>
    <li>Bye</li>
</ul>
````

- **Ordered listing**

➤ Markdown

\* Hello

\* Bye

➤ HTML Generated
````
<ol>
    <li>Hello</li>
    <li>Bye</li>
</ol>
````

- **Simple text**

➤ Markdown

Hello

I'm a text <br/>
with 2 lines

➤ HTML Generated
````
<p>
    Hello
</p>
<p>
    I'm a text
        <br />
    with 2 lines
</p>
````

- **Bold and emphasis text**

| Markdown | HTML Generated |
| -------- | -------- |
| \*\*Hello**    | ```<b>Hello</b>```    |
| \_\_Hello__   | ```<em>Hello</em>```    |

- **Just for fun**

| Markdown |  HTML Generated|Description|
| -------- | -------- |  -------- |
| [[Hello]]    | 8b1a9953c4611296a827abf8c47804d7	   | convert in MD5 (lowercase) the content
|((Hello Chicago))  | Hello hiago    |remove all c (case insensitive) from the content


## 🧑‍💻 Author

- [Vladimir Davidov](https://github.com/v-dav) - Holberton School
