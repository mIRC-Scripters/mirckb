$cr
===

The $cr identifier returns the carriage return character, which is the same as $chr(13), which carries the line into a break for a new line.

Synopsis
--------

.. code:: text

    $cr

Parameters
----------

None

Example
-------

Create a simple input box that uses $cr to break to a new line:

.. code:: text

    //noop $input(The word "will" $+ $cr $+ will be on a newline)

Compatibility
-------------

.. compatibility:: 4.52

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$crlf </identifiers/crlf>`
    * :doc:`$lf </identifiers/lf>`

