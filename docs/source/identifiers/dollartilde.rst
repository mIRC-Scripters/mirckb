$~
==

$~ is a construct which allows you to call built-in identifiers only, custom aliases are not checked. This conveniently avoids the identifier warning message and halting behavior. Returns the result of the built-in identifier call, or $null (see the notes)

Synopsis
--------

.. code:: text

    $~identifiername()

Parameters
----------

None

Notes & Examples
----------------

It's unclear still why this undocumented construct exists. Khaled stated that this should not be used in scripts, that it changes the way the paramater are parsed. But a look at a decompiled mirc.exe says otherwise, the only thing it does is prevent custom aliases from being checked.

As a result, the identifier warning message is not triggered and the script not halted if you call an identifier that is not a built-in identifier of mIRC.

This can effectively be used to check for existence of a built-in identifier, be it if you want to do something once a future version has the identifier, or if you want to support older mirc version not having a built-in identifier. This has recently proven to be useful to write mIRC/Adiirc compatible script.

.. code:: text

    
    //echo -a $~rands(1,6) vs $rands(1,6)
    
    if ($~rands(1,1) == 1) { echo -sg this version support $!rands }
    

However, recently it was figured out that $~ have a purpose that makes more sense, and that's local identifiers, one that only have a value in specific mIRC events.
Because such identifier have a global scope, they have a value inside an alias if that alias is called from the event's scope.
So consider for example a script that's going to be shared on different mIRC configuration/install/machine:

.. code:: text

    on *:text:*:#:process_message $1-
    on *:input:#:processs_message $1-
    alias process_message {
    var %nick $iif($nick,$nick,$me)
    ....
    }

which is typical, if you load this script into a mIRC which has a custom alias named "me" returning "test" for example, this script would fail, %nick would incorrectly take the value "test" for your on input. This is where $~ is useful, using $~nick would actually ensure that if $nick has a value, then this value can only come from the event specific identifier and never a custom aliases, indeed preventing conflicts.

Another thing to consider is the spacing, if the $~identifier call is not a built-in and you have some spacing, consider:

.. code:: text

    echo -ag $~nonbuilt-in( $me )
    ;displays "yournickname )"

in this case only the part up to the space is evaluated as $null, the rest of the line is not touched and will evaluate normally.

This means that to correctly check if an identifier is supported, you must not use space:

.. code:: text

    if ($~rands(1,1) == 1) { echo -sg this version support $!rands } // correct
    if ($~rands(1, 1) == 1) { echo -sg this version support $!rands } // incorrect
    
as it will now act as 'if ( 1) == 1)' on a version not supporting $rands, instead of 'if ($null == 1)'

Compatibility
-------------

Version added: 6.0

See also
--------
