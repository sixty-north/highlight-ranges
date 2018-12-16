"""Support for styling the output with CSS.
"""
import pkg_resources


def default_css():
    """Get the default CSS for pygmentized HTML output.

    Returns: The CSS as a string.
    """
    css = pkg_resources.resource_string('highlight_ranges', 'data/style.css')
    return css.decode()


def get_css(css_file=None):
    """Get the CSS to use for pygmentized HTML output.

    If `css_file` is `None`, this simply returns the result of `default_css()`.
    If `css_file` is provided, this appends the contents of that file to the
    default CSS.

    Args: 
        css_file: A file containing extra CSS to use.

    Returns: The CSS as a string.
    """
    css = default_css()

    if css_file is not None:
        with open(css_file, mode='rt') as handle:
            css += handle.read()

    return css
