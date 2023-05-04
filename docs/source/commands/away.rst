/away
=====

The **/away** command marks you as away with the server. Using the away with no parameters will unset your away status. Even though /away uses IRC to mark you as away;  this command also stores the away message and the time left internally.

Synopsis
--------

.. code:: text

    /away [message]

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
    * - [message]
      - The away message to be set.

Example
-------

.. code:: text

    ;Set an away message
    /away Work, will be back at 10PM
    ;Unset your away status
    /away

The above example will output:

.. code:: text

    -
    You have been marked as being away
    -
    You are no longer marked as being away
    -

The /away command is usually combined with the $away, $awaymsg, and $awaytime idnetifers:

.. code:: text

    ; /setAway Work, will be back at 10PM
    alias setAway {
    if (!$away) {
    ; mark as away
    away $$1-
    amsg I am currently away
    }
    else echo -c info * /setAway: You are currently away
    }
    ; /remAway
    alias remAway {
    if ($away) {
    amsg I am back (from: $awaymsg $+ ) I was gone for $duration($awaytime)
    ;unset the away status
    away
    }
    else echo -c info * /remAway: You are not away
    }

Compatibility
-------------

Added: mIRC v2.1a (28 Feb 1995)

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$away </identifiers/$away>`
    * :doc:`$awaymsg </identifiers/$awaymsg>`
    * :doc:`$awaytime </identifiers/$awaytime>`
