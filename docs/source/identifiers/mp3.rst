$mp3
====

.. attention:: This feature has essentially been replaced by :doc:`$sound </identifiers/sound>`

$mp3 returns various information about sound files

Synopsis
--------

.. code:: text

    $mp3(<type>)

Possible value for <type>:
* mp3 - Return the mp3 folder
* midi - Return the midi folder
* wave - Return the wave folder

.. code:: text

    $mp3(filename>)[.property]

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
      - Returns the mode: ''mono'', ''stereo'', etc.
    * - copyright
      - Returns any copyright information.
    * - private
      - Returns ''$true'' or ''$false'' for the private tag.
    * - crc
      - Returns ''$true'' or ''$false'' if crc is found.
    * - .id3
      - Returns the id3 tag information.
    * - .tag
      - Used to retrieve id3v2 information.
    * - .tags
      - Used to retrieve id3v2 information.

If used with a music filename, the above properties are available.

.. note:: Only mp3, ogg, and wma files currently support the following properties. Keep in mind that not all properties may have been set. Each property returns the id3v1 values. For id3v2, use the ''.tag'', and ''.tags'' properties.

Examples
--------

Echo the artist name of the currently playing mp3 file to the active window:

.. code:: text

    //echo -a $mp3($insong.fname).artist

Create a small alias that will open a window, @id3info, and echo some basic info about the currently playing song to it:

.. code:: text

    alias id3info {
    
      ; First, we check to make sure we currently have an mp3, ogg, or wma file playing
      if ($insong) {
    
        ; If the @id3info window is open, clear it, otherwise create it.
        $iif($window(@id3info),clear @id3info,window @id3info)
    
        echo @id3info Artist: $mp3($insong.fname).artist
        echo @id3info Track: $mp3($insong.fname).track
        echo @id3info Title: $mp3($insong.fname).title
        echo @id3info Album: $mp3($insong.fname).album
    
        ; The below calculation converts the milliseconds for the sound
        ; file length into the format mm:ss, or minutes:seconds. Note that
        ; this does not properly support lengths over 59 minutes and 59
        ; seconds long.
        echo @id3info Length: $replace($round($calc($mp3($insong.fname).length / 1000 / 60),2),.,:)
        echo @id3info Year: $mp3($insong.fname).year
      }
    }

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
    * :doc:`$vol </identifiers/vol>`
    * :doc:`/splay </commands/splay>`
    * :doc:`/vol </commands/vol>`

