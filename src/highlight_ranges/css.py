"""Support for styling the output with CSS.
"""
import pkg_resources


def default_css():
    css = pkg_resources.resource_string('highlight_ranges', 'data/style.css')
    return css.decode()


def get_css(css_file=None):
    css = default_css()

    if css_file is not None:
        with open(css_file, mode='rt') as handle:
            css += handle.read()

    return css
