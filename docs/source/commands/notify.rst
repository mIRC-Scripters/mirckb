/notify
=======

The /notify command manages the notify feature. You can manually force mIRC to update the notify list by typing /notify with no parameters. Note: Some IRC networks might let you use a full address instead of just a nickname, the only way to see if it works is to try it out.

Synopsis
--------

.. code:: text

    /notify [-shrln] <on|off|nickname> [network] [note]

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -s
      - shows the notify list window
    * - -h
      - hides the notify list window
    * - -r
      - removes the specified nickname from your notify list
    * - -l
      - displays your notify list
    * - -n
      - indicates that the network has been specified

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <on|off|nickname>
      - turns notify on/off or edit the nickname's entry, you can prefix the nickname with a '+' sign to get mIRC to do a /whois on the nickname, be careful with the frequency of use, might get you disconnected
    * - [network]
      - if -n is specified, the network the notify should work on
    * - [note]
      - if specified, specify a little note for each nickname

Example
-------

Compatibility
-------------

.. compatibility:: 3.9

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$notify </identifiers/notify>`

