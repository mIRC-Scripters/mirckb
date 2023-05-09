On Nosound
==========

The ON NOSOUND event triggers when a remote user attempts to send a /sound command - mIRC|sound request and the file does not exist on the local mIRC system.

This event fills the :doc:`$filename </identifiers/filename>` identifier with the file name of the attempted sound.

Synopsis
--------

.. code:: text

    ON <level>:NOSOUND:<commands>

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

Example
-------

Send a message to the user when sound file does not exist:

.. code:: text

    ON *:NOSOUND:msg $nick Unfortunately, I do not have: $filename

Compatibility
-------------

.. compatibility:: 4.6

See also
--------

.. hlist::
    :columns: 4

    * :doc:`playing music </other/playing_music>`
    * :doc:`on midiend </events/on_midiend>`
    * :doc:`on mp3end </events/on_mp3end>`
    * :doc:`on waveend </events/on_waveend>`
    * :doc:`$inmidi </identifiers/inmidi>`
    * :doc:`$insong </identifiers/insong>`
    * :doc:`$inwave </identifiers/inwave>`
    * :doc:`$sound </identifiers/sound>`
    * :doc:`$vol </identifiers/vol>`
    * :doc:`/splay </commands/splay>`
    * :doc:`/vol </commands/vol>`

