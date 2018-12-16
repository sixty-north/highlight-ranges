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
from pathlib import Path
import sys

from docopt import docopt
from exit_codes import ExitCode
from pygments.lexers import get_lexer_by_name

from highlight_ranges.css import get_css
from highlight_ranges.html import get_div, get_html
from highlight_ranges.version import __version__


def generate_output(source_path,
                    lexer_name,
                    div_only=False,
                    css_file=None):
    """Get the pygmentized HTML for the code in a file.

    Args:
        source_path: pathlib.Path referring to the file containing the source code.
        lexer_name: The name of the pygments lexer to use for parsing the code.
        div_only: Whether the output should be just a div (as opposed to an entire HTML document).
        css_file: Path to file containing CSS to append to the default.

    Returns: The generated output as a string.
    """
    lexer = get_lexer_by_name(lexer_name)
    div = get_div(lexer, source_path)

    if div_only:
        output = div
    else:
        css = get_css(css_file)
        output = get_html(css, div)
    return output


def main(argv=sys.argv):
    """Main command-line handler.

    Args:
        argv: List of command line arguments.

    Returns: The integer exit code suitable for returning from a program.
    """
    arguments = docopt(
        __doc__,
        argv=argv[1:],
        version='highlight-ranges {}'.format(__version__))

    output = generate_output(
        Path(arguments['<source-file>']),
        arguments['--lexer'],
        div_only=arguments['--div-only'],
        css_file=arguments['--css-file'])

    print(output)
    return ExitCode.OK


if __name__ == '__main__':
    sys.ext(main())
