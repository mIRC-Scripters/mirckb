/flood
======

The **/flood** command can be used to change the current flood settings for mIRC.

Synopsis
--------

.. code:: text

    /flood [<+|->L] [on|off|clear] <chars> <maxlines> <maxmessages> <ignoretime>

Switches
--------

'+' enable the specific flood option, while '-' disable it, L can be:

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - c
      - ctcp
    * - m
      - own messages
    * - o
      - op
    * - q
      - query
    * - w
      - whois

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - [on|off|clear]
      - turns flood protection on/off or clear the settings
    * - <chars>
      - maximum number of characters sent before it triggers <maxlines> - maximum number of buffered lines
    * - <maxmessages>
      - maximum number of message allowed per nick <ignoretime> - number of seconds nicks are ignored if they exceed <maxmessages>

Example
-------

.. code:: text

    /flood 200 10 2 30

Compatibility
-------------

Added: mIRC vmIRC 3.3, 3.4 ()

See also
--------
