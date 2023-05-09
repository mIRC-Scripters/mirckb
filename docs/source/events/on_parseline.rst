On Parseline
============

The on parseline event triggers before incoming/outgoing IRC server lines are received/sent and allows a script to modify them.

The incoming / outgoing lines are in IRC protocol which is very different to the terminology used in the mIRC front end. For example all messages to channels and individual users are sent / received using PRIVMSG. :doc:`$ctcp </commands/ctcp>` also uses PRIVMSG with a special encoding to indicate it is CTCP. :doc:`$me </commands/me>` action messages are a specific type of CTCP message etc. ''Use of PARSELINE should therefore be considered advanced scripting and is not for the faint-of-heart.''

Because PARSELINE will be called for every matching line, care should be taken to provide the best possible matchtext in order to minimise the number of times it is called, and to keep the processing undertaken to a reasonable level.

Synopsis
--------

.. code:: text

    on <level>:parseline:in|out|*:<matchtext>:<commands>

* <level> - The appropriate :doc:`access levels </intermediate/events>` for the event.
* <matchtext> - See the :doc:`on text </events/on_text>` event page for a definition of the <matchtext> parameter and related prefixes.

Notes
-----

Note 1: For ''out'' lines, the text you are matching against has a $LF as the last character that you need to account for in your match text. e.g.

.. code:: text

    on *:parseline:out:PRIVMSG *Hello:echo -a $parseline

will not be triggered when you type "Hello" in a channel or query window. Instead you will need something like:

.. code:: text

    on *:parseline:out:PRIVMSG *Hello?:echo -a $parseline
    on *:parseline:out:PRIVMSG *Hello*:echo -a $parseline

Note 2: The ":" character is used quite frequently as a separator in IRC raw messages, but it is also used as a separator in mSL's ON statements. You can either use a placeholder for a single character (?) or multiple characters (*) or you can use a calculated match text or a regular expression for the ":" e.g.

.. code:: text

    on *:parseline:out:PRIVMSG *Hello?:echo -a $parseline
    on *:parseline:out:PRIVMSG & ?Hello?:echo -a $parseline
    on *:parseline:out:$(PRIVMSG & :Hello?):echo -a $parseline
    on $*:parseline:out:/^PRIVMSG [^ ]+ :Hello./:echo -a $parseline

Inside this event, you can use :doc:`$parseline </commands/parseline>` without the -q switch to change the line.

Local identifiers
-----------------

The on parseline event exposes 3 local identifiers:


.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Identifier
      - Description
    * - :doc:`$parsetype </identifiers/parsetype>`
      - Return the type of line, "in" or "out"
    * - :doc:`$parseline </identifiers/parseline>`
      - Return the line being sent/received.
    * - :doc:`$parseutf </identifiers/parseutf>`
      - Return $true if mIRC is going to decode/encode utf8 the message after the on parseline event

.. note:: For 'out' lines, $parseline is terminated with a $LF character that is not visible when viewed in mIRC. You may wish to remove this with:

.. code:: text

    var %pl $parseline
    if ($asc($right(%pl,1)) == 10) %pl = $right(%pl,-1)

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$parseline </commands/parseline>`
    * :doc:`$parseline </identifiers/parseline>`
    * :doc:`$parseutf </identifiers/parseutf>`
