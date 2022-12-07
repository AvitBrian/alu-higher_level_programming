#!/usr/bin/python3
""" creates a text indentation function """


def text_indentation(text):
    """ indents text """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    chars = 0
    while chars < len(text) and text[chars] == ' ':
        chars += 1
    while chars < len(text):
        print(text[chars], end="")
        if text[chars] == "\n" or text[chars] in ".?:":
            if text[chars] in ".?:":
                print("\n")
            chars += 1
            while chars < len(text) and text[chars] == ' ':
                chars += 1
            continue
        chars += 1
