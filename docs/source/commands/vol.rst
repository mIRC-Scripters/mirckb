/vol
====

The **/vol** command lets you change the volume on your system. The /vol command can also be used to mute the system volume.

.. note:: originally on Windows, you could set the volume/mute setting for different audio type: wave, midi, and mp3. This is why mIRC had the -wmp switches, to change those different volume/mute settings. Since Windows 7, this is no longer the case, only the master volume remains. But you can now change the volume/mute setting per application in Windows. mIRC does not have a way to change the volume/mute setting per application; using the -wmp switches now only change the volume/mute setting for the mIRC application.

Synopsis
--------

.. code:: text

    /vol -wmpvuN [volume]

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -w
      - Changes the waves volume (or the mIRC's volume on Windows 7+)
    * - -m
      - Changes the midis volume (or the mIRC's volume on Windows 7+)
    * - -p
      - Changes the mp3s volume (or the mIRC's volume on Windows 7+)
    * - -v
      - Changes the master volume
    * - -uN
      - Changes mute setting, N = 1 for muting, N = 2 for unmuting, this switch has to be used with at least one of the others switches

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - [volume]
      - a number ranging from 0 to 65535

Example
-------

.. code:: text

    ;mute the master volume
    /vol -vu1

Compatibility
-------------

Added: mIRC v5.8 (14 Dec 2000)

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
    * :doc:`/splay </commands/splay>`
