$?
==

.. attention:: This feature has essentially been replaced by :doc:`$input </identifiers/input>`

The $? identifier is used to request immediate user-input.

Synopsis
--------

.. code:: text

    $?="[Input Request Message]"

Displays an input box to get user-input. The "Input Request Message" is optional; if not specified, it default to "Enter reply:"

Usage
-----

There are four ways you can use this identifier:

# $?="Give Me Input"
    Displays an input request with the words 'Give Me Input' above the input box.
# $?*="Give Me Password"
    Displays a password input request: the input is treated as a password field. The input is shown as •••
# $?!="Give Me Input"
    Displays an input request with a Yes & No button, with the words 'Give Me Input' above them.
    If you click Yes, the input returns $true, otherwise it returns $false, even if you don't click No and exit out other ways.
# $?N="Give me input!
    Where N is a positive number > 1 representing the $N identifier, If the value of $N is $null, you are asked to provide it, otherwise $N is returned.
# $?#="Give me input!
    where # represents $chan, If the value of $chan is $null, you are asked to provide it, otherwise $chan is returned

You can use :doc:`$crlf </identifiers/crlf>` to get multiple lines.

.. note:: This fills the :doc:`$! </identifiers/dollarexclamation_mark>` identifier with the value entered in the editbox if you press ok or yes buttons

Notes & Quirks
--------------

The $? identifier has some parsing issues, it has been replaced by :doc:`$input </identifiers/input>` to overcome these issues:

* $? can be used without the '=' sign as long as you either don't pass as an input request message (just $?), or that this paramater contain a balanced number of quotes:
    * $? $?"test" $?"test words" etc are all valid usages.
    * In fact, mIRC start looking for a valid parameter when you start the first quote, $?ignored"this is the message" will actually ignore the part before the first quote
* //echo -a $?"message with multiple words" $?!"test"
    This line cause parsing issue, here $?!"test" is evaluated before, mIRC seems to get lost as to which quote is closing which quote, and end up evaluating more than it should

Examples
--------

Below are three examples that display exactly how to use each individual property:

Basic
^^^^^

Echoes whatever the user types into the input field to the active window:

.. code:: text

    alias testme {
      echo -a $?="Type something for me"
    }

Does the same as the first example, except while the user is typing, the characters are replaced by password characters. The typed value, however, is visibly legible when it is echoed to the active window.

.. code:: text

    alias testme {
      echo -a $?*="Enter Password:"
    }

Pops up an input request asking if the user likes chocolate. If they click Yes, it echoes $true to the active window; otherwise, it echoes $false.

.. code:: text

    alias testme {
      echo -a $?!="Do you like chocolate?"
    }

We tokenize the A B using token 32, which is the character for spaces. The script then asks the user for a 3rd token value, via $?3. Once the user enters that value, it is then echoed to the active window. If we use $?2 instead, B will be used without asking anything.

.. code:: text

    alias testme {
      tokenize 32 A B
      echo -a $?3
    }