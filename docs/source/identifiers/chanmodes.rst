$chanmodes
==========

The $chanmodes identifier will return the supported list of channel modes available on the active network connection. If not connected, mIRC defaults to a standard value of ''bIe,k,l''.

.. note:: Any active connection window can use this identifier, not just an active channel.

Parameters
----------

None

Example
-------

Echo the current available channel modes to the active window:

.. code:: text

    //echo -a $chanmodes

Compatibility
-------------

.. compatibility:: 5.9

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$chantypes </identifiers/chantypes>`
    * :doc:`$nickmode </identifiers/nickmode>`
    * :doc:`$prefix </identifiers/prefix>`

