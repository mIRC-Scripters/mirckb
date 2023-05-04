/ialclear
=========

The **ialclear** command clears the IAL (Internal Address List).

Synopsis
--------

.. code:: text

    /ialclear [nickname]

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
    * - [nickname]
      - If specified, the IAL is only cleared for that nickname, otherwise the whole list is cleared

Example
-------

.. code:: text

    ;Clear the IAL
    /ialclear

Compatibility
-------------

Added: mIRC v5.9 ()

See also
--------

.. hlist::
    :columns: 4

    * :doc: `/ial </commands/ial>`
    * :doc: `/clearial </commands/clearial>`
    * :doc: `/ialmark </commands/ialmark>`
    * :doc: `$ial </identifiers/$ial>`
    * :doc: `$address </identifiers/$address>`
    * :doc: `$ialchan </identifiers/$ialchan>`
