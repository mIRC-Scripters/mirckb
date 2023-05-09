$inwave
=======

.. note:: This command is also a part of the Playing music - mIRC|playing music section.

$inwave returns whether or not a wav file is currently playing.

Synopsis
--------

.. code:: text

    $inwave[.property]

Properties
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Property
      - Description
    * - fname
      - Returns the file name of the currently playing wav file.
    * - pos
      - Returns the current position that the player is playing the wav at.
    * - length
      - Returns the full length of the currently playing wav file.
    * - pause
      - Returns ''$true'' if the currently playing wav file is paused, else it returns ''$false''.

Example
-------

Echo whether or not a wav file is playing to the active window

.. code:: text

    //echo -a $inwave

Echo the currently playing wav file's length to the active window

.. code:: text

    //echo -a $inwave.length

Compatibility
-------------

.. compatibility:: 5.3

See also
--------

.. hlist::
    :columns: 4

    * :doc:`playing music </other/playing_music>`
    * :doc:`on midiend </events/on_midiend>`
    * :doc:`on mp3end </events/on_mp3end>`
    * :doc:`on nosound </events/on_nosound>`
    * :doc:`on waveend </events/on_waveend>`
    * :doc:`$inmidi </identifiers/inmidi>`
    * :doc:`$insong </identifiers/insong>`
    * :doc:`$sound </identifiers/sound>`
    * :doc:`$vol </identifiers/vol>`
    * :doc:`/splay </commands/splay>`
    * :doc:`/vol </commands/vol>`

