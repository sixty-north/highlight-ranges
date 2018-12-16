import pkg_resources


def default_pygments_css():
    css = pkg_resources.resource_string('highlight_ranges', 'data/style.css')
    return css.decode()


def default_css():
    css = default_pygments_css()
    return css + """
    .ge {
        background-color: red;
    }
    """


def get_css(css_file=None):
    if css_file is None:
        return default_css()

    with open(css_file, mode='rt') as handle:
        return handle.read()
