from pygments.lexers.python import PythonLexer
from pygments.token import Error


class SporRangeLexer(PythonLexer):
    HIGHLIGHT_RANGE = (15, 18)

    name = 'Spor Ranges'
    aliases = ['spor-ranges']
    filenames = ['*.*']

    def get_tokens_unprocessed(self, text):
        for index, token, value in PythonLexer.get_tokens_unprocessed(self, text):
            if index >= self.HIGHLIGHT_RANGE[0] and index <= self.HIGHLIGHT_RANGE[1]:
                yield index, Error, value
            else:
                yield index, token, value
