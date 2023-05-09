On Close
========

The ON CLOSE event triggers within mIRC when a specific window type is closed.

Synopsis
--------

.. code:: text

    ON <level>:CLOSE:<?|#|@|=|!|*>:<commands>

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <*><#><?><@><=><!>
      - The place, or places where the event listens, you can specify specific name of window, seperate them by comma.
        * \* - Any channel/query/dcc/custom windows
        * # - Any #channel windows
        * ? - Any query windows
        * = - Any dcc chat windows
        * ! - Any dcc server windows
    * - <commands>
      - The commands to be performed when the event triggers

Local identifiers
-----------------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Identifier
      - Description
    * - :doc:`$target </identifiers/target>`
      - Is filled with the name of the window related to the event.

Examples
--------

.. code:: text

    ; When Channel window are closed, print a message to
    ; the "Status Window".
    
    ON *:CLOSE:#: { echo -sg Closed $target window. }

.. code:: text

    ; When DCC Chats are closed, send a notice to
    ; the person.
    
    ON *:CLOSE:=:notice $nick Hey, thank you so much for the chat!

.. code:: text

    ; When any window is closed, echo the window name
    ; to a custom @windowWatcher window. If that window doesn't exist,
    ; create it first.
    
    ON *:CLOSE:*: {
      $iif(!$window(@windowWatcher),window @windowWatcher)
      echo @windowWatcher Window Closed: $target $+ .
    }

Compatibility
-------------

.. compatibility:: 5.3

See also
--------

.. hlist::
    :columns: 4

On open - mIRC|ON OPEN

