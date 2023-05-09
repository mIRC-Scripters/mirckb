$inmidi
=======

.. note:: This identifier is also a part of the Playing music - mIRC|playing music section.

$inmidi returns whether or not a midi file is currently playing.

Synopsis
--------

.. code:: text

    $inmidi

Properties
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Property
      - Description
    * - fname
      - Returns the file name of the currently playing midi file.
    * - pos
      - Returns the current position that the player is playing the midi at.
    * - length
      - Returns the full length of the currently playing midi file.
    * - pause
      - Returns ''$true'' if the currently playing midi file is paused, else it returns ''$false''.

Example
-------

Echo whether or not a midi file is playing to the active window

.. code:: text

    //echo -a $inmidi

Compatibility
-------------

.. compatibility:: 5.0

See also
--------

.. hlist::
    :columns: 4

* Playing Music - mIRC|Playing Music
* On midiend - mIRC|ON MIDIEND
* On mp3end - mIRC|ON MP3END
* On nosound - mIRC|ON NOSOUND
* On waveend - mIRC|ON WAVEEND
    * :doc:`$insong </identifiers/insong>`
    * :doc:`$inwave </identifiers/inwave>`
    * :doc:`$sound </identifiers/sound>`
    * :doc:`$vol </identifiers/vol>`
    * :doc:`/splay </commands/splay>`
    * :doc:`/vol </commands/vol>`

