================
highlight-ranges
================

Highlight ranges of code in `pygments <http://pygments.org>`_ output.

This provides a filter that uses `spor <http://github.com/abingham/spor>`_
anchors to determine which ranges of code to highlight in the pygmentized
output. You specify the ranges by creating anchors with metadata where the key
"highlight" is `true`, e.g.:

.. code-block:: json

    {"highlight": true}

Quick start
===========

First, install `highlight-ranges`. See the "Installation" section for details.

Create a directory somewhere and create a file named ``example.py`` with the
following contents:

.. code-block:: python

    def func(x):
        y = x * 4
        return y

Now initialize a spor repository and add an anchor that will highlight the
second line in the file::

    spor init
    spor add example.py 17 9 5

Finally, use the ``highlight-ranges`` filter to generate the pygmentized HTML
of the code::

    pygmentize -l python3 -f html -O full -F highlight-ranges:file=example.py example.py > example.html

If you open ``example.html`` in a browser, you should see the second line in the
code emphasized.

Installation
============

You can install from PyPI with `pip:`::

    pip install highlight-ranges

Or you can install from source::

    pip install .

Styling
=======

The filter marks highlighted ranges of code with the ``Generic.Emph`` type. From
a CSS point of view, this means you can style the highlights via the ``ge``
class.

Filter options
==============

file
  The file being pygmentized.