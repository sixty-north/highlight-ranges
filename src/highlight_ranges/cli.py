"""highlight-ranges

Usage:
  highlight-ranges [options] <source-file>
  highlight-ranges (-h | --help)
  highlight-ranges --version

Options:
  -h --help        Show this screen
  --version        Show version
  --lexer=NAME     Name of the pygments lexer to use [default: python3]
  --div-only       Only generate the div snippet, not the full HTML
  --css-file=FILE  File containing extra CSS
"""
import sys

from docopt import docopt
from exit_codes import ExitCode
from pygments.lexers import get_lexer_by_name

from highlight_ranges.css import get_css
from highlight_ranges.html import get_div, get_html
from highlight_ranges.version import __version__


def get_code(source_file):
    with open(source_file, mode='rt') as handle:
        return handle.read()


def generate_output(arguments):
    code = get_code(arguments['<source-file>'])
    lexer = get_lexer_by_name(arguments['--lexer'])
    div = get_div(lexer, code)

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
