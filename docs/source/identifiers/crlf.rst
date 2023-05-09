$crlf
=====

The $crlf identifier concatenates both the carriage return and linefeed characters into a single character line-break.

Synopsis
--------

.. code:: text

    $crlf

Parameters
----------

None

Example
-------

Create a simple input box that uses $crlf to break to a new line:

.. code:: text

    //noop $input(And then the word "suddenly" $+ $crlf $+ suddenly appeared on a new line!)

Compatibility
-------------

.. compatibility:: 5.4

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$cr </identifiers/cr>`
    * :doc:`$lf </identifiers/lf>`

