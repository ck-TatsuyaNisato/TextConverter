import html2markdown
import textile

def textile_to_markdown_converter(file_name):
    markdown_file_path = f'./MarkdownFiles/{file_name}.md'
    textile_file_path = f'./TextileFiles/{file_name}.txt'
    html_file_path = f'./HTMLFiles/{file_name}.html'

    # Read Markdown input from a file
    with open(textile_file_path, 'r', encoding='utf-8') as file:
        textile_input = file.read()

    # Convert Markdown to HTML
    html_file = textile.textile(textile_input)
    with open(html_file_path, 'w', encoding='utf-8') as file:
        html_file = '\n'.join(line.lstrip() for line in html_file.split('\n'))
        file.write(html_file)

    # Convert HTML to Textile
    markdown_file = html2markdown.convert(html_file)

    # Write Textile output to a file
    with open(markdown_file_path, 'w', encoding='utf-8') as file:
        file.write(markdown_file)

