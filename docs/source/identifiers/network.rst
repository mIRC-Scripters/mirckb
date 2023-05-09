$network
========

$network retrieves the current network name from the IRC server that mIRC is connected to.

Synopsis
--------

.. code:: text

    $network

Parameters
----------

None

Examples
--------

.. code:: text

    ; Create an alias that echos the current
    ; network to the active window
    alias netPlease { echo -a The current network is: $network }

The above command can be used by typing the following into the mIRC command-line:

.. code:: text

    /netPlease

Compatibility
-------------

.. compatibility:: 5.5

See also
--------

.. hlist::
    :columns: 4

    * :doc:`on connect </events/on_connect>`
    * :doc:`on connectfail </events/on_connectfail>`
    * :doc:`on disconnect </events/on_disconnect>`
    * :doc:`$server </identifiers/server>`

