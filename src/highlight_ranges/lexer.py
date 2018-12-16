from pygments.lexers import get_lexer_by_name
from pygments.lexers.python import PythonLexer
from pygments.token import Generic


def get_lexer_class(lexer_name):
    base_lexer = get_lexer_by_name(lexer_name)

    # TODO: Is there are more direct way to get this class?
    base_lexer_class = type(base_lexer)

    class SporRangeLexer(base_lexer_class):
        HIGHLIGHT_RANGE = (20, 30)

        name = 'Spor Ranges'
        aliases = ['spor-ranges']
        filenames = ['*.*']

        def get_tokens_unprocessed(self, text):
            for index, token, value in PythonLexer.get_tokens_unprocessed(self, text):
                if index >= self.HIGHLIGHT_RANGE[0] and index <= self.HIGHLIGHT_RANGE[1]:
                    yield index, Generic.Emph, value
                else:
                    yield index, token, value

    return SporRangeLexer
