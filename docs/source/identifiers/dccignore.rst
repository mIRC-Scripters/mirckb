$dccignore
==========

The $dccignore identifier will return either :doc:`$true </identifiers/true>` or :doc:`$false </identifiers/false>` depending on the the DCC ignore option within mIRC. This identifier can also be used to retrieve certain DCC ignore file type options, also from within the DCC ignore options window.

Synopsis
--------

.. code:: text

    $dccignore[(N/filename)]

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - N
      - Matches the Nth file name/ignore type within the DCC ignore options list
    * - filename
      - This can be a :ref:`matching_tools-wildcard`, and matches the specific filename/extension in the DCC ignore options list

Example
-------

Echo to the active window the total number of DCC ignore list items:

.. code:: text

    //echo -a $dccignore(0)

Echo to the active window if *.exe is in the DCC ignore list:

.. code:: text

    //echo -a $dccignore(*.exe)

Echo to the active window the last item in the DCC ignore list:

.. code:: text

    //echo -a $dccignore($dccignore(0))

Compatibility
-------------

.. compatibility:: 5.61

See also
--------

.. hlist::
    :columns: 4

    * :doc:`/dcc </commands/dcc>`

