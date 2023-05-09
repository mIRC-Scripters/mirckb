$keylparam
==========

$keylparam is filled during an :doc:`on keydown </events/on_keydown>`, :doc:`on keyup </events/on_keyup>`, or :doc:`on char </events/on_char>` event inside of a custom window (:ref:`custom_windows`). This value is the value returned by Windows itself to mIRC when these events occurs, the lParam value is an array of bit containing informations such as extended key, repeat count etc.

Synopsis
--------

.. code:: text

    $keylparam

Parameters
----------

None

Meaning
-------

* 0-15 -    The repeat count for the current message. The value is the number of times the keystroke is autorepeated as a result of the user holding down the key. If the keystroke is held long enough, multiple messages are sent. However, the repeat count is not cumulative.
* 16-23 -	The scan code. The value depends on the OEM.
* 24 -	Indicates whether the key is an extended key, such as the right-hand ALT and CTRL keys that appear on an enhanced 101- or 102-key keyboard. The value is 1 if it is an extended key; otherwise, it is 0.
* 25-28 -    Reserved; do not use.
* 29 -	The context code. The value is 1 if the ALT key is held down while the key is pressed; otherwise, the value is 0.
* 30 -	The previous key state. The value is 1 if the key is down before the message is sent, or it is 0 if the key is up.
* 31 -	The transition state. The value is 1 if the key is being released, or it is 0 if the key is being pressed.

Compatibility
-------------

.. compatibility:: 7.69

See also
--------

.. hlist::
    :columns: 4

    * :doc:`on keyup </events/on_keyup>`
    * :doc:`on keydown </events/on_keydown>`
    * :doc:`on char </events/on_char>`
    * :doc:`$keychar </identifiers/keychar>`
    * :doc:`$keyval </identifiers/keyval>`

