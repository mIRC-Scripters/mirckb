$prefix
=======

$prefix returns the list of channel user nickname prefixes (to indicate channel op, voice etc. status) supported on the active network connection. If not connected, mIRC defaults to a standard value of (ohv)@%+.

.. note:: Any active connection window can use this identifier, not just an active channel.

Parameters
----------

None

Example
-------

Echo the current available channel user nickname prefixes to the active window:

.. code:: text

    //echo -a $prefix

Compatibility
-------------

.. compatibility:: 5.9

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$chanmodes </identifiers/chanmodes>`
    * :doc:`$chantypes </identifiers/chantypes>`

