$inmp3
======

.. attention:: This feature has essentially been replaced by :doc:`$insong </identifiers/insong>`

$inmp3 return $true/$false if an mp3 is playing or information about the mp3 via some properties.

.. note:: This identifier is also a part of the Playing music - mIRC|playing music section.

Synopsis
--------

.. code:: text

    $inmp3

Parameters
----------

None

Properties
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Property
      - Description
    * - .fname
      - Returns the filename of the mp3 currently playing
    * - .pos
      - Returns the position of the current mp3 playing
    * - .length
      - Returns the length of the mp3.
    * - .pause
      - Returns $true if an mp3 is currently paused, $false otherwise

Example
-------

.. code:: text

    //echo -a $inmp3

Compatibility
-------------

.. compatibility:: 5.8

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
    * :doc:`$inwave </identifiers/inwave>`
    * :doc:`$sound </identifiers/sound>`
    * :doc:`$vol </identifiers/vol>`
    * :doc:`/splay </commands/splay>`
    * :doc:`/vol </commands/vol>`
