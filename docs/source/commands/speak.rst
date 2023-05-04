/speak
======

The **/speak** command is used to allow mIRC to speak text audibly.

Synopsis
--------

.. code:: text

    /speak -spclu [speed] [pitch] [text]

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - s
      - -Allows you to specify the speed for the text to be spoken (0 - 100).
    * - p
      - Controls the pitch at which the text is spoken (0 - 100).
    * - c
      - Clear all queued lines of speaking.
    * - l
      - Apply the lexicon settings in the speech dialog.
    * - u
      - Apply the option settings in the speech dialog.

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - speed
      - If the **-s** switch is invoked, this parameter is where you specify the speed at which the text should be spoken (0 - 100).
    * - pitch
      - If the **-p** switch is invoked, this parameter is where you specify the pitch at which the text should be spoken (0 - 100).
    * - text
      - This is the text to be spoken by the speaking system.

Examples
--------

'''Speak the words 'Hello World!'**

.. code:: text

    /speak Hello World!

**Speak 'Hi there!' at *30* speed with a pitch of *50*'''

.. code:: text

    /speak -sp 30 50 Hi there!

Compatibility
-------------

Added: mIRC v3.8 (25 Nov 1995)

See Also
--------

.. hlist::
    :columns: 4

    * :doc:`/gtalk </commands/gtalk>`
    * :doc:`/splay </commands/splay>`
    * :doc:`$speak </identifiers/$speak>`
