/clipboard
==========

The /clipboard command copies text to the clipboard.

Synopsis
--------

.. code:: text

    /clipboard [-an] [text]

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -a
      - Appends text to the end of the current clipboard's contents
    * - -n
      - Appends a $crlf to the end of the text

.. note:: Presence or absence of a single trailing $crlf does not affect the lines count of $cb(0)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - [text]
      - Text to be placed in clipboard. If no text parameter used, the clipboard is cleared.

Example
-------

Clear the clipboard and put "Hello world!" in it

.. code:: text

    /clipboard Hello World!
    
Put 'abcd' into clipboard then append efgh and carriage return:

.. code:: text

    //clipboard abcd | clipboard -an efgh | echo -a $cb(0).len / $cb(1).len / $cb(1)
    ;returns: 10 / 8 / abcdefgh
    ;(The difference between length of $cb(0) and $cb(1) is the $crlf.
    
Clear clipboard contents:

.. code:: text

    /clipboard
    
Append $crlf to end of current clipboard contents:

.. code:: text

    /clipboard -an

Compatibility
-------------

.. compatibility:: 5.1

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$cb </identifiers/cb>`
    * :doc:`$inpaste </identifiers/inpaste>`

