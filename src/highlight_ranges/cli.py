"""highlight-ranges

Usage:
  highlight-ranges [options] <source-file>
  highlight-ranges (-h | --help)
  highlight-ranges --version

Options:
  -h --help        Show this screen.
  --version        Show version.
  --lexer=NAME     Name of the pygments lexer to use [default: python3]
  --div-only       Only generate the div snippet, not the full HTML
  --css-file=FILE  File contains the CSS to embed in the HTML
"""
from io import StringIO
import sys

from docopt import docopt
from exit_codes import ExitCode
from pygments import highlight
from pygments.formatters.html import HtmlFormatter

from highlight_ranges.css import get_css
from highlight_ranges.lexer import get_lexer_class
from highlight_ranges.version import __version__

HTML_TEMPLATE = """<html>
<head>
    <style>
    {css}
    </style>
</head>
{code}
</html>
"""


def get_div(lexer_class, code):
    highlighted = StringIO()

    highlight(
        code,
        lexer=lexer_class(),
        formatter=HtmlFormatter(),
        outfile=highlighted)

    return highlighted.getvalue()


def get_code(source_file):
    with open(source_file, mode='rt') as handle:
        return handle.read()


def get_html(css, div):
    return HTML_TEMPLATE.format(css=css, code=div)


def generate_output(arguments):
    code = get_code(arguments['<source-file>'])
    lexer_class = get_lexer_class(arguments['--lexer'])
    div = get_div(lexer_class, code)

    if arguments['--div-only']:
        output = div
    else:
        css = get_css(arguments['--css-file'])
        output = get_html(css, div)
    return output


def main(argv=sys.argv):
    arguments = docopt(
        __doc__,
        argv=argv[1:],
        version='highlight-ranges {}'.format(__version__))

    output = generate_output(arguments)

    print(output)
    return ExitCode.OK


if __name__ == '__main__':
    main()
