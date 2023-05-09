$lf
===

The $lf identifier returns the linefeed character, which is the same as $chr(10), which feeds the line into a break for a new line.

Synopsis
--------

.. code:: text

    $lf

Parameters
----------

None

Example
-------

Create a simple input box that uses $lf to break to a new line:

.. code:: text

    //noop $input(The word "appears" $+ $cr $+ appears suddenly on a newline)

Compatibility
-------------

.. compatibility:: 4.52

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$cr </identifiers/cr>`
    * :doc:`$crlf </identifiers/crlf>`

