/ialmark
========

The **ialmark** command marks the IAL entry for a nickname with the specified text with an optional alternate name for the mark. In effect, it's like a hashtable for each nick where each item must have a string attached to it

Synopsis
--------

.. code:: text

    /ialmark [-nrw] <nickname> [text]

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -n
      - the [name] of the mark. If -n is not used, the default name 'default' is used.
    * - -r
      - removes the mark
    * - -w
      - used with -rn to treat name as :doc:`wildcard </intermediate/matching_tools.html#wildcard>`

Marks can be accessed using :doc:`$ialmark(nick,n/name) </identifiers/$ialmark>` and properties 'name' and 'mark'.

Marks are removed if the nick is removed from the nicklist, either from no longer being in a channel with them, or by /ialclear or by being disconnected from that server. You cannot have a named-mark without it having a value. The mark does follow the nick to the new nick after a nick change.

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <nickname>
      - The nickname you want to mark
    * - [text]
      - The text you want to add. If not specified, the mark is cleared

Example
-------

.. code:: text

    ;If the nick Ouims is in the $ial, marks the nick Ouims with the named-mark 'default' containing the text 'test'
    /ialmark Ouims test
    ;If you are in the $ial, adds a mark to your nick named 'foo' containing the text 'bar'
    //ialmark -n $me foo bar
    ;Remove the named-mark 'default' (any parameters after the nick are ignored)
    //ialmark -r $me foo bar
    ;Remove the named-mark 'foo'
    //ialmark -rn $me foo
    ;removes all named wildcard mark names beginning with 'f'
    //ialmark -rnw $me f*
    ;removes all named wildcard marks beginning with 'd' including the default 'default'
    ;informs whether the named-mark 'default' exists, and if so whether it contains a mark value
    //ialmark $me
    ;informs whether the named-mark 'foo' exists, and if so whether it contains a mark value
    //ialmark $me foo

Compatibility
-------------

Added: mIRC v5.9 (15 Jun 2001)

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$ialmark </identifiers/$ialmark>`
    * :doc:`/ialclear </commands/ialclear>`
    * :doc:`/ial </commands/ial>`
    * :doc:`$ial </identifiers/$ial>`
    * :doc:`$address </identifiers/$address>`
    * :doc:`$fulladdress </identifiers/$fulladdress>`
    * :doc:`$ialchan </identifiers/$ialchan>`
