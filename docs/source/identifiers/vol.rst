$vol
====

$vol can be used to retrieve the current volume, from the Windows audio control, for the specified sound type parameter.

.. note:: This command is also a part of the Playing music - mIRC|playing music section.

Synopsis
--------

.. code:: text

    $vol(wave | midi | song | master)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - wave
      - Returns the current volume for wave files.
    * - midi
      - Returns the current volume for midi files.
    * - song
      - Returns the current volume for mp3, ogg, and wma files.
    * - master
      - This returns the master control volume setting for overall system volume.

Properties
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Property
      - Description
    * - mute
      - Returns the current ''mute'' settings for the specified sound type parameter.

Examples
--------

Echo the mute status for mp3 files to the active window:

.. code:: text

    //echo -a $vol(song).mute

Echo the current master system volume to the active window:

.. code:: text

    //echo -a $vol(master)

Compatibility
-------------

.. compatibility:: 6.0

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
    * :doc:`/splay </commands/splay>`
    * :doc:`/vol </commands/vol>`

