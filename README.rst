================
highlight-ranges
================

Highlight ranges of code in `pygments <http://pygments.org>`_ output.

This lets you specify ranges of source code that should be highlighted in the
output produced by pygments. You specify the ranges by creating `spor
<http://github.com/abingham/spor>`_ anchors with metadata where the key
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

Finally, use the ``highlight-ranges`` command to generate the pygmentized HTML
of the code::

    highlight-ranges example.py > example.html

If you open ``example.html`` in a browser, you should see the second line in the
code highlighted in red.

Installation
============

You can install from PyPI with `pip:`:

    pip install highlight-ranges

Or you can install from source::

    pip install .