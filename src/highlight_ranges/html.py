from io import StringIO
import pkg_resources

from pygments import highlight
from pygments.formatters.html import HtmlFormatter
from spor.repository import open_repository

from highlight_ranges.spor_filter import SporRangeFilter


def get_html(css, div):
    template = pkg_resources.resource_string(
        'highlight_ranges', 'data/template.html')
    return template.decode().format(css=css, code=div)


def get_div(lexer, source_path):
    with source_path.open(mode='rt') as handle:
        code = handle.read()

    repo = open_repository(source_path)

    anchors = (anchor for _, anchor in repo.items() if anchor.file_path == source_path.absolute())

    lexer.add_filter(SporRangeFilter(anchors))

    highlighted = StringIO()
    highlight(
        code,
        lexer=lexer,
        formatter=HtmlFormatter(),
        outfile=highlighted)

    return highlighted.getvalue()

