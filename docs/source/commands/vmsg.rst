/vmsg
=====

The /vmsg command allows you to send a message to all voices on a channel using a 

/msg +#channel format if the STATUS token is seen in raw 005 and it contains '+', otherwise mIRC uses its own method to send to all voices. mIRC will display '+#channel: message' in the active window.

Synopsis
--------

.. code:: text

    /vmsg [channel] <text>

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
    * - [channel]
      - the optional channel you want to use, otherwise the active channel is used
    * - <text>
      - The message you want to send

Example
-------

None

Compatibility
-------------

.. compatibility:: 7.53

See also
--------

.. hlist::
    :columns: 4

    * :doc:`/omsg </commands/omsg>`
