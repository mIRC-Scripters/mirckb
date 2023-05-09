On Vcmd
=======

The on VCMD event triggers when the Speech recognition software matches a word you have spoken to a word in a list of words.

Synopsis
--------

.. code:: text

    ON <level>:VCMD:<*|#|?|@>:<commands>

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <*|#|?|@>
      - The location from which you want to listen for spoken word.
    * - <commands>
      - The commands to be performed when the event listener's criteria is met.

Example
-------

.. code:: text

    alias vctest {
     if ($vcmdver == $null) halt
     vcmd -c on
     vcadd connect Dalnet, connect Efnet, connect Undernet, connect IRCnet
     vcadd Part Channel, Disconnect, List Commands, Moo Cow
    }
    
    on 1:vcmd:connect*:*:server $2
    on 1:vcmd:part channel:*:if ($active ischan) part $active
    on 1:vcmd:disconnect:*:quit
    on 1:vcmd:list commands:*:vcmd -l
    on 1:vcmd:moo cow:*:splay moo.wav
    on 1:vcmd:*:*:echo You said: $1-

Compatibility
-------------

.. compatibility:: 5.7

See also
--------

.. hlist::
    :columns: 4

    * :doc:`/vcmd </commands/vcmd>`
    * :doc:`/vcadd </commands/vcadd>`
    * :doc:`/vcrem </commands/vcrem>`
    * :doc:`$vcmdver </identifiers/vcmdver>`
    * :doc:`$vcmdstat </identifiers/vcmdstat>`
    * :doc:`$vcmd </identifiers/vcmd>`
