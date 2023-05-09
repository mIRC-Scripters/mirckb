$comchan
========

$comchan is used to return the common channels that both the local mIRC client, and a remote user, share.

Synopsis
--------

.. code:: text

    $comchan(nick,N)[.property]

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Argument
      - Description
    * - nick
      - The nickname of the user to find common channels with
    * - N
      - The Nth common channel that both the local and remote clients share

Properties
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Property
      - Description

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Argument
      - Description
    * - op
      - Returns :doc:`$true </identifiers/true>` if the local mIRC client is opped on the matched channel
    * - help
      - Returns :doc:`$true </identifiers/true>` if the local mIRC client is a helper on the matched channel
    * - voice
      - Returns :doc:`$true </identifiers/true>` if the local mIRC client is voiced on the matched channel
    * - owner
      - Returns :doc:`$true </identifiers/true>` if the local mIRC client is owner on the matched channel

Example
-------

Echo the common channels of the local client, and a remote user nicknamed myFriend:

.. code:: text

    //echo -a $comchan(myFriend,0)

Echo the common channels of the local client, and a remote user nicknamed ''myFriend''', and if the local client is opped on the first match:

.. code:: text

    //echo -a Total common channels: $comchan(myFriend,0) --- Is opped on $comchan(myFriend,1) $+ : $comchan(myFriend,1).op

Compatibility
-------------

.. compatibility:: 5.0

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$channel </identifiers/channel>`
    * :doc:`$nick </identifiers/nick>`

