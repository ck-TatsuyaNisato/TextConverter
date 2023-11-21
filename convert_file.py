import MarkdownToTextile
import TextileToMarkdown

def main():
    # Get a target file name and check the extension
    file_name_with_extension = input().split(".")
    file_name_without_extension = file_name_with_extension[:-1]
    file_name = ''.join(map(str, file_name_without_extension))

    if file_name_with_extension[-1] == "md":
        MarkdownToTextile.markdown_to_textile_converter(file_name)
    elif file_name_with_extension[-1] == "txt":
        TextileToMarkdown.textile_to_markdown_converter(file_name)

if __name__ == "__main__":
    main()
