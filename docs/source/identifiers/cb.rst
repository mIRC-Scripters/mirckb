$cb
===

The $cb identifier allows mIRC to return the contents of the Windows Clipboard.

Synopsis
--------

.. code:: text

    $cb
    $cb(N,[u],[%var|&binvar])

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - N
      - The Nth :doc:`$crlf </identifiers/crlf>` delimited line in the clipboard, you can use -1 to get the full clipboard with newline included.
    * - u
      - Return the text encoded to utf8
    * - %var|&binvar
      - You can pass a variable or a binary variable to be filled instead of being returned by $cb, using a binvar allow you to handle more than the current line lenght limit of 8292 char.

Properties
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Property
      - Description
    * - .len
      - returns the length of the Nth line
    * - .utflen
      - returns the len of the text encoded to utf8, same as .len with the 'u' parameter
    * - .utf
      - This property appears in the source code but does not work, it looks like the source code is not checking the proper variable handling the prop name. It would naturally return the text encoded to utf8

Example
-------

Echo clipboard contents to the active window:

.. code:: text

    //echo -a $cb

Echo the total number of clipboard entires to the active window:

.. code:: text

    //echo -a $cb(0)

Create a custom alias that will open a custom window ''@myWindow'', and then echo all clipboard line contents to it:

.. code:: text

    ; Use: /cblist
    alias cblist {
    
      ; Open the window, and clear it just in case it was already opened
      window @myWindow
      clear @myWindow
    
      ; Set the %i, our counting variable, to the start value of 1, and
      ; set the %x variable to the amount of lines in the clipboard
      var %i = 1, %x = $cb(0)
    
      ; Loop until %x has gone through all clipboard contents
      while (%i <= %x) {
        echo @myWindow $cb(%i)
        inc %i
      }
      echo @myWindow Clipboard contents finished!
    }

Compatibility
-------------

.. compatibility:: 6.2

See also
--------

