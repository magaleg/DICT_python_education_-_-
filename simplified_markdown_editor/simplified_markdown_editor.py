"""project Markdown editor"""


def print_help():
    """Prints a list of available formatters and special commands"""
    help_text = """Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line
Special commands: !help !done"""
    print(help_text)


def format_text(formatter, text, level=None, url=None):
    """Applies chosen format to the text given.
    :param:
    formatter (str) is a type of formatting
    text (str or list) is a text for formatting
    level (int) is used for the header
    url (str) is an url for link

    :returns: formatted text (str)"""

    if formatter == "plain":
        return text
    elif formatter == "bold":
        return f"\n__{text}__"
    elif formatter == "italic":
        return f"\n_{text}_"
    elif formatter == "header":
        return f"\n{'#' * level} {text}"
    elif formatter == "link":
        return f"\n[{text}]({url})"
    elif formatter == "inline-code":
        return f"\n`{text}`"
    elif formatter == "ordered-list":
        return '\n'.join([f"{i + 1}. {item}" for i, item in enumerate(text)])
    elif formatter == "unordered-list":
        return '\n'.join([f"* {item}" for item in text])
    elif formatter == "new-line":
        return "\n"
    else:
        return ""


def main():
    """The main function to run the program. Asks the user to provide a formatter,
    then shows the result. When done, saves the result to the output.md"""

    markdown_text = ""
    formatters = {
        "plain", "bold", "italic", "header", "link", "inline-code",
        "ordered-list", "unordered-list", "new-line"
    }

    while True:
        formatter = input("Choose a formatter: ")

        if formatter == "!help":
            print_help()
            continue
        elif formatter == "!done":
            with open("output.md", "w") as file:
                file.write(markdown_text)
            print(markdown_text)
            break
        elif formatter not in formatters:
            print("Unknown formatting type or command")
            continue

        if formatter == "header":
            try:
                level = int(input("Level: "))
                if not 1 <= level <= 6:
                    print("The level should be within the range of 1 to 6")
                    continue
            except ValueError:
                print("The level should be within the range of 1 to 6")
                continue
            text = input("Text: ")
            markdown_text += format_text(formatter, text, level)

        elif formatter == "link":
            text = input("Label: ")
            url = input("URL: ")
            markdown_text += format_text(formatter, text, url=url)

        elif formatter == "ordered-list" or formatter == "unordered-list":
            try:
                num_items = int(input("Number of rows: "))
                if num_items <= 0:
                    print("The number of rows should be greater than zero")
                    continue
            except ValueError:
                print("The number of rows should be greater than zero")
                continue
            items = [input(f"Row #{i + 1}: ") for i in range(num_items)]
            markdown_text += '\n' + format_text(formatter, items)

        elif formatter == "new-line":
            markdown_text += format_text(formatter, "")

        else:
            text = input("Text: ")
            markdown_text += format_text(formatter, text)

        print(markdown_text)


if __name__ == "__main__":
    main()
