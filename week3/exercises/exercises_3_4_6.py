long_string = """This is
a multi-line string
to show how
multi-line strings work"""
for word in long_string.split("\n"):
    # by default split splits on any white space (space, tab, newline)
    # but you can have it split only on newlines like in this example.
    print(word)
