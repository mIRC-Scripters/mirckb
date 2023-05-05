/sockwrite
==========

The **/sockwrite** command allows you to send data to a TCP socket connection previously opened with :doc:`/sockopen </commands/sockopen_commands>` (See :doc:`tCP sockets </advanced/sockets.html#tcp-socket>` ).
You can specify a :ref:`matching_tools-wildcard` for the name to send the data to all matching sockets.

When the data has been sent, the :doc:`on sockwrite </events/on_sockwrite>` event triggers.

mIRC will queue your request up to 16384 bytes, you must check how many bytes is the send buffer with :doc:`$sock </identifiers/sock>` ().sq before trying to queue on a socket

.. note:: If the queue is empty, (first /sockwrite ever for example), you can send more than that limit and it will be sent as chunk of the send queue limit or less.

Synopsis
--------

.. code:: text

    /sockwrite -abnt <name> [numbytes] <text|%var|&binvar>

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -b
      - Indicates that you are specifying the numbytes value which is the number of bytes you want send, the full line is sent otherwise
    * - -n
      - Appens a :doc:`$crlf </identifiers/crlf>` to the line being sent if it's not a &binvar and does not already end with a $crlf
    * - -t
      - Forces mIRC to send anything beginning with a & as plain text
    * - -a
      - Prevents characters in the range 0-255 from being UTF-8 encoded as long as the line only contains characters in the range 0-255

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <name>
      - The socket name.
    * - [numbytes]
      - If -b has been specified, indicates the number of bytes you want to send.
    * - <text|%var|&binvar>
      - The message you want to send, can be a binary variable.

.. note:: if /sockwrite fails, :doc:`$sockerr </identifiers/sockerr>` is set as well as :doc:`$sock </identifiers/sock>` ().wserr and :doc:`$sock </identifiers/sock>` ().wsmsg inside the :doc:`on sockwrite </events/on_events/on_sockwrite>` event.

Example
-------

See the page for the :doc:`on sockwrite </events/on_events/on_sockwrite>` event for more informations and examples about /sockwrite

Compatibility
-------------

Added: mIRC v5.3 (04 Jan 1998)

See also
--------

.. hlist::
    :columns: 4

    * :doc:`/sockopen </commands/sockopen>`
    * :doc:`/sockread </commands/sockread>`
    * :doc:`/sockmark </commands/sockmark>`
    * :doc:`on sockwrite </events/on_sockwrite>`
    * :doc:`on sockread </events/on_sockread>`
    * :doc:`$sockerr </identifiers/sockerr>`
    * :doc:`$sock() </identifiers/sock>`
