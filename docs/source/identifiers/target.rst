$target
=======

$target returns the target of an event. For instance, when a window closes, the :doc:`on close </events/on_close>` event triggers and $target is filled with the window name of that window.

Synopsis
--------

.. code:: text

    $target

Parameters
----------

None

Properties
----------

None

Examples
--------

.. code:: text

    ; When any window is closed, echo the window name
    ; to a custom @windowWatcher window. If that window doesn't exist,
    ; create it first.
    
    ON *:CLOSE:*: {
      $iif(!$window(@windowWatcher),window @windowWatcher)
      echo @windowWatcher Window Closed: $target $+ .
    }

.. code:: text

    ; When a message is received in a query,
    ; open a new @window with the user's nickname and log the
    ; chat from there on out. If the window closes, stop logging.
    
    ON *:OPEN:?:*: {
    
      ; Add the user to level 3 for logging
      .auser 3 $address($nick,2)
    
      ; Set the window name to the dynamic $target identifier
      %w = @ $+ $target
    
      ; If the custom logging window is not open, create and 
      ; minimize it.
      if (!$window(%w)) { window -n %w }
    
      ; If the user has sent data, log it to the custom window
      if ($1) { echo %w $1- }
    }
    ON 3:TEXT:*:?: {
    
      ; Set the window name to the dynamic $target identifier
      var %w = @ $+ $target
    
      ; If the custom logging window is not open, create and 
      ; minimize it.
      if (!$window(%w)) { window -n %w }
    
      ; Echo the contents of the message to the window.
      echo %w $1-
    }
    ON 3:CLOSE:?: {
    
      ; When the query window is closed locally or remotely,
      ; remove the user from the user level 3 for logging,
      .ruser 3 $address($target,2)
    
      ; Input a request if the log window should be kept open
      ; or closed.
      window $iif($input(Do you want to keep the log window open?,yi,Keep Log Window?),-a,-c) @ $+ $target
    }

Compatibility
-------------

.. compatibility:: 5.3

See also
--------

.. hlist::
    :columns: 4

    * :doc:`on open </events/on_open>`
    * :doc:`on close </events/on_close>`

