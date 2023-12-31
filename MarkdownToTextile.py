import markdown2

from html.parser import HTMLParser

def markdown_to_textile_converter(file_name):
    markdown_file_path = f'./MarkdownFiles/{file_name}.md'
    textile_file_path = f'./TextileFiles/{file_name}.txt'
    html_file_path = f'./HTMLFiles/{file_name}.html'

    # Read Markdown input from a file
    with open(markdown_file_path, 'r', encoding='utf-8') as file:
        markdown_input = file.read()

    # Convert Markdown to HTML
    html_file = convert_markdown_to_html(markdown_input)
    with open(html_file_path, 'w', encoding='utf-8') as file:
        file.write(html_file)

    # Convert HTML to Textile
    textile_file = convert_html_to_textile(html_file)

    # Write Textile output to a file
    with open(textile_file_path, 'w', encoding='utf-8') as file:
        file.write(textile_file)

class HTMLToTextileParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.textile_output = []
        self.head = ""
        self.url = ""
        self.img = ""
        self.blockquote = ""
        self.strong = False
        self.ol_counter = 0
        self.ul_counter = 0
        self.is_for_blockquote = False

    def handle_starttag(self, tag, attrs):
        # print(f"start:{tag}")
        if self.textile_output:
            if self.textile_output[-1] == "\n":
                self.textile_output.pop()
        if tag in ["h1","h2","h3","h4","h5"]:
            self.head = tag
        elif tag == 'img':
            for attr, value in attrs:
                if attr == "src":
                    self.img = value
        elif tag == 'a':
            for attr, value in attrs:
                if attr == "href":
                    self.url = value
        elif tag == 'strong':
            self.strong = True
        elif tag == 'blockquote':
            self.is_for_blockquote = True
            self.textile_output.append('\n')
            self.textile_output.append('bq. ')
        elif tag == 'code':
            self.textile_output.append(' @')
        elif tag == 'ol':
            break_line_num = self.textile_output[-1].count("\n")
            self.textile_output[-1] = self.textile_output[-1].replace("\n"*break_line_num, "")
            self.ol_counter += 1
        elif tag == 'ul':
            break_line_num = self.textile_output[-1].count("\n")
            self.textile_output[-1] = self.textile_output[-1].replace("\n"*break_line_num, "")
            self.ul_counter += 1
        elif tag == 'li':
            self.textile_output.append("\n")
            # Create a nested list
            # TODO: FIX: If the nest is deeper than 4 levels and the nest has ol and ul, the deeper level list is the same as the 4 level's list type
            if self.ul_counter > 0 and self.textile_output:
                num_ul = "*"*(self.ul_counter+self.ol_counter) + " "
                self.textile_output.append(num_ul)
            elif self.ol_counter > 0:
                num_ol = "#"*(self.ol_counter+self.ul_counter) + " "
                self.textile_output.append(num_ol)

    def handle_endtag(self, tag):
        # print(f"end:{tag}")
        if tag == 'strong':
            self.strong = False
        elif tag == 'code':
            self.textile_output.append('@ ')
        elif tag == 'ol':
            self.textile_output.pop()
            self.ol_counter -= 1
        elif tag == 'ul':
            self.textile_output.pop()
            self.ul_counter -= 1
        elif tag == 'blockquote':
            self.is_for_blockquote = False

    def handle_data(self, data):
        # print(f"data:{data}")
        if self.head:
            data = f"{self.head}. {data}\n"
            self.head = ""
        elif self.url:
            data = f'"{data}":{self.url}'
            self.url = ""
        elif self.img:
            data = f"!{self.img}!\n"
            self.img = ""
        elif self.strong:
            data = f" *{data}* "
        else:
            data = f"{data}"
        self.textile_output.append(data)


def convert_html_to_textile(html_input):
    parser = HTMLToTextileParser()
    parser.feed(html_input)
    # print(parser.textile_output)
    return ''.join(parser.textile_output)

def convert_markdown_to_html(markdown_input):
    html_file = markdown2.markdown(markdown_input)
    return html_file