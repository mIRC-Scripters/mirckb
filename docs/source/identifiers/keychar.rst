$keychar
========

$keychar is filled during an :doc:`on keydown </events/on_keydown>`, :doc:`on keyup </events/on_keyup>` or :doc:`on char </events/on_char>` event inside of a custom @window (:ref:`custom_windows`), it returns the characters that was inputted if any.

.. warning:: This identifier is broken by design inside the :doc:`on keydown </events/on_keydown>` and :doc:`on keyup </events/on_keyup>` events.
    These two events have been trying for years to report AND keypresses, AND resulting characters but their implementation was wrong.
    On newer version of mIRC, this was fixed, :doc:`on keydown </events/on_keydown>` and :doc:`on keyup </events/on_keyup>` only trigger for keypresses.

    To get the resulting character, one should use the :doc:`on char </events/on_char>` event. $keychar is still filled inside :doc:`on keydown </events/on_keydown>` and :doc:`on keyup </events/on_keyup>` for backward compatibility purpose. To get an idea, both events will correctly fill $keychar with the character when you press 'A', because it's one keypress corresponding to one character, but the main issue was that some keyboard/language requires you to press two keys to generate a character, sometimes mores.

    To sum up, checking $keychar inside :doc:`on keydown </events/on_keydown>` and :doc:`on keyup </events/on_keyup>` is incorrect and won't work for any language/keyboard, those two events are to be used to look for keypresses only with $keyval, use $keychar inside :doc:`on char </events/on_char>` only, to get characters.

Synopsis
--------

.. code:: text

    $keychar

Parameters
----------

None

Example
-------

Create an alias that launches a custom, :ref:`picture_windows` which listens for key presses and displays the key value pressed, the key character pressed, and if it is repeating:

.. code:: text

    alias keyDownTest {
      window -p $+ $iif($window(@myWindow),ra) @myWindow 550 300 250 105
    }
    ON *:KEYDOWN:@myWindow:*: {
      clear @myWindow
      drawtext @myWindow 1 3 3 Key value: $keyval
      drawtext @myWindow 1 3 47 @myWindow Repeating: $keyrpt
    }
    on *:char:@mywindow:*:{
      drawtext @myWindow 1 3 25 Key character: $keychar
    }

The following command can now be typed into any mIRC command prompt:

.. code:: text

    /keyDownTest

Below is an image reflecting what this example will look like:

File:Keyup event.png|This screenshot shows an example of the ON KEYDOWN event custom example.

Note that this makes use of :ref:`picture_windows`, the :doc:`/drawtext </commands/drawtext>` command. These types of :ref:`picture_windows` and their tools can be very powerful in creating some amazing graphical layouts, as well as mIRC games.

Compatibility
-------------

.. compatibility:: 5.5

See also
--------

.. hlist::
    :columns: 4

    * :doc:`on char </events/on_char>`
    * :doc:`$keyrpt </identifiers/keyrpt>`
    * :doc:`$keyval </identifiers/keyval>`

