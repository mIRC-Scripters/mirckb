$avoice
=======

The $avoice identifier allows you to get data from your /avoice command - mIRC|Auto-Voice list in mIRC.

Synopsis
--------

.. code:: text

    $avoice(address/N)[.property]

.. note:: $avoice by itself returns ``$true`` if auto-voice is enabled, otherwise it returns ``$false``.

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - address
      - Returns any match based on the specified address from the auto-voice list.
    * - N
      - Returns any match in the auto-voice list based on the Nth entry in the list. If N is 0, the total amount of addresses in the auto-voice list will be returned.

Properties
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Property
      - Description
    * - type
      - If a match is found, returns the list of channels associated with its auto-voice.
    * - network
      - Returns which network the auto-voice is associated with.

Examples
--------

Echo to the active window whether or not auto-voice is enabled

.. code:: text

    //echo -a $avoice

Echo to the active window the total number of addresses in the auto-voice list

.. code:: text

    //echo -a $avoice(0)

Echo to the active window the network that the match is associated with

.. code:: text

    //echo -a $avoice(*testhost.com).network

Compatibility
-------------

.. compatibility:: 5.9

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$aop </identifiers/aop>`
    * :doc:`$auto </identifiers/auto>`
    * :doc:`/aop </commands/aop>`
    * :doc:`/avoice </commands/avoice>`
    * :doc:`/ignore </commands/ignore>`
    * :doc:`/pop </commands/pop>`
    * :doc:`/pvoice </commands/pvoice>`

