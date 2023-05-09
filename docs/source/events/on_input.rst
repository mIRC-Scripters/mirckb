On Input
========

The ON INPUT event triggers when text is entered into an mIRC editbox, then followed by an enter-key press.

Synopsis
--------

.. code:: text

    ON <level>:INPUT:<*#?=!@>:<commands>

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <level>
      - The level for the event to trigger.
    * - <\*#?=!@>
      - The window type that this event should monitor.
    * - *
      - Any window
    * - #
      - Any channel, or specific channel name(s)
    * - ?
      - Query windows
    * - =
      - DCC Chat windows
    * - !
      - Fserve windows
    * - @
      - Custom windows
    * - <commands>
      - The commands to be performed when the event listener's criteria is met.

Examples
--------

If ^scripts is entered into an editbox, echo the total amount of loaded scripts to the active window:

.. code:: text

    ON *:INPUT:*: {
      if ($1 == ^scripts) {
        echo -a There are $script(0) script(s) loaded.
        haltdef
      }
    }

The results would look something like this:

.. code:: text

    There are 9 total script(s) loaded.

The example above makes use of the :doc:`$haltdef </commands/haltdef>` command, which prevents mIRC from performing the default operation for this event. If there were no :doc:`$haltdef </commands/haltdef>` there, mIRC would carry out the first command which was to echo the details to the active window, but then it would also either send the message to the active chat, or channel, or provide an error stating you are not currently on a channel.

Compatibility
-------------

.. compatibility:: 5.0

See also
--------

.. hlist::
    :columns: 4

    * :doc:`on keydown </events/on_keydown>`
    * :doc:`on keyup </events/on_keyup>`

