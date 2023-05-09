/autojoin
=========

The /autojoin command is used in conjunction with the on Connect event (or the Perform option available in alt + o > options > perfom..) in order to delay or prevent auto-joining of channels. This also apply to rejoining of open channels windows during reconnect

Synopsis
--------

.. code:: text

    /autojoin -nsdN

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -n
      - Join now
    * - -s
      - Skip autojoin
    * - -dN
      - Delay auto-join for N seconds

Parameters
----------

None

Example
-------

.. code:: text

    on *:connect:{
      /* 
        5 seconds delay before we re-join the channels
        Enough time to perform more important things
      */
      autojoin -d5
    
      ns id FooBar
      mode $me -x
    }

.. note:: The max delay is 600 seconds, anything more resets to 600.

Compatibility
-------------

.. compatibility:: 6.17

See also
--------

.. hlist::
    :columns: 4

    * :doc:`/join </commands/join>`

