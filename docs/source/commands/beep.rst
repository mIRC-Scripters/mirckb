/beep
=====

The **/beep** command can be used to generate simple tones on the speaker. The command can also perform the beeps multiple times and with certain delay.

Synopsis
--------

.. code:: text

    /beep [number] [delay]

Switches
--------

None

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - [number]
      - Number of beeps, default to 3 if not specified.
    * - <delay>
      - Delay (in milliseconds), default to ~500ms if not specified.

Example
-------

.. code:: text

    ;Beep 3 times with a second delay
    /beep 3 1000

Compatibility
-------------

Added: mIRC v3.2 (02 May 1995)

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$vol </identifiers/vol>`
    * :doc:`$ebeeps </identifiers/ebeeps>`
    * :doc:`/ebeeps </commands/ebeeps>`
    * :doc:`/sound </commands/sound>`
    * :doc:`/speak </commands/speak>`
    * :doc:`/vol </commands/vol>`
