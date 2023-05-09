$qt
===

$qt returns the text string enclosed with double-quotes.

Synopsis
--------

.. code:: text

    $qt(<TEXT>)

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
    * - TEXT
      - Text string to ensure is enclosed in double quotes.

Properties
----------

None

Example
-------

Does not affect double-quotes within the text, only adds a double-quote to the start/end of TEXT if a double-quote is not already present.

.. code:: text

    //var %ini $qt($mircini) | echo -a %ini | echo -a $qt(%ini)
    ; returns path\filename of your mirc.ini with double-quotes around it.
    ; no change in 2nd line because quotes already present

.. code:: text

    //echo -a $qt("""Test""String)
    ; returns: """Test""String"
    ; No change to internal quotes, no alteration of string start because at least 1 quote already present, only added missing quote to end of string.

Compatibility
-------------

.. compatibility:: 6.17

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$noqt </identifiers/noqt>`

