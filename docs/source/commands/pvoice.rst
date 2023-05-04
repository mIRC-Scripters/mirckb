/pvoice
=======

The **/pvoice** command performs a delayed voice on a nickname. The purpose of this command is to prevent a channel window filling up with voice mode changes whenever several users have the same nickname in their auto-voice section.

Before performing the voice it checks if the user is already voiced.

Synopsis
--------

.. code:: text

    /pvoice <delay> [#channel] <nickname>

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
    * - <delay>
      - mIRC will pause around <delay> seconds before performing the voice. If <delay> is zero, it does an immediate voice.
    * - [#channel]
      - If specified, the channel you want to voice the nickname on, otherwise the current channel is used
    * - <nickname>
      - The nickname you want to voice.

Example
-------

None

Compatibility
-------------

Added: mIRC v6.0 (16 Aug 2002)

See also
--------

.. hlist::
    :columns: 4

    * :doc:`/pop </commands/pop>`
