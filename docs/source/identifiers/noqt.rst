$noqt
=====

$noqt returns the text string with single enclosure double-quotes removed.

Synopsis
--------

.. code:: text

    $noqt(text)

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
    * - text
      - Text string from which to remove single enclosure double quotes.

Properties
----------

None

Example
-------

Does not affect double-quotes within the text, only removes a single double-quote at the start/end of text.

.. code:: text

    //var %ini $qt($mircini) echo -a %ini | echo -a $noqt(%ini)
    ; 1st line returns path\filename of your mirc.ini with double-quotes around it.
    ; 2nd line shows filename with surrounding double-quotes removed

.. code:: text

    //echo -a $noqt("""Test""String)
    ; returns: ""Test""String
    ; No change to internal quotes, removes 1 double-quote from start of string, no alteration of string ending because no double-quote already present.

Compatibility
-------------

.. compatibility:: 6.17

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$qt </identifiers/qt>`

