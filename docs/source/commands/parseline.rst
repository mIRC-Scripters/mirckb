/parseline
==========

**/parseline** can be used to inject lines as though mIRC was receiving or sending them from/to IRC servers. It can also be used to modify the line being received/sent from the :doc: `on parseline </events/on_parseline>` event.

**Warning**: This feature should only be used, for example, to support features and/or protocols that mIRC does not already support, not to modify standard lines. mIRC maintains internal states based on incoming and outgoing lines. If lines are modified, mIRC may not work correctly

Synopsis
--------

.. code:: text

    /parseline -aiotbpnuN [text|&binvar]
    /parseline -q[aiotbpnuN] [text|&binvar]

Switches
--------

Required

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -i or -o
      - -o** - Specify an input or output message
    * - -t or -b
      - -b** - Specify a text or binvar parameter

Optional

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -q
      - Can be used to add a new line to the end of the in/out queue, they are processed after the end of the script execution.

.. note:: Without -q, you're changing the current line from the :doc: `on parseline </events/on_parseline>` event, you'll get an error otherwise.

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -a
      - modifier for -t, codepoints 128-255 are not encoded to UTF8 if no codepoint above 255 is found
    * - -p
      - Used with -q, indicate the line must trigger on parseline
    * - -n
      - Add a :doc: `$crlf </identifiers/$crlf>` to the end of the line if the line doesn't already end with a $crlf
    * - -uN
      - Enable/Disable utf8 encoding/decoding of the line. Use N = 1 to enable, 0 to disable

.. note:: A script must check $parseutf to know whether mIRC will be UTF-8 encoding/decoding a line.

** For outgoing lines, if $parseutf is $true, mIRC will UTF-8 encode the line before sending it to the server after the PARSELINE event. You can prevent this by using -u0.

** For incoming lines, if $parseutf is $true, after the PARSELINE event, mIRC will UTF-8 decode the line before processing it. You can prevent this by using -u0.

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - [text|&binvar]
      - The text or binvar parameter depending on if you used the -t or -b switch

Example
-------

.. code:: text

    //parseline -qitn bipartite.nj.us.SwiftIRC.net PRIVMSG #mIRCScripting :test

Keep a window open after parting the channel is now possible:

.. code:: text

    on *:PARSELINE:in:?* PART #*:if ($gettok($mid($parseline,2),1,33) == $me) .parseline -it

.. note:: You'll have to use "/parseline -qot join #channel" to join the channel back, this is because /join does not /join if the window exist, assuming you're on the channel

Compatibility
-------------

Added: mIRC v7.42 (17 Jul 2015)

See also
--------

.. hlist::
    :columns: 4

    * :doc: `on parseline </events/on_parseline>`
    * :doc: `$parseutf </identifiers/$parseutf>`
