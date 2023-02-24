/ial
====

The **/ial** command turns IAL (Internal Address List) on or off. If no on/off parameter is used, it will display the IAL status.

.. note:: This setting is not persistent across sessions and resets to on every time mIRC is run.

Synopsis
--------

.. code:: text

    /ial [on|off]

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
    * - [on|off]
      - Turns the IAL on/off.

Example
-------

.. code:: text

    ;Turns IAL off
    /ial off


Compatibility
-------------

Added: mIRC v4.7 (09 Dec 1996)

.. note:: Unless otherwise stated, this was the date of original functionality. Further enhancements may have been made in later versions.

See also
--------

.. hlist::
    :columns: 4

    * :doc:`/ialclear <ialclear>`
    * :doc:`/ialmark <ialmark>`
    * :doc:`$ial </identifiers/ial>`
    * :doc:`$address </identifiers/address>`
    * :doc:`$ialchan </identifiers/ialchan>`
