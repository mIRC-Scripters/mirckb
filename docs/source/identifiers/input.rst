$input
======

$input is used to request immediate user-input.

.. note:: This replaces the deprecated $? identifier.

Synopsis
--------

.. code:: text

    $input(prompt,options,window,title,text)

Prompts the user for input and returns the result.

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - prompt
      - Parameter must not be blank. Text displayed inside the input dialog window. The input dialog is extended vertically as needed to display the prompt message if it is very long. You can also make text in the prompt message appear on different lines by using :doc:`$crlf </identifiers/crlf>` to separate lines. The input window widens as needed by 1-3 buttons, the edit or combo dropdown, icon, or titlebar text
    * - options
      - Options can be a combination of the following:
    * - e
      - show input editbox. Content of input editbox returned by clicking leftmost button. Defaults to returning empty string if <esc> out of dialog or pressing 'No' 'Cancel'. Can get $no/$cancel/$timeout by using the forcing 'f switch ('v' switch also required to get $timeout)
    * - p
      - show input password editbox. Same return strings as 'e'
    * - o
      - 'ok' button
    * - n
      - 'yes' 'no' 'cancel' buttons
    * - y
      - 'yes' 'no' buttons
    * - r
      - 'retry' 'cancel' buttons
    * - m
      - indicates that multiple text parameters have been specified. They will be displayed in a combo dropdown box. The first text item is the default item (a reference to an item in the list), the rest are the items in the list. Selected list item is returned from clicking the leftmost button. Dropdown list begins with the 2nd 'text' parameter, and item from list is displayed as default selection only if it has case-insensitive match with the 1st 'text' parameter.
    * - v
      - Only works when you're not using any of 'pem' switches. makes $input returns $ok, $yes, $no, $cancel, $retry if you press such buttons. Also makes $input returns $timeout if the kN timeout switch is used
    * - f
      - This switch is the same as the 'v' switches except it works for when you're using any of the 'pem' switches. Exception: if you're using the kN switch with any of the 'pem' switch, then 'f' must be used in conjunction with 'v' to get $timeout
    * - kN
      - an N seconds timeout value. On timing out, has default action of returning $false for 'onyr' switches (or no 'pem' switches used, default) or $null for 'pem' switches. Returns $timeout if 'v' switches is used without 'pem', requires both 'f' and 'v' switches if you're using 'pem' and you want $timeout.
    * - g
      - right-align buttons
    * - b
      - disables buttons for 1 second when dialog is displayed and clears keyboard buffer
    * - tciqwh
      - show the goldstar,recycle bin,info, question, warning, and halt icons respectively.
    * - d
      - play system sound associated with icon switch used: 'di' 'dt' = 'asterisk', 'dq' = 'question', 'dw' 'dc' = 'exclamation', 'dh' = 'critical stop'
    * - s
      - indicates that window parameter has been specified (making optional 'title' be the 4th parameter)
    * - a
      - make $input dialog active if mIRC is not the active application
    * - u
      - use current active window as parent window, including custom dialog window. In the past, the 's' switch could not be used to pass a custom dialog window as the parent, this switch is then technically there for custom dialog support as parent.
    * - window
      - if option s is specified, the name of the window to be used as parent window, can be any string that $window(string) will return correctly, so no custom dialog.
    * - title
      - the titlebar text.
    * - text
      - default text placed in the input editbox

The options, window, title, and text are optional parameters

By default, 'onyr' switches  return $true from 'Ok' 'Yes' 'Retry' buttons and returns $false from 'No' 'Cancel' buttons. 'pem' switches defaults buttons returning the contents of editbox/combobox except 'No' 'Cancel' buttons returning $null. f switch extends 'No' 'Cancel' buttons in 'pem' to have same behavior as in 'onyr' with 'v' switch. kN defaults to returning $false if dialog not exited within N seconds. 'v' changes $true $false from button clicks to instead return '$yes' '$no' '$ok' '$retry' '$cancel', except for $false strings caused by kN change to $timeout.

For the options parameter, you can also use a number as a combination of value added together, without the presence of any letter switches, which is how $input was originally working:
* 1  - show input editbox (equivalent of the 'e' switch)
* 2  - show input password editbox (equivalent of 'p' switch)
* 4  - ok button (equivalent of 'o')
* 8  - yes/no buttons ('y')
* 16 - yes/no/cancel buttons ('n')
* 32 - return $ok, $yes, $no, $cancel, $retry for buttons. ('v')
* 64 - show the info icon ('i')
* 128 - show the question icon ('q')
* 256 - show the warning icon ('w')
* 512 - show the halt icon ('h')
* 1024 - insert 'window' as the 3rd parameter ('s')
* 2048 - activate the $input dialog when mIRC is not the active application ('a')
* 4096 - show the gold star icon ('t')
* 8192 - retry/cancel buttons ('r')
* 16384 - align buttons to the right ('g')
* 32768 - show the recycle bin icon ('c')
* 65536 - play icon-related sound ('d')
* 131072 - combo dropdown list ('m')

$input(sup,5) is equivalent to $input(sup,eo)

.. note:: This identifier cannot be used in a remote event. One way around this is to use a :doc:`/timer </commands/timer>` to initiate an input request after the script ends. Another way around it is to use :doc:`/signal </commands/signal>` to trigger an :doc:`on signal </events/on_signal>` event.

Examples
--------

.. code:: text

    alias testme {
      echo -a $input(Type something for me,e)
    }

Echoes whatever the user types into the input field to the active window.

.. code:: text

    alias testme {
      echo -a $input(Enter Password:,p)
    }

Does the same as the first example, except while the user is typing, the characters are replaced by password characters. The typed value, however, is visibly legible when it is echoed to the active window.

.. code:: text

    alias testme {
      echo -a $input(Do you like chocolate?,y)
    }

Pops up an input request asking if the user likes chocolate. If they click Yes, it echoes :doc:`$true </identifiers/true>` to the active window; otherwise, it echoes :doc:`$false </identifiers/false>`.

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$? </identifiers/dollarquestion_mark>`
