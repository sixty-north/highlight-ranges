from io import StringIO
import sys

from pygments import highlight
from pygments.formatters.html import HtmlFormatter

from pygments_ranges.lexer import SporRangeLexer

# TODO: Let user specify a base lexer. Build a SporRangeLexer from it.
# TODO: Let use specify CSS file name.

input_filename = sys.argv[1]

with open(input_filename, mode='rt') as handle:
    code = handle.read()

highlighted = StringIO()

highlight(
    code,
    lexer=SporRangeLexer(),
    formatter=HtmlFormatter(),
    outfile=highlighted)

template = """<html>
<head>
    <link rel="stylesheet" type="text/css" href="spor_range.css">
</head>
<div class="highlight">
    <pre><span></span><span class="k">def</span> <span class="nf">foo</span><span class="p">():</span>
    <span class="err">return</span> <span class="mi">1</span> <span class="o">+</span> <span class="mi">2</span>
</pre>
</div>

</html>
"""

output = template.format(highlighted)
print(output)
