/ialfill
========

The **/ialfill** command fills the IAL by sending a /WHO #channel to the server and processing the WHO reply.

Synopsis
--------

.. code:: text

    /ialfill <channel>

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -f
      - Force refill the IAL.

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <channel>
      - The channel to fill

Example
--------

.. code:: text

    /ialfill #fill

Compatibility
-------------

Added: mIRC v7.48 (15 Apr 2017)

.. note:: Unless otherwise stated, this was the date of original functionality. Further enhancements may have been made in later versions.

See also
--------

.. hlist::
    :columns: 4

    * :doc:`/ialclear <ialclear>`
    * :doc:`/ial <ial>`
    * :doc:`/ialmark <ialmark>`
    * :doc:`$ial </aliases/ial>`
    * :doc:`$address </aliases/address>`
    * :doc:`$ialchan </aliases/ialchan>`
