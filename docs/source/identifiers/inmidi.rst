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
      - Returns ``$true`` if the currently playing midi file is paused, else it returns ``$false``.

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

    * :doc:`playing music </other/playing_music>`
    * :doc:`on midiend </events/on_midiend>`
    * :doc:`on mp3end </events/on_mp3end>`
    * :doc:`on nosound </events/on_nosound>`
    * :doc:`on waveend </events/on_waveend>`
    * :doc:`$insong </identifiers/insong>`
    * :doc:`$inwave </identifiers/inwave>`
    * :doc:`$sound </identifiers/sound>`
    * :doc:`$vol </identifiers/vol>`
    * :doc:`/splay </commands/splay>`
    * :doc:`/vol </commands/vol>`

