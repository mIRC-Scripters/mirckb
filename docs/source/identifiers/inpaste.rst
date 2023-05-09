$inpaste
========

$inpaste returns $true if a user triggered the :doc:`on input </events/on_input>` event by pressing Control+V or Shift+Insert to paste text into an editbox or using the 'Paste' choice from the editbox's right-click menu.

It appears that $inpaste is mostly $false, and can be $true only when:

# In channel editbox where Options/Display/Other/'Editbox Lines' is set to 'Single'
# In @window editbox created with /window -e0 or -e, or created with -e3 while Editbox Lines is set to single
# Clipboard contains at least one of $cr $lf $crlf
# Paste from the clipboard triggers the ON INPUT event
# $inpaste is used within the ON INPUT or ON PARSELINE:out event

.. note:: If you paste text into the editbox which doesn't trigger the INPUT event, pressing <enter> later messaging the pasted text to #channel does not set $inpaste to $true.

Synopsis
--------

.. code:: text

    $inpaste

Parameters
----------

None

Properties
----------

None

Example
-------

.. code:: text

    on *:INPUT:*:{ if ( ($istok(/ $comchar,$left($strip($1),1),32)) && (!$ctrlenter) && ($inpaste)) { echo -g Preventing this pasted /command from being executed: $1- | halt } }

.. code:: text

    on *:PARSELINE:out:*:{ echo -s debug $scriptline $event : $inpaste is $true only if this line was triggered by pasting from the clipboard : $parseline }

.. code:: text

    if ($inpaste) echo -a INPUT event triggered by paste from clipboard
    elseif ($ctrlenter) echo -a INPUT event triggered by pressing <enter> and <Ctrl> keys together
    else echo -a INPUT event triggered by pressing <enter>

Compatibility
-------------

.. compatibility:: 5.8

See also
--------

.. hlist::
    :columns: 4

    * :doc:`on input </events/on_input>`
    * :doc:`on parseline </events/on_parseline>`
    * :doc:`$ctrlenter </identifiers/ctrlenter>`
    * :doc:`$comchar </identifiers/comchar>`
