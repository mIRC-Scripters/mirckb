/clearial
=========

.. warning:: This feature has essentially been replaced by **/ialclear** command.

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

.. note:: Unless otherwise stated, this was the date of original functionality. Further enhancements may have been made in later versions.

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$ial </aliases/ial>`
    * :doc:`$address </aliases/address>`
    * :doc:`/ial <ial>`
    * :doc:`/ialclear <ialclear>`
    * :doc:`/ialmark <ialmark>`