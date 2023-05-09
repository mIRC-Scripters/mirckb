/raw
====

The /raw command toggles the raw events processing. With no parameters, the /raw command displays the current state (either disabled or enabled).  Alternatively, the /raw command can be used to send text to the server AS IS.

Synopsis
--------

.. code:: text

    /raw [on|off]
    /raw [-qn] <string>

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
    * - [on|off]
      - Enables or disables raw events processing
    * - <string>
      - The data to be sent to the server

Example
-------

To see the current state:

.. code:: text

    /remote

Which will print something like:

.. code:: text

    * Remote is on (Ctcps,Events,Raw)

/raw can also be used to send text to the server:

.. code:: text

    /raw PRIVMSG #mIRC :Hello World!

The command above is equivalent to /msg #mIRC Hello World.

Compatibility
-------------

.. compatibility:: 3.3

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
    * :doc:`/quote </commands/quote>`

