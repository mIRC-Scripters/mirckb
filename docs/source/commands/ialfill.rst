/ialfill
========

The ialfill command fills the IAL by sending a /WHO #channel to the server and processing the WHO reply.

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
-------

.. code:: text

    /ialfill #fill

Compatibility
-------------

.. compatibility:: 7.48

See also
--------

.. hlist::
    :columns: 4

    * :doc:`/ialclear </commands/ialclear>`
    * :doc:`/ial </commands/ial>`
    * :doc:`/ialmark </commands/ialmark>`
    * :doc:`$ial </identifiers/ial>`
    * :doc:`$address </identifiers/address>`
    * :doc:`$ialchan </identifiers/ialchan>`

