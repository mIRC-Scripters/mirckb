/splay
======

.. note:: This command is also a part of the :doc:`playing music </other/playing_music>` section.*

**/splay** can be used to play a number of common Windows sound files. Supported formats include, but sometimes are not limited to: *.wav*, *.mid*, *.mp3*, *.ogg*, and *.wma*.

Synopsis
--------

.. code:: text

    /splay -cwmpq [filename | stop | pause | resume | seek | skip] [pos]

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - c
      - Allows you to clear the play queue, except for the currently playing sound (which will continue to play).
    * - w
      - Tells the command you are specifying a *.wav* file to play.
    * - m
      - Tells the command you are specifying a *.mid* file to play.
    * - p
      - Tells the command you are specifying an *.mp3/.wma/.ogg* file to play.
    * - q
      - Specifies that the filename you desire to play should be placed in the queue, after the current sounds has played, and any preceding sounds in the play queue..

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - filename
      - the filename you wish to play
    * - stop
      - Stops the currently playing file.
    * - pause
      - Allows you to pause the currently playing sound file.
    * - resume
      - Allows you to resume the currently paused sound file.
    * - seek
      - Allows you to seek to a certain point in the currently playing file. See **[pos]** below.
    * - skip
      - Allows you to skip the currently playing sound file. If there are any files in the queue, the next file will begin to play.
    * - [pos]

.. note:: The seek position is in milliseconds. Keep in mind that 1-second = 1000-milliseconds.

Examples
--------

*'Play the file *myfile.mp3* located in the mIRC Sounds folder**

.. code:: text

    /splay -p myfile.mp3

**Stop the currently playing mp3**

.. code:: text

    /splay -p stop

**Stop all sound files**

.. code:: text

    /splay -pmw stop

**Seek to 1:03 in the currently playing mp3'''

.. code:: text

    /splay -p seek 60300

Compatibility
-------------

Added: mIRC v6.0 (16 Aug 2002)

See Also
--------

.. hlist::
    :columns: 4

    * :doc:`pLaying mUsic </other/playing_music>`
    * :doc:`oN mIDIEND </events/oN_midiend>`
    * :doc:`oN mP3eND </events/oN_mp3end>`
    * :doc:`oN nOSOUND </events/oN_nosound>`
    * :doc:`oN wAVEEND </events/oN_waveend>`
    * :doc:`$inmidi </identifiers/$inmidi>`
    * :doc:`$insong </identifiers/$insong>`
    * :doc:`$inwave </identifiers/$inwave>`
    * :doc:`$sound </identifiers/$sound>`
    * :doc:`$vol </identifiers/$vol>`
    * :doc:`/vol </commands/vol>`
