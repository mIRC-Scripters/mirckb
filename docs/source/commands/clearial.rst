/clearial
=========

.. attention:: This feature has essentially been replaced by :doc:`/ialclear </commands/ialclear>`.

The **/clearial** command clears the IAL; If a nickname is specified, it will clear that nickname's entry

Synopsis
--------

.. code:: text

    /clearial [nick]

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
    * - [nick]
      - Removes that nickname's IAL entry

Example
-------

.. code:: text

    ;Print out your own address
    //echo -a $qt($address($me,1))

    ;Remove your own nick from the IAL
    //clearial $me

    ;Print out your own address
    //echo -a $qt($address($me,1))

Compatibility
-------------

Added: mIRC v5.71 (07 May 2000)

See also
--------

.. hlist::
    :columns: 4

    * :doc: `$ial </identifiers/$ial>`
    * :doc: `$address </identifiers/$address>`
    * :doc: `/ial </commands/ial>`
    * :doc: `/ialclear </commands/ialclear>`
    * :doc: `/ialmark </commands/ialmark>`
