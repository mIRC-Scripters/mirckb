$insong
=======

.. note:: This command is also a part of the Playing music - mIRC|playing music section.

$insong returns whether or not an mp3, wma, or ogg file is currently playing.

Synopsis
--------

.. code:: text

    $insong

Properties
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Property
      - Description
    * - fname
      - Returns the file name of the currently playing mp3, wma, or ogg file.
    * - pos
      - Returns the current position that the player is playing the mp3, wma, or ogg at.
    * - length
      - Returns the full length of the currently playing mp3, wma, or ogg file.
    * - pause
      - Returns ''$true'' if the currently playing mp3, wma, or ogg file is paused, else it returns ''$false''.

Example
-------

Echo whether or not a mp3, wma, or ogg file is playing to the active window

.. code:: text

    //echo -a $insong

Compatibility
-------------

.. compatibility:: 6.0

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
    * :doc:`$inwave </identifiers/inwave>`
    * :doc:`$sound </identifiers/sound>`
    * :doc:`$vol </identifiers/vol>`
    * :doc:`/splay </commands/splay>`
    * :doc:`/vol </commands/vol>`
