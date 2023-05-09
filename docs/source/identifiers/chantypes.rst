$chantypes
==========

The $chantypes identifier will return the supported list of channel prefix types available on the active network connection. If not connected, mIRC defaults to a standard value of ''#''.

.. note:: Any active connection window can use this identifier, not just an active channel.

Parameters
----------

None

Example
-------

Echo the current available channel prefix types to the active window:

.. code:: text

    //echo -a $chantypes

Compatibility
-------------

.. compatibility:: 5.9

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$chanmodes </identifiers/chanmodes>`
    * :doc:`$prefix </identifiers/prefix>`

