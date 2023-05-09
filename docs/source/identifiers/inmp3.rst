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

* Playing Music - mIRC|Playing Music
* On midiend - mIRC|ON MIDIEND
* On mp3end - mIRC|ON MP3END
* On nosound - mIRC|ON NOSOUND
* On waveend - mIRC|ON WAVEEND
    * :doc:`$inmidi </identifiers/inmidi>`
    * :doc:`$insong </identifiers/insong>`
    * :doc:`$inwave </identifiers/inwave>`
    * :doc:`$sound </identifiers/sound>`
    * :doc:`$vol </identifiers/vol>`
    * :doc:`/splay </commands/splay>`
    * :doc:`/vol </commands/vol>`
