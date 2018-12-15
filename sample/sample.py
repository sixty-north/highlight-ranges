# This is a comment
def foo():
    "docstring"
    with open('asdf', mode='rt') as handle:
        x = [1, 2, 3]
        y = x[1]
        return handle.read()