/quote
======

The /quote command has been deprecated by the /raw command and can be used to send text to the server AS IS.

Synopsis
--------

.. code:: text

    /quote -qn <string>

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -q
      - Prevents the text being sent to the server from being printed to the window.
    * - -n
      - Prevents UTF-8 encoding when sending characters in the 0-255 range.

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <string>
      - The data to be sent to the server

Example
-------

.. code:: text

    ; send "héllo World!" without encoding the é in utf8
    /quote -nq PRIVMSG #mIRC :héllo World!

Compatibility
-------------

.. compatibility:: 4.5

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$remote </identifiers/remote>`
    * :doc:`$rawmsg </identifiers/rawmsg>`
    * :doc:`/ctcps </commands/ctcps>`
    * :doc:`/remote </commands/remote>`
    * :doc:`/commands </commands/commands>`
    * :doc:`/events </commands/events>`
    * :doc:`/raw </commands/raw>`

