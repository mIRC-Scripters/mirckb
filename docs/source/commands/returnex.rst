/returnex
=========

The **/returnex** command immediately leaves the current subroutine and returns a given value back to the calling routine (if one exists). This command performs the same operation as :doc:`/return </commands/return>` with the exception of how it handles spaces. All spaces, including leading, trailing, and multiple, are retained. (Normally multiple spaces are collapsed into a single space and leading and trailing spaces are trimmed off).

This command was added undocumented mainly to allow people to call an identifier in the subtext parameter of :doc:`$regsubex </identifiers/regsubex>` , without seeing their returned value missing spaces but you can use it for that purpose anywhere.

Synopsis
--------

.. code:: text

    /returnex [value]

Switches
--------

None

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - [value]
      - The value to return to the calling routine

Example
-------

.. code:: text

    alias space_example {
    ; Prints 9: <space>A<space><space>B<space><space>C<space>
    echo -a $len($preserve_space)

    ; Prints 5: A<space>B<space>C
    echo -a $len($strip_space)
    }

    ; Return with the spaces intact
    alias preserve_space returnex $get_abc

    ; Collaps spaces
    alias strip_space return $get_abc

    ; Just an example string "<space>A<space><space>B<space><space>C<space>"
    alias get_abc returnex $+($chr(32), A, $chr(32), $chr(32), B, $chr(32), $chr(32), C, $chr(32))

Compatibility
-------------

Added: mIRC v6.2 (23 Nov 2006)

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$result </identifiers/result>`
    * :doc:`/alias </commands/alias>`
    * :doc:`/return </commands/return>`
