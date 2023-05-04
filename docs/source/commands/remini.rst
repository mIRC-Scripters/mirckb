/remini
=======

The **/remini** command deletes a whole section or a single item in an INI file

.. note:: you shouldn't be using this on the INI files used by mIRC but that should work.

Synopsis
--------

.. code:: text

    /remini <inifile> <section> [item]

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
    * - <inifile>
      - The filename of the ini file
    * - <section>
      - The section of the ini file you want to delete
    * - [item]
      - If speficied, the item you want to delete in the section, otherwise the whole section is deleted

Example
-------

Compatibility
-------------

Added: mIRC v4.6 (07 Sep 1996)

See also
--------

.. hlist::
    :columns: 4

    * :doc: `/writeini </commands/writeini>`
    * :doc: `$readini </identifiers/$readini>`
    * :doc: `$ini </identifiers/$ini>`
