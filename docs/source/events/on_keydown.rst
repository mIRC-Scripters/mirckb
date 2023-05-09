On Keydown
==========

The ON KEYDOWN event is triggered when a key is pressed down inside of a custom custom windows - mIRC|@window.

.. note:: Before version 7.62, on keydown was broken, it was incorrectly trying to do two things at once, reporting keypress and the resulting character of keypresses.

The idea was to report the key being pressed in $keyval, and the resulting character in $keychar. From the very beginning, $keyval was incorrect because it returned the ASCII value of the character being pressed instead of the corresponding keycode which comes with the internal WM_KEYDOWN windows message, which has a different value for letters than ASCII. And then, if you needed to press two keys to get a character, something related to 'dead key' as well, you couldn't get the resulting character properly. For example if you press control + o, you need to get the control key being pressed, the 'o' key being pressed, and the resulting character, which is a $chr(15). It was not even possible to change on keydown to report things correctly because keypresses and resulting character comes from two differents message, and the resulting character is only known in the second one, which is always sent second. So on keydown was changed to only report keypress, which is way more correct. The event now to get the resulting character no matter what, like if you're trying to script a visual editbox in a picture window, you need to use the new created event, :doc:`on char </events/on_char>`

Synopsis
--------

.. code:: text

    ON <level>:KEYDOWN:<@>:<keycode,...,keycodeN>:<commands>

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <level>
      - The level for the event to trigger.
    * - <@>
      - The custom windows - mIRC|custom window where this event should listen. Can be @ for all windows.
    * - <keycode>
      - The specific key, or keys to listen for. Can specify multiple keys, such as:

.. code:: text

    ON *:KEYDOWN:@myWindow:38,42,55,78:echo -a $keyval

See https://docs.microsoft.com/en-us/windows/win32/inputdev/virtual-key-codes for a list of key code

Identifiers
-----------

This event fills the following identifiers:

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Identifier
      - Description
    * - :doc:`$keyval </identifiers/keyval>`
      - The Windows keycode value of the key pressed, this has nothing to do with ascii or unicode code point, the list can be found here https://docs.microsoft.com/en-us/windows/win32/inputdev/virtual-key-codes
    * - :doc:`$keychar </identifiers/keychar>`
      - The actual character pressed if there is one, see the note above, this is kept for backward compatibility reason, scripters should not use this value inside on keydown
    * - :doc:`$keyrpt </identifiers/keyrpt>`
      - If the key is being held down/repeating

Example
-------

Create an alias that launches a custom, :ref:`picture_windows` which listens for key presses and displays the key value pressed, the key character pressed, and if it is repeating:

.. code:: text

    alias keyDownTest {
      window -p $+ $iif($window(@myWindow),ra) @myWindow 550 300 250 105
    }
    ON *:KEYDOWN:@myWindow:*: {
      clear @myWindow
      drawtext @myWindow 1 3 3 Key value: $iif($keyval,$v1,NA)
      drawtext @myWindow 1 3 25 Key character: $iif($keychar,$v1,NA)
      drawtext @myWindow 1 3 47 @myWindow Repeating: $keyrpt
    }

The following command can now be typed into any mIRC command prompt:

.. code:: text

    /keyDownTest

Below is an image reflecting what this example will look like:

File:Keyup event.png|This screenshot shows an example of the ON KEYDOWN event custom example.

Note that this makes use of a :ref:`picture_windows`, as well as the /drawtext command - mIRC|drawtext command. These types of :ref:`picture_windows` and their tools can be very powerful in creating some amazing graphical layouts, as well as mIRC games.

Compatibility
-------------

.. compatibility:: 5.8

See also
--------

.. hlist::
    :columns: 4

    * :doc:`/drawtext </commands/drawtext>`
    * :doc:`on keyup </events/on_keyup>`
    * :doc:`$keyval </identifiers/keyval>`
    * :doc:`$keychar </identifiers/keychar>`
    * :doc:`$keyrpt </identifiers/keyrpt>`

