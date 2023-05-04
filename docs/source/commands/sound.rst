/sound
======

The **/sound** command allows you to send a sound to a channel/nickname with an optional message. Nicknames must have the Accept sound request option enabled to be able to play the sound as well as having the sound file.

Synopsis
--------

.. code:: text

    /sound [on|off|nick/channel] <sound_filename> [message]

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
    * - [on|off|nick/channel]
      - Either turn the Accept sound request message on/off, or send the sound request to the specified nick/channel.
    * - <sound_filename>'
      - The sound to be played, must be in any subfolder of the sound directory, the sound directory included.
    * - [message]
      - The optional message you want to send as well as the send request, this will be sent as an action message ( :doc:`/me </commands/me>` ).

Example
-------

Compatibility
-------------

Added: mIRC v3.7 (24 Oct 1995)

See also
--------
