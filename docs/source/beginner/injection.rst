mSL Injection
=============

**mSL injection** is a code injection technique that exploits mIRC's ability to dynamically evaluate code on the run. With mSLs powerful commands and identifiers, the result of a code injection attack can be disastrous. It is important that you understand what to look for when working with vulnerable commands.

This tutorial will try to summarize for you what commands are problematic, how to detect it, and how to fix it. 

An eval injection vulnerability consists of two things:

* A script that evaluates a code (via a vulnerable command/ident)
* User input that is not properly validated

Injections happen because of a simple side effect of the main rules definiting the syntaxes/semantics of the language.

Injection via commands
----------------------

For a command, the interesting rule used by the parser to make it working is to evaluate $identifiers and %variables once before passing their value to the command:

.. code:: text

    echo -a $me

Here $me is evaluated, then -a is passed as the first parameter and the value of $me is passed as the second parameter to the /echo command.

Nested command
^^^^^^^^^^^^^^

Now, the language features some commands where one or more of their parameters are actually meant to be a new command with its own parameters. That new command is meant to be used later automatically by mIRC, this is where the injection happens.

Any command like this suffers the problem, we also refer to this problem as the double evaluation problem. They are fortunately not a lot of these commands, here is a list:

* /timer
* /scon
* /scid
* /dde

The /timer command
~~~~~~~~~~~~~~~~~~

Perhaps the most problematic command of them all is the /timer command. The /timer command is used to delay the execution of another command (it has others features but this is the interesting one).

Because of this, you must pass a new command to be executed after the delay to the timer command:

.. code:: text

    //.timer 1 1 echo -a $day

Which will execute ``echo -a <value of $day>`` one time, after waiting 1 second.

What happens here is that the parameters passed to the /timer command are evaluated once as we saw, so $day gets evaluated once, producing the current day.

The timer will register that its associated command to be executed when the delay has passed is ``echo -a <$day's value>``

When the timer fires, its command (a new command) is executed and therefore all of its parameters are, once again, evaluated one time. In this example there is no problem and we can't see the difference because $day can only return a day of the week. If $day is monday, evaluating the plain text monday will always produce monday.

But what if we didn't have $day? what if we had something like $2? Let's consider a more useful example, an innocent reminder script:

.. code:: text

    on *:text:!reminder & *:#:{
     if ($2 !isnum) {
        notice $nick [Reminder] Syntax Error: !reminder <seconds> <message>
        return
      }
      .timer 1 $2 notice $nick [Reminder] $3- (Set $2 seconds ago)
    }

When the correct input is provided, this script works wonderfully. For example:

.. code:: text

    <Mike> !reminder 18000 jill's birthday tomorrow!
    -Bot- [Reminder] jill's birthday tomorrow! (Set 18000 seconds ago)

Indeed, /timer evaluated the parameter once: $2 is evaluated to 18000 and $3- to "jill's birthday tomorrow!"

The associated command of the timer is correctly ``notice Mike [Reminder] jill's birthday tomorrow! (Set 18000 seconds ago)``, when the timer fires, the /notice command will see its parameters evaluated once, but there is nothing to evaluate in this case.

Although this script might seem simple, let's take a look at what happens when someone provides incorrect or even malicious input as in this case:

.. code:: text

    <Mike> !reminder 0 . | ns drop nick | quit hacked!
    -Bot- [Reminder] . (Set 0 seconds ago)
    * Bot (~Bot@isp.example.com) Quit (Quit: hacked!)

This is an msl injection attack. Let's take a deeper look into what has happened:

As we know, /timer evaluated the parameter once; $2 is evaluated to ``0`` and $3- is evaluated to ``. | ns drop nick | quit hacked!``

So now, the associated command of the timer becomes ``.notice Mike [Reminder] . | ns drop nick | quit hacked!`` and you might be recognizing the pipe character, used to separate commands, which mIRC will interpret as such, resulting in /ns drop nick and /quit hacked! being executed.

Clearly, you can see how the timer command can be extremely dangerous. The unfortunate part is that there is no clean way of solving this problem. The only way to prevent this from happening is to encode the problematic parameters so that when they get evaluated, they produce something which needs one more evaluation to produce the correct value. We usually do that by encoding the parameters using based64 encoding. Below is an alias to perform this:

.. code:: text

    alias safe return $!decode( $encode($1-, m) ,m)

The spacing is very important. Our new !reminder script now looks like this:

.. code:: text

    on *:text:!reminder & *:#:{
      if ($2 !isnum) {
        notice $nick [Reminder] Syntax Error: !reminder <seconds> <message>
        return
      }
      .timer 1 $2 notice $nick [Reminder] $safe($3-) (Set $safe($2) seconds ago)
    }

Let's take a look at what happens now:

.. code:: text

    <Mike> !reminder 0 . | ns drop nick | quit hacked!
    -Bot- [Reminder] . | ns drop nick | quit hacked! (Set 0 seconds ago)

And Mike now can't do anything harmful.

/timer will evaluate the parameter as we know but this time, $safe($3-) where $3- is ``. | ns drop nick | quit hacked!`` is evaluated to ``$decode( LiB8IG5zIGRyb3AgbmljayB8IHF1aXQgaGFja2VkIQ== ,m)`` and $safe($2) to ``$decode( MTgwMDA= ,m)``.

The command associated with the timer now becomes ``/notice Mike [Reminder] $decode( LiB8IG5zIGRyb3AgbmljayB8IHF1aXQgaGFja2VkIQ== ,m) (Set $decode( MTgwMDA= ,m) seconds ago)`` and those $decode, when evaluated once by /notice, will produce the correct result (the original input of Mike).

Now you don't need to do that for any /timer command of course, only when the parameter is unknown at the time you are writing the script, such as $2 and $3- here.

.. note:: Since mIRC 7.44, an $unsafe identifier has been added which behaves just like $safe (the name was changed to unsafe to avoid misleading new users), delaying the execution of one level.

**$chan/#**

You may think $chan can't be evaluated in an malicious way but that's not true, if the $chan (also #) identifier is unknown, you should encode it as well.

The reason for this is mIRC allows prefixing an identifier with the pound sign to make mIRC prefixes (if needed) the evaluated string by the pound symbol. For example:

.. code:: text

    //tokenize 32 A #B | echo -a #$1 #$2

This will produce the following result:

.. code:: text

    #A #B

So what does that have to do with $chan and timers? Everything! 

Consider the following bot's code:

.. code:: text

    alias bot_pass return foo_bar_42
    on *:connect:{  
      autojoin -d5  
      ns id $bot_pass
    }
    on *:invite:#:join #
    on !*:join:#:{
      timer 1 2 notice $nick Hello $nick $+ , Welcome to # $+ !
    }

Everything works just fine under normal conditions. But Mike knows better than to test things under normal conditions:

.. code:: text

    * Now talking in #$($bot_pass)
    /invite foobar #$($bot_pass)
    * Bot joined #$($bot_pass)
    /hop #$($bot_pass)
    * Attempting to rejoin channel #$($bot_pass)
    * Rejoined channel #$($bot_pass)
    -Bot- Hello Mike, Welcome to foo_bar_42

Because $chan (or #) was not escaped, it was evaluated. Mike was able to evaluate the $bot_pass alias and get the bot's password.

You might want to watch out for $nick as well, some servers allow nicknames to have the '$' character.

/scon and /scid
~~~~~~~~~~~~~~~

Both of these commands were created to evaluate/execute code on a given connection. Just like the /timer command, any unknown content must be escaped somehow.

Though, unlike /timer, the /scid and /scon are so that when their associated command triggers, they are able to evaluate local variables (but they can't evaluate local identifier like $1-), which makes the escaping easier, you can use the $safe method, but you can simply just use a local variable, consider this less practical example:

.. code:: text

    on *:text:!global *:#:{
      scon -at1 amsg [AMSG] $1-
    }

The script is designed to do a global amsg (i.e. perform an /amsg on every active connection). Just like the timer command, $1- will be evaluated again in the specified connection when the associated command of /scon triggers (/amsg [AMSG] $1-), which means any user code will become part of your bot's code.

* $safe solution:

.. code:: text

    on *:text:!global *:#:{
      scon -at1 amsg [AMSG] $safe($1-)
    }

* Local variable solution:

.. code:: text

    on *:text:!global *:#:{
      var %a $1-
      scon -at1 amsg [AMSG] % $+ a
    }

The associated command becomes ``amsg [AMSG] %a`` and %a is evaluated correctly to produce the user's message.

.. note:: /scid and /scon can be used to change the current connection only, in this case you can just execute the command normally after, does not work for /scon -a for example.

/dde
~~~~

/dde has the same issue and the same solution as /timer, just use $safe on the problematic parameters.

/flash
^^^^^^

Though /flash is the only command doing it for now, more commands might do this in the future. /flash does not take a new command as one of its parameter but it can take a text as an optional parameter, to be used automatically later, that text will be evaluated once by /flash, and mIRC will also evaluate the text parameter once when applying the flash:

.. code:: text

    on *:text:!testflash:#:/flash $ $+ me

So $ $+ me evaluates to "$me" by /flash, and $me will be evaluated to your nickname (that text appears in mIRC's titlebar).

The $safe solution must be used there.

Injection via $identifiers
--------------------------

$readini() and $read()
^^^^^^^^^^^^^^^^^^^^^^

If you have visited #mSL on swiftirc, and you had some code that used $read() or $readini() without the n switch you would most likely had people yelling at you to always use it. But why? The reason is:

.. warning:: By default BOTH $read() and $readini() treat the text in the file as code!

So what are some of its consequences? Consider the following greet script:

.. code:: text

    on *:text:!setgreet*:#:{
      if (!$2-) { notice $nick Syntax Error: !setgreet <greet> | return }
      writeini greets.ini greet $nick $2-
      notice $nick [Greet] Greet Saved.
    }
    on !*:join:#:{
      if ($readini(greets.ini, greet, $nick)) {
        msg $chan [[ $+ $nick $+ ] $v1
      }
    }

Let's see what happens:

.. code:: text

    <Mike> !setgreet
    -Bot- Syntax Error: !setgreet <greet>
    <Mike> !setgreet Two things are certain in life, death and taxes. - Benjamin Franklin
    -Bot- [Greet] Greet Saved.
    /hop
    * Rejoined channel #foobar
    <Bot> [foobar] Two things are certain in life, death and taxes. - Benjamin Franklin
    <Mike> !setgreet Hello $findfile(C:\, *, 1, quit hacked!)
    -Bot- [Greet] Greet Saved.
    /hop
    * Rejoined channel #foobar
    * Bot (~Bot@isp.example.com) Quit (Quit: hacked!)

In this example Mike used the fact that $findfile() can execute a command when it finds a matching file. It should be clear how dangerous this can be. 

So how do we fix it? Using the **n** option!

.. code:: text

    $read(... , n, ...)
    ;and 
    $readini(..., n, ...)

Our new code would look like this:

.. code:: text

    on *:text:!setgreet*:#:{
      if (!$2-) { notice $nick Syntax Error: !setgreet <greet> | return }
      writeini greets.ini greet $nick $2-
      notice $nick [Greet] Greet Saved.
    }
    on !*:join:#:{
      if ($readini(greets.ini, n, greet, $nick)) {
        msg $chan [[ $+ $nick $+ ] $v1
      }
    }

$calc()
^^^^^^^

ALL unknown (in advance) input to $calc should be validated. $calc has its own special evaluation routine, it possesses the ability to double evaluate variables and identifier if their value returns a %variable. Consider the following code:

.. code:: text

    //var %x = 12345 | tokenize 32 % $+ x | echo -a $1 = $calc($1)

Which will produce the following result: 

.. code:: text

    %x = 12345

**Surprise!** We bet you did not expect that to happen. (This is actually a side effect of $calc being able to evaluate variables inside parenthesis or immediately after an operator without a space.) 

Now let's take a look at a more practical example:

.. code:: text

    ; Assume %password is set to 123456
    on *:connect:{
      autojoin -d5
      if ($network == UnderNet) {
        msg x@channels.undernet.org login Wiz126 %password
      }
    }
    on *:text:!calc *:#:{
      msg $nick [Calc] $2- = $calc($2-)
    }

Like most people, this user has an on connect event to register his user and a simple !calc script. 

Let's see what Mike can do to him:

.. code:: text

    <Mike> !calc 3*5+55
    <Wiz126> [Calc] 3*5+55 = 70
    <Mike> !calc %password
    <Wiz126> [Calc] %password = 123456

It's clear how Mike was able to get the value of a pretty important variable. 

It's important to note that EVEN if %password was set to "1234rosebud". The $calc() will return "1234", which is not the whole password but it's a big chunk of it.

A simple way to prevent this from happening with such a script is to restrict the usage to input which do not contain identifiers and %variables:

.. code:: text

    on *:text:!calc *:#:{
      if (!$regex($2-,/\$\S+|%\S+/)) {
        msg $nick [Calc] $2- = $calc($2-)
      }
    }

$decode
^^^^^^^

This is not really an exploit, but is a way for someone to disguise their malicious command. It can't be executed except by someone taking advantage of the $iif() bug below, or else as part of a script. When a /command is typed in a channel editbox, it will not let anything be executed if it's a command which begins with a % or a $, but that behavior does not extend to remote scripts.

.. code:: text

    //var %cmd echo | [ %cmd ] 4 -a hello world


Pasting the above command into an editbox echoes 'hello world' to the active window in red text. However it won't work if the square braces are removed, because the command beginning with % halts the editbox command, but doesn't halt the same thing in a remote script.

Something similar can be done with $decode, but it only works if $decode(string) is placed somewhere which allows its contents to be evaluated/executed, which includes the $iif bug, placing into a timer's command line, inside square braces, etc. Below shows how the decode string is created, but the echo command is NOT executed by $decode, but by the fact that the decoded string is placed into the timer's command string. If the "timer 1 1" had not been there, this would have executed the echo command if it were inside a remote script, but would not have executed in the editbox simply because the editbox doesn't execute commands beginning with % or $.

.. code:: text

    //var -s %a $remove($encode(echo 4 -a hello world,m),=) | timer 1 1 $decode(ZWNobyA0IC1hIGhlbGxvIHdvcmxk,m)

$findfile $finddir $hfind $dllcall etc
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This category relates to identifiers who have a 'command parm' or a 'callback alias' where a malicious command could be placed. It's harder for $hfind and $dllcall to be exploited, because they require knowing the name of an existing hashtable or the pathname to a dll file. However, there's always at least 1 filename in the $mircdir folder, so the following /noop command can be used to execute the encoded echo command contained in $findfile's command parm. Again, the $decode command is not executing the command, it's just disguising the command that has been placed into a location which executes code placed there. The following 3 commands are doing the exact same thing, with the only difference being that $decode is hiding what the payload command actually is.

.. code:: text

    //noop $findfile(.,*,1, $decode(ZWNobyA0IC1hIGhlbGxvIHdvcmxk,m) )
    //noop $findfile(.,*,1, $+(echo 4 -a hello world) )
    //noop $findfile(.,*,1, echo 4 -a hello world )

Injection via Bugs
------------------

There are currently a few bugs in mIRC that allow for mSL injection, most in a round-a-bout fashion

$iif( (cond) /cmd, true, false )
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Due to the way mIRC handles $iif() statements, by wrapping a condition in parens and then appending a command, mIRC will execute/eval the command/identifier.

.. code:: text

    //echo -a $iif( (1) echo -a See what I mean, truthy, falsey)

The above will echo "See what I mean /!return 1", and neither the truthy or falsey statements are returned nor is the outter echo statement executed.
This is happening because internally, $iif is calling the /if construct in the following way:

.. code:: text

    //if (condition) !return 1 | !return 0

which gives:

.. code:: text

    //if ( (1) echo -a See what I mean) !return 1 | !return 0

And the quirk is there, this syntax actually executes the echo command.

The abuse of this is limited as the user of mIRC would either have to code the malformed $iif() statement or be tricked into issuing it from something such as the editbox. Be careful!

Injection via mIRC configuration
--------------------------------

You should inspect your mIRC settings for certain things which can be used to exploit you. If you check these things, you can help defend against some exploits which depend on a combination of factors, where just severing 1 link in the chain prevents the exploit.<br>

First, check the Options menu of your Alt+R scripts editor. It's a good idea set a few options here which can prevent problems.

Identifier Warning
^^^^^^^^^^^^^^^^^^

This halts a script when an invalid identifier name is used, rather than evaluating the identifier as $null. The error warning can alert you to a script error which can cause it to not do as you expect.

.. code:: text

    alias identwarntest {
      $nosuchidentifier echo -a hello world
    }

If you do not have identifier warning, and the above identifier is the mis-typing of an identifier which was supposed to return either "echo -a" or "notice $nick" or "msg #channel", then without identifier warning being checked, that identifier evaluates to $null, causing the remainder of the command to be executed. If the 1st word is not a valid command, mIRC sends the command to a server in case that's a valid server command, which makes it possible to leak sensitive info in some cases. By halting the script with an identifier warning, this gives a chance to fix your script.

Initialization Warning
^^^^^^^^^^^^^^^^^^^^^^

This warns if the /load command or the script-editor's /file/open has loaded a script containing ``:START:`` or ``:LOAD:`` events which would execute code immediately. This still doesn't defend against scripts containing ``:TEXT:`` or other events which could be triggered \*later\*, and doesn't defend if /reload was used instead of /load.

Monitor File Changes
^^^^^^^^^^^^^^^^^^^^

This warns if a loaded script has changed without being changed by the scripts editor itself. Sometimes it can be caused by your editing scripts in a 3rd party editor such as notepad, but it could also be caused by a script using /write to alter itself or a different script.

It's possible to have a script loaded that you don't realize. ``//write $chr(160) test | .reload -rs999 $chr(160)``

This creates a file without a filetype, where the filename itself is not visible in most fonts, then loads it as a remote script. All you see in the script editor's "view" menu is an extra-thick border at the bottom of the scripts list, and if you have too many scripts loaded, it's hiding inside the "more" list. This next command lists all the scripts you have loaded. If you see a line showing nothing between the double quotes or is something you don't recognize, you should investigate and possibly unload it.

.. code:: text

    //var %i 1 | while ($script(%i)) { echo -a %i : $qt($nopath($script(%i))) | inc %i }


Restricting DCC Get Filetypes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You should view the contents of your downloads folder with suspicion if you don't know from whom you received the file. If you disable filetype blocking, you should do it temporarily, by using the "turn ignore back on in xx minutes" feature, which causes the 'disable' choice to revert back to the prior 'accept only' or 'ignore only' setting.

While you can either configure Options/DCC/Ignore as 'ignore only' to specify a list of filetypes to be blocked, or as 'accept only' to specify a list of the only filetypes accepted, 'ignore only' requires updating the list as new executable filetypes need to be added. It's probably better to use 'accept only', since this allows you to manage the list of the only filetypes which are accepted. You should block all executable filetypes, without expecting to be able to inspect the download folder for suspicious items.

.. code:: text

    //var %a $chr(8238) $+ piz.!wen.oediv.ezicr.exe | echo -a write %a test

As you can see from the above command, this is a filename ending with .exe, which means it's an executible filetype. However, if your windows font is unicode-aware, and you use "/run ." to view the contents of your mirc folder, you'll see that this .exe file appears as if it's a .zip file. If someone created an .exe file containing the icon normally associated with .zip files, then renames it to this filename, and then uses DCC to send this file to you - it would appear as if it's a .zip file that's safe to click on to view the contents. This next event handler creates a log of the files you've received via DCC, and allows you to check later to see who sent an unknown file to you.

.. code:: text

    on *:FILERCVD:*:{
      write getlog.txt $time(yyyy.mm.dd HH:nn:ss) $network $nick $get(-1).ip $address($nick,5) $get(-1).size file: $filename
    }
