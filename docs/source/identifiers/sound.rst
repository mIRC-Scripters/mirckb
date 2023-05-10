$sound
======

$sound is a powerful identifier that can be used to retrieve various information about sound files, including: directories which contain specific sounds file types, as well as ID3 tags associated with sound files which support them.

.. note:: This identifier is also a part of the :doc:`playing music </other/playing_music>` section.

Synopsis
--------

.. code:: text

    $sound(<type>)

Possible value for <type>:
* mp3 - Return the mp3 folder
* midi - Return the midi folder
* wave - Return the wave folder

$sound without parameters returns the default folder for music in general.

.. code:: text

    $sound(filename>)[.property]

Properties
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Property
      - Description
    * - album
      - Retrieves the specified album name sound file.
    * - title
      - Returns the song title for the file.
    * - artist
      - Returns the artist name for the file.
    * - year
      - Returns the year associated with the song release.
    * - comment
      - Returns any comments made by the file creator.
    * - genre
      - Grabs the genre for the file, if set.
    * - track
      - Retrieves the track number associated with the song.
    * - length
      - Returns the full length of the song in milliseconds.
    * - version
      - Gets the version number of the song, or track.
    * - bitrate
      - Returns the bitrate for the file.
    * - vbr
      - Gets the variable bit rate for the file.
    * - sample
      - Returns the sampling frequency.
    * - mode
      - Returns the mode: ``mono``, ``stereo``, etc.
    * - copyright
      - Returns any copyright information.
    * - private
      - Returns ``$true`` or ``$false`` for the private tag.
    * - crc
      - Returns ``$true`` or ``$false`` if crc is found.
    * - .id3
      - Returns the id3 tag information.
    * - .tag
      - Used to retrieve id3v2 information.
    * - .tags
      - Used to retrieve id3v2 information.

If used with a music filename, the above properties are available.

.. note:: Only mp3, ogg, and wma files currently support the following properties. Keep in mind that not all properties may have been set. Each property returns the id3v1 values. For id3v2, use the ``.tag``, and ``.tags`` properties.

Examples
--------

Echo the artist name of the currently playing mp3 file to the active window:

.. code:: text

    //echo -a $sound($insong.fname).artist

Create a small alias that will open a window, @id3info, and echo some basic info about the currently playing song to it:

.. code:: text

    alias id3info {
    
      ; First, we check to make sure we currently have an mp3, ogg, or wma file playing
      if ($insong) {
    
        ; If the @id3info window is open, clear it, otherwise create it.
        $iif($window(@id3info),clear @id3info,window @id3info)
    
        echo @id3info Artist: $sound($insong.fname).artist
        echo @id3info Track: $sound($insong.fname).track
        echo @id3info Title: $sound($insong.fname).title
        echo @id3info Album: $sound($insong.fname).album
    
        ; The below calculation converts the milliseconds for the sound
        ; file length into the format mm:ss, or minutes:seconds. Note that
        ; this does not properly support lengths over 59 minutes and 59
        ; seconds long.
        echo @id3info Length: $replace($round($calc($sound($insong.fname).length / 1000 / 60),2),.,:)
        echo @id3info Year: $sound($insong.fname).year
      }
    }

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
    * :doc:`$insong </identifiers/insong>`
    * :doc:`$inwave </identifiers/inwave>`
    * :doc:`$vol </identifiers/vol>`
    * :doc:`/splay </commands/splay>`
    * :doc:`/vol </commands/vol>`

