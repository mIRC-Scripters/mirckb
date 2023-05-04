/flist
======

**/flist** lists all open files, or those matching the specified name, which can be a :doc: `wildcard </intermediate/matching_tools.html#wildcard>` expression.

Synopsis
--------

.. code:: text

    /flist [name]

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
    * - name
      - a :doc: `wildcard </intermediate/matching_tools.html#wildcard>` expression

Example
-------

.. code:: text

    /flist
    /flist myhandle*

Compatibility
-------------

Added: mIRC v6.1 (17 Feb 2006)

See also
--------

.. hlist::
    :columns: 4

    * :doc: `$fopen </identifiers/$fopen>`
    * :doc: `$fread </identifiers/$fread>`
    * :doc: `$ferr </identifiers/$ferr>`
    * :doc: `$feof </identifiers/$feof>`
    * :doc: `/fclose </commands/fclose>`
    * :doc: `/fopen </commands/fopen>`
    * :doc: `/fseek </commands/fseek>`
    * :doc: `/fwrite </commands/fwrite>`
