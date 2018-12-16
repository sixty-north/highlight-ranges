from io import StringIO
import pkg_resources

from pygments import highlight
from pygments.formatters.html import HtmlFormatter

from highlight_ranges.spor_filter import SporRangeFilter


def get_html(css, div):
    template = pkg_resources.resource_string(
        'highlight_ranges', 'data/template.html')
    return template.decode().format(css=css, code=div)


def get_div(lexer, code):
    highlighted = StringIO()

    lexer.add_filter(SporRangeFilter())

    highlight(
        code,
        lexer=lexer,
        formatter=HtmlFormatter(),
        outfile=highlighted)

    return highlighted.getvalue()

