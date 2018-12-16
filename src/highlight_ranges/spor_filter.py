from pygments.filter import Filter
from pygments.token import Generic


class SporRangeFilter(Filter):

    def __init__(self, anchors, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._anchors = tuple(anchors)

    def _should_highlight(self, start, stop):
        for anchor in self._anchors:
            if anchor.metadata.get('highlight', False):
                return (start >= anchor.context.offset and
                        stop <= (anchor.context.offset + len(anchor.context.topic)))

    def filter(self, lexer, stream):
        start = 0
        for ttype, value in stream:
            stop = start + len(value)
            if self._should_highlight(start, stop):
                ttype = Generic.Emph
            yield ttype, value

            start = stop
