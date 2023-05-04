/noop
=====

The **/noop** command simply discards all the values after evaluating its arguments like mIRC would in an ordinary command. This is useful for identifiers that return a value but you do not wish to do anything with these values.

Synopsis
--------

.. code:: text

    /noop [args]

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
    * - [args]
      - Arguments to evaluate

Example
-------

.. code:: text

    alias noop_example {
    ; discard the value we get from $tip
    noop $tip(Example, Hello, Hello there)
    }

Compatibility
-------------

Added: mIRC v6.17 (17 Feb 2006)

See also
--------

.. hlist::
    :columns: 4

    * :doc: `$eval </identifiers/$eval>`
    * :doc: `$ </identifiers/$>`
    * :doc: `$evalnext </identifiers/$evalnext>`
    * :doc: `/scid </commands/scid>`
    * :doc: `/scon </commands/scon>`
