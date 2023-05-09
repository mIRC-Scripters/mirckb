/vnotice
========

The /vnotice command allows you to send a notice to all voices on a channel using a /NOTICE +#channel format if the WALLVOICE token is seen in raw 005, otherwise mIRC uses its own method to send to all voices. mIRC will display '+#channel: message' in the active window.

Synopsis
--------

.. code:: text

    /vnotice [channel] <text>

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

    * :doc:`/onotice </commands/onotice>`

