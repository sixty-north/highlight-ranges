"""Examples of styles for highlighting.
"""

from pygments.style import Style
from pygments.styles.default import DefaultStyle
from pygments.token import Generic


class BlackOnRed(Style):
    """An example style that highlights with black text on a red background.

    It's based on the default pygments style.
    """
    default_style = ""
    styles = dict(DefaultStyle.styles)
    styles[Generic.Emph] = 'bg:#f00 #000'
