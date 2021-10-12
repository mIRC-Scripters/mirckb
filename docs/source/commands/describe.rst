/describe
=========

The **/describe** command sends an action message to a specific channel or person. This command is the same the **/me** command except you can set a destination channel or nick other then the active window.

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

.. note:: Unless otherwise stated, this was the date of original functionality. Further enhancements may have been made in later versions.

See also
--------

.. hlist::
    :columns: 4

    * :doc:`/ame <ame>`
    * :doc:`/amsg <amsg>`
    * :doc:`/me <me>`
    * :doc:`/msg <msg>`
    * :doc:`/qme <qme>`
    * :doc:`/qmsg <qmsg>`
    * :doc:`/say <say>`