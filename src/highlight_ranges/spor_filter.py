from pygments.filter import Filter
from pygments.token import Generic


class SporRangeFilter(Filter):

    HIGHLIGHT_RANGE = (20, 30)

    # def __init__(self, **options):
    #     Filter.__init__(self, **options)
    #     self.class_too = get_bool_opt(options, 'classtoo')

    # TODO: I *think* we can split values at the point where they overlap
    # ranges, thereby letting us highlight the exact ranges specified instead of
    # on whole-token boundaries.
    def filter(self, lexer, stream):
        start = 0
        for ttype, value in stream:
            stop = start + len(value)
            if start >= self.HIGHLIGHT_RANGE[0] and stop <= self.HIGHLIGHT_RANGE[1]:
                ttype = Generic.Emph
            yield ttype, value

            start = stop
