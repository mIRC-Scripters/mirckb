$caller
=======

$caller returns a value which indicates the context in which your alias has been called.

The possible returned value can be:
* "activex" - called from $comcall
* "command" - called from a command
* "dde" - called from a external application using :doc:`$dde </identifiers/dde>` 
* "dll" - called from a :doc:`DLL </advanced/dll>`
* "dragdrop" - called from a drag'n'drop event
* "editbox" - called from an editbox
* "event" - called from an event (including $devent = mouse)
* "funckey" - called from a function key
* "identifier" - called from an identifier
* "menu" - called from a menu
* "mouse" - called from an alias attached to toolbar menu
* "play" - called from a :doc:`/play </commands/play>` context
* "sendmsg" - called from a :doc:`sendmessage </advanced/sendmessage>` function
* "timer" - called from a timer
* "http" - call back alias from $urlget
* "tabcomp" - called from a tab completion in editbox
* "other" - called from other contexts including:
# label of popups menu
# /filter -a sort_alias
# identifier in dialog table (ie returning one of the x y w h numbers)

Synopsis
--------

.. code:: text

    $caller

Parameters
----------

None

Properties
----------

None

Example
-------

Activex: edit the echo in the alias cbthread in :doc:`$comcall </identifiers/comcall>` page to include $caller

Command & Identifier: execute /A or //noop $A

.. code:: text

    alias A B
    alias B echo -ag $caller

Editbox:
execute: /A
or
execute: //echo -a $caller

.. code:: text

    alias A echo -ag $caller

Event: execute /dns test

.. code:: text

    on *:dns:echo -a $caller

Funckey: hit shift + f11 on your keyboad:

.. code:: text

    alias s11 echo -a caller

Menu: right click in a channel

.. code:: text

    menu channel {
    $caller displays in menu label text as other:echo -a $caller displays here as menu
    }

play: execute in a connected status window //play -as A $mircini | .timer 1 2 play off

.. code:: text

    alias A echo -sg $caller

Timer: type in editbox:

.. code:: text

    /timer 1 1 echo -a $caller
    or
    //timer 1 1 echo -a $ $+ caller

Compatibility
-------------

Compatibility
-------------

.. compatibility:: 7.52

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$fromeditbox </identifiers/fromeditbox>`
    * :doc:`$comcall </identifiers/comcall>`
    * :doc:`/toolbar </commands/toolbar>`
    * :doc:`/filter </commands/filter>`
    * :doc:`$dll </identifiers/dll>`
    * :doc:`$dde </identifiers/dde>`
    * :doc:`/play </commands/play>`
    * :doc:`/timer </commands/timer>`
    * :doc:`$devent </identifiers/devent>`
