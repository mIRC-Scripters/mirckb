/describe
=========

The **/describe** command sends an action message to a specific channel or person. This command is the same the :doc:`/me command </commands/me>` except you can set a destination channel or nick other then the active window.

Synopsis
--------

.. code:: text

    /describe <nick|channel> <message>

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
    * - <nick|channel>
      - The destination channel or person for the action message
    * - <message>
      - The action message to be sent

Example
-------

.. code:: text

    ;When someone says 'moo', we will reply
    On *:Text:moo:#:{
    describe $chan moos back!
    }

Compatibility
-------------

Added: mIRC v3.1 (23 Apr 1995)

See also
--------

.. hlist::
    :columns: 4

    * :doc:`/ame </commands/ame>`
    * :doc:`/amsg </commands/amsg>`
    * :doc:`/me </commands/me>`
    * :doc:`/msg </commands/msg>`
    * :doc:`/qme </commands/qme>`
    * :doc:`/qmsg </commands/qmsg>`
    * :doc:`/say </commands/say>`
