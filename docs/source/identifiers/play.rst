$play
=====

$play returns informations about queued /play request

Synopsis
--------

.. code:: text

    $play(N)
    or
    $play(nick,N)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - nick
      - if you specify a nick, it returns how many play requests an user has in the queue.
    * - N
      - The Nth /play request queued

Properties
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Property
      - Description
    * - .type
      - returns the type of the request, "topic" if you are using :doc:`/play -t </commands/play>`, "file" otherwise
    * - .fname
      - returns the complete filename used for the play request
    * - .topic
      - returns the name of the topic if you used :doc:`/play -t </commands/play>`
    * - .pos
      - returns the number of the line that play request is at, (the next line to be played)
    * - .lines
      - returns the total number of lines in the file being played
    * - .delay
      - returns the delay used for the play request (default to 1000)
    * - .status
      - returns the status of the play request, "playing" or "queued"

Example
-------

.. code:: text

    //echo -a $play(0)

Compatibility
-------------

.. compatibility:: 5.82

See also
--------

.. hlist::
    :columns: 4

    * :doc:`/play </commands/play>`

