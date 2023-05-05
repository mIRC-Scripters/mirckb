/play
=====

The **/play** command is a powerful tool that allows you to play text files to users or channels on IRC line by line. /play uses the flood settings in the options.

The play central dialog lists all of the currently queued play requests, and allows you to maintain the queue. Files are played in the order in which they are queued.
The play central dialog can be displayed with the /playctrl command.

When the lines are interpreted as command (with -s or -c) you can use $pnick in those lines to refer to the window that is being used.

Synopsis
--------

.. code:: text

    /play [-xaescpbrnqNmNfNlNtTOPIC] [alias] [channel/nick/stop] [filename] [delay]

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -x
      - Treat the first line in the file as a regular text instead of line count if it is a number.
    * - -a
      - Uses the [alias] parameter as the alias to be called instead of /msg or /notice.
    * - -e
      - Echoes the line to channel/nick window as it would send them to the server (if the window does not exist, a line of the form /msg <window> <line> is displayed in the status window).
    * - -s
      - Can be used offline, will interpret lines as actual command instead of plaintext and execute them in the status window.
    * - -c
      - Forces mIRC to interpret lines as actual command instead of plaitext and execute them in the specified window.
    * - -n
      - Uses /notice instead of /msg.
    * - -p
      - Indicates it is a priority request, the current play request is paused and will resume once this one is finished.
    * - -b
      - Uses the clipboard instead of a file, the clipboard is temportarily saved to a file with a name of the form playqN.txt, which is deleted once playing is completed.
    * - -r
      - Forces a single line to be chosen randomly and played.
    * - -fN
      - Plays the whole file starting from the specified line.
    * - -tTOPIC
      - Forces mIRC to look up the specified topic/section (INI structure) in the file and play all lines under that topic/section.
    * - -lN
      - Forces the specified line number to be played.

This two switches only apply for a /play request initiated via a remote definition, not by you:

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -mN
      - limits the number of requests that can be queued by a specific user/channel. If the user/channel already has or exceeds the specified number of requests queued then the play request is ignored.
    * - -qN
      - Specifies the maximum number of requests that can be queued. If the queue length is already larger than or equal to the specified number then the play request is ignored.

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - [alias]
      - If you have specified -a, the alias that will be called instead of /msg or /notice.
    * - [channel/nick/stop]
      - The window you want to play to, if required, or "stop" if you want to stop and clear the queue.
    * - [filename]
      - The filename you want to play.
    * - [delay]
      - You can specify a delay, in millisecond, between each line sent.

Example
-------

.. code:: text

Compatibility
-------------

Added: mIRC v3.1 (23 Apr 1995)

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$play </identifiers/play>`
    * :doc:`on playend </events/on_playend>`
