/tip
====

The **/tip** command can be used to change the text of an active balloon tip or close it instantly.

Synopsis
--------

.. code:: text

    /tip -c <name/N>
    /tip -t <name/N> [text]

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -c
      - Close the balloon tip
    * - -t
      - change the tip's text

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <name/N>
      - The name or the Nth active balloon tip.
    * - [text]
      - The new text for the tip.

Example
-------

.. code:: text

    ; /tip_countdown <seconds>
    ;
    alias tip_countdown {
    ; create balloon tip
    noop $tip(counter, Count Down, x, $$1)
    update_counter
    }
    alias update_counter {
    if ($tip(counter)) {
    var %seconds = $tip(counter).delay
    ; update the text
    tip -t counter %seconds $+(second, $iif(%seconds > 1, s),!)
    .timer -m 1 500 update_counter
    }
    }

Compatibility
-------------

Added: mIRC v6.3 (17 Oct 2008)

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$tip </identifiers/tip>`
    * :doc:`/tips </commands/tips>`
