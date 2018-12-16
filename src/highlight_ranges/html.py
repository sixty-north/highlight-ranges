"""Support for generating pygmentized HTML from source code.
"""

from io import StringIO
import logging

from pygments import highlight
from pygments.formatters.html import HtmlFormatter
from spor.repository import open_repository

from highlight_ranges.spor_filter import SporRangeFilter

log = logging.getLogger(__name__)


TEMPLATE = """<html>
<head>
    <style>
    {css}
    </style>
</head>
{code}
</html>
"""


def get_html(css, elem):
    """Generate a complete HTML document with embedded CSS and an element in the body.

    Args:
        css: CSS string to embed in the document.
        elem: HTML element (as a string) to embed in the body of the document.

    Returns: The HTML as a string.
    """
    return TEMPLATE.format(css=css, code=elem)


def get_div(lexer, source_path):
    """Construct a pygmentized HTML div for the code in a file.

    This looks for a spor repository containing `source_path` and uses the anchors therein to 
    find ranges in the code to highlight.

    Args:
        lexer: The pygments lexer instance to use to lex the code.
        source_path: The `pathlib.Path` to the file containing the source.

    Returns: The div as a string.
    """
    with source_path.open(mode='rt') as handle:
        code = handle.read()

    try:
        repo = open_repository(source_path)

        anchors = (anchor for _, anchor in repo.items()
                   if anchor.file_path == source_path.absolute())
    except ValueError:
        log.warn("No spor repository found for {}".format(source_path))
        anchors = ()

    lexer.add_filter(SporRangeFilter(anchors))

    highlighted = StringIO()
    highlight(
        code,
        lexer=lexer,
        formatter=HtmlFormatter(),
        outfile=highlighted)

    return highlighted.getvalue()
