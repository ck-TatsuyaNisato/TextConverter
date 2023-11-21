You can write with external link(ex. Wiki, esa.io). No need to write again.  
However take care of being same permissions a repository and wiki page.

# File Converter (Markdown2Textile or Textile2Markdown)
## Description
- What is the purpose: To convert files easily
- Languages/Framework: Python
- Link to Documentation

## How to
### Set up for development
1. Install Python
2. (Optional) Install venv
3. `$ pip install -r requirements.txt`

### How to use
1. Clone the repository
2. Open your terminal
3. Move the local repository
4. Store your file to convert in the target foloder (e.g. If you want to convert a Markdown file to a Textile file, please store the file in `MarkdownFiles`)
5. `$ python convert_file.py`
6. `{FILE_NAME.XX}`
7. Check the target folders ( (e.g. If you converted a Markdown file to a Textile file, please check the file in `TextileFiles`))

### Limitations
- Due to the breaklines, some lines cannot be recognized as a heading
- Due to the bug of `markdown2`, not applicable when using italic

### Deploy the code

### Release
write here

### Coding Review
write here

## (optional, also ok in docs) Dependencies (homepage, license, reason for using)
- html2markdown  0.1.7
- markdown2      2.4.10
- textile        4.0.2
- pip            23.3.1
