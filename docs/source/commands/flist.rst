/flist
======

The **/flist** command lists all open files, or those matching the specified name, which can be a wildcard expression.

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
      - a wildcard expression

Example
-------

.. code:: text

    /flist
    /flist myhandle*

Compatibility
-------------

Added: mIRC v6.1 (29 Aug 2003)

.. note:: Unless otherwise stated, this was the date of original functionality. Further enhancements may have been made in later versions.

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$fopen </identifiers/fopen>`
    * :doc:`$fread </identifiers/fread>`
    * :doc:`$ferr </identifiers/ferr>`
    * :doc:`$feof </identifiers/feof>`
    * :doc:`/fclose <fclose>`
    * :doc:`/fopen <fopen>`
    * :doc:`/fseek <fseek>`
    * :doc:`/fwrite <fwrite>`
