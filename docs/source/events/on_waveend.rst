On Waveend
==========

The ON WAVEEND event triggers whenever a WAV file has finished playing via the :doc:`/splay </commands/splay>` command.

This event fills the :doc:`$filename </identifiers/filename>` identifier, which will be set to the complete location and filename of the sound file that just ended.

Synopsis
--------

.. code:: text

    ON <level>:WAVEEND:<commands>

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <level>
      - The level for the event to trigger.
    * - <commands>
      - The commands to be performed when the event listener's criteria is met.

Examples
--------

Echo to the active window when the sound file has ended, including its filename:

.. code:: text

    ON *:WAVEEND:echo -a $nopath($filename) has ended

The example above will output results similar to the contents below:

.. code:: text

    Chopin - Four Scherzos.wav has ended

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
    * :doc:`$inmidi </identifiers/inmidi>`
    * :doc:`$insong </identifiers/insong>`
    * :doc:`$inwave </identifiers/inwave>`
    * :doc:`$sound </identifiers/sound>`
    * :doc:`$vol </identifiers/vol>`
    * :doc:`/splay </commands/splay>`
    * :doc:`/vol </commands/vol>`

