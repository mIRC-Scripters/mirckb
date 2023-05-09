On Text
=======

The on text event is a mIRC event that triggers when a remote user (I.E. not the local user) receives a channel or a query message.

Synopsis
--------

.. code:: text

    on <level>:text:<matchtext>:<target>:<commands>

Level
-----

* <level> - The appropriate :doc:`access level </intermediate/events>` for the event.

Matchtext
---------

A <matchtext> is a text pattern that mIRC will use to compare with something. Inside the on text event, the matchtext parameter is every user message. In general, there is only one matchtext parameter per event, you can also find matchtext parameter in others area of the mIRC scripting language, like in the :doc:`$filter </commands/filter>` command for example. An event only triggers if its matchtext parameter matches the appropriate data (user message, notice and server message etc..)

Wildcard text pattern
^^^^^^^^^^^^^^^^^^^^^

The matchtext can contain wild characters: 
* \* - matches any text
* ? - matches any single letter
* & - matches any single word

For Example: 
* !test - the matchtext will only match if the ONLY word is "!test"
* !test\* - the matchtext will match if the text starts with "!test"
* \*!test - the matchtext will match if the text ends with the word "!test"
* \*!test* - the matchtext will match any text that has "!test" in it (anywhere)
* !test & - the matchtext will match any text that start with the word test !test and is only followed by a second word

The basic text pattern
^^^^^^^^^^^^^^^^^^^^^^

The most basic on text event is the normal :ref:`matching_tools-wildcard` pattern:

.. code:: text

    on *:text:!help:#:{
      notice $nick For Help just state your question and pastebin any relevant code.
    }

Sometimes we want to get the user's input. We can use the & to match a single word (in this case it will be a name, although it doesn't matter)

.. code:: text

    on *:text:!color &:?:{
      var %color = $gettok(white black red blue brown yellow orange green, $rand(1, 8), 32)
      msg $chan $2's random color is: %color $+ .
    }

RegEx text pattern
^^^^^^^^^^^^^^^^^^

The matchtext parameter can also be a Regular Expression Pattern by using the $ event prefix (:ref:`dollar-prefix`). 

Example:

.. code:: text

    on $*:text:/^!test$/i:#:{
      msg $chan Test Worked!
    }

Dynamic text pattern
^^^^^^^^^^^^^^^^^^^^

Text matched patterns can also be dynamic, for example your name at the time of the execution ($me), a variable or time. In order for mIRC to know to evaluate the expression, it must be enclosed by the $() identifier. 

Example:

.. code:: text

    on *:text:$(*slaps $me $+ *):#:{
      describe $chan Slaps $nick with dried-up sandwich!
    }

Or 

.. code:: text

    on *:text:$(!example * $+ %match $+ *):#:{
      describe $chan This is an example, $+ $nick $+ !
    }

If the entire match text pattern contains a SINGLE variable, the $() is not required, this technique can also be used for any other parameter of an event. 

Example:

.. code:: text

    ;Assume %text is set to !cool
    on *:text:%text:#:{
      msg $chan I am the coolest! 
    }

It is also possible to use regular expressions with dynamic match text.

.. code:: text

    on $*:text:$(/^!slaps $me $+ /Si):#:{
      describe $chan Slaps $nick with dried-up sandwich!
    }

Target
------

The target parameter of the event defines the locations of where the event can be triggered from. For example, the on text event can be triggered by a channel message or by a query.

* ? - defines query location
* # - defines channel location
* * - defines both query and channel locations
* %var - A variable containing a channel or a list of channels is also acceptable 

Example:

.. code:: text

    ;let %chan equal #mSL,#help,#support
    on *:text:!hi:%chan:{
      notice $nick Hello!
    }

Example 2:

.. code:: text

    ; use local identifier $channels to work
    alias -l channels { return #mSL,#help,#support }
    on *:text:!hi:$($channels):{
      notice $nick Hello!
    }

Local $identifier available in the on text event
------------------------------------------------

The on text event support the common IRC related local identifiers

See also
--------
