$aop
====

The $aop identifier allows you to get data from your /aop command - mIRC|Auto-Op list in mIRC.

Synopsis
--------

.. code:: text

    $aop(address/N)[.property]

.. note:: $aop by itself returns ``$true`` if auto-op is enabled, otherwise it returns ``$false``.

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - address
      - Returns any match based on the specified address from the auto-op list.
    * - N
      - Returns any match in the auto-op list based on the Nth entry in the list. If N is 0, the total amount of addresses in the auto-op list will be returned.

Properties
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Property
      - Description
    * - type
      - If a match is found, returns the list of channels associated with its auto-op.
    * - network
      - Returns which network the auto-op is associated with.

Examples
--------

Echo to the active window whether or not auto-op is enabled

.. code:: text

    //echo -a $aop

Echo to the active window the total number of addresses in the auto-op list

.. code:: text

    //echo -a $aop(0)

Echo to the active window the network that the match is associated with

.. code:: text

    //echo -a $aop(*testhost.com).network

Compatibility
-------------

.. compatibility:: 5.9

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$avoice </identifiers/avoice>`
    * :doc:`$auto </identifiers/auto>`
    * :doc:`/aop </commands/aop>`
    * :doc:`/avoice </commands/avoice>`
    * :doc:`/ignore </commands/ignore>`
    * :doc:`/pop </commands/pop>`
    * :doc:`/pvoice </commands/pvoice>`

