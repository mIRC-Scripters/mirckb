$submenu
========

$submenu can be used in popups definition to dynamically create a popup

Synopsis
--------

.. code:: text

    $submenu($id($1))

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - $id
      - The name of the identifier called by mIRC, the parameter passed to it is always $1, used by mIRC to pass information to your identifier.

It calls $id first with the parameter "begin" then will pass an incremented integer starting at 1 and will increase as long as you return a correct popups definition, then will send "end" 

.. note:: You cannot use this to create nested submenus, it will only build one single submenu.

Properties
----------

None

Example
-------

.. code:: text

    menu status {
      Animal
      .$submenu($animal($1))
    }
    alias animal {
      echo -s > $1
      if ($1 == begin) return -
      if ($1 == 1) return Cow:echo Cow
      if ($1 == 2) return Llama:echo Llama
      if ($1 == 3) return Emu:echo Emu
      if ($1 == end) return -
    }

More examples
~~~~~~~~~~~~~

*The following text was written by blue-elf* [1]_

Unfortunately, the mirc.hlp only provides a very simple example on $submenu. To explain $submenu better is to show examples. So here's the first one:

First create the following alias:

.. code:: text

    alias _partchan {
      if ($1 == begin) return -
      if ($chan($1) ischan) return $ifmatch :part $ifmatch
    }

If you type //echo -a $_partchan(1) and the first channel that you're on is #mirc, it'll show up:

.. code:: text

    #mirc :part #mirc

At first glance, it may seem useless. But if you apply that to $submenu, something wonderful happens

Now in your channel popups, put the following:

.. code:: text

    Part
    .All Channels:partall
    .$submenu($_partchan($1))

And see what it does. What happens is, mIRC takes every channel that you're on and puts it in the popups. The popup creation is 'virtual' in the sense that you don't see it in any file. The old method of doing this would be to have in popups:

.. code:: text

    Part
    .All Channels:partall
    .-
    .$chan(1):part $chan(1)
    .$chan(2):part $chan(2)
    ; and so on, which is tediously repetitive and is very limiting

With the use of $submenu, our work has been cut down greatly. No more repetitive popup scripting.

Advanced examples
~~~~~~~~~~~~~~~~~

Another good use for $submenu is when you have a list of items. Supposing you have a %variable that contains channelnames. Let's say you have this variable:

.. code:: text

    %recent.channels #mirc,#ircnewbies,#irchelp,#mircscripts,#mircscripts.org

All you need to do is create an alias:

.. code:: text

    alias _recentchan {
      if ($gettok(%recent.channels,$1,44)) return $ifmatch :join $ifmatch
    }

Then paste the following in your popups:

.. code:: text

    Recent channels
    .$submenu($_recentchan($1))

And even more advanced examples
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

One very good thing about $submenu is that it also allows for $2, $3 and so on. Which means, you can supply other parameters in your custom identifier. Just remember that the $1 will always be a number.

Let's take that recent channels adventure to demonstrate the capabilities of $submenu.

Supposing you have three variables, for recent items. One variable for recent channels, one for recent servers, and one for recent nicks. We will have some variables as below (shown with their values):

.. code:: text

    %recent.join #mirc,#ircnewbies,#irchelp,#mircscripts,#mircscripts.org
    %recent.server irc.daxnet.no,twisted.ma.us.dal.net,mclean.va.us.undernet.org
    %recent.nick Kamek,tabo,blue-elf,Dark_Greg,fubik

You'll see later that the variables have been named with a purpose.
Create an alias as below:

.. code:: text

    alias _recent {
      if ($gettok($($+(%,recent.,$2),2),$1,44)) return $ifmatch : $2 $ifmatch
    }

Here's a breakdown of that alias: ``$+(%,recent.,$2) will create %recent.$2``

If the value of $2 is join, it will create the variable %recent.join if the value of $2 is nick, it will create the variable %recent.nick if the value of $2 is server, it will create the variable %recent.server

Putting it inside $(%recent.join,2) is actually putting it inside $eval. So now, if we have %recent.join, it will be evaluated and will return the actual value of that variable (the #mirc,#ircnewbies.. and so on).

Now, the $gettok shouldn't need explaining, and same goes for $ifmatch.

The reason why we named the variables that way, is to make it easier for us to create the $_recent identifier. Thus:

.. code:: text

    return $ifmatch : $2 $ifmatch

If I supply 'join' as the $2, it will become:

.. code:: text

    return $ifmatch : join $ifmatch

This speeds up scripting greatly, whether you're talking in terms of typing, or speed of the script itself - since you're using less if-else statements.
But anyway, going back to the subject of $submenu, put this in your popups, preferrably in menubar or status popups:

.. code:: text

    Recent
    .Servers
    ..$submenu($_recent($1,server))
    .Channels
    ..$submenu($_recent($1,join))
    .Nicks
    ..$submenu($_recent($1,nick))

Now, test it and see what happens. It's as though this was written in your popups:

.. code:: text

    Recent
    .Servers
    ..irc.daxnet.no : server irc.daxnet.no
    ..twisted.ma.us.dal.net : server twisted.ma.us.dal.net
    ..mclean.va.us.undernet.org : server mclean.va.us.undernet.org

And so on... the only difference is, mIRC is doing it internally for you.

Re-evaluating identifiers
~~~~~~~~~~~~~~~~~~~~~~~~~

Let's try some identifiers and variables inside $submenu identifiers. If you're used to dynamically creating your popups via the /write command, you're probably no stranger to using $!identifiers and % $+ variables. For the uninitiated, when writing to popup files, you'd need $!identifiers so that the actual value of the identifiers aren't written to the file, but the literal '$identifier' itself. The same is true for %variables.

How is this applicable to $submenu?

Let's say we want to use that part example above.

.. code:: text

    alias _part {
      if ($chan($1) ischan) return $ifmatch : part $ifmatch $!input(Enter message,1,Part)
    }

Notice how I used $!input as opposed to $input. This is to prevent mIRC from evaluating the $input command while it is creating the submenu (or the popup item).
So now, if you apply the above to the popups, it'll add an option for you to input a part message.

Similarly with variables, if you don't want the variable to be immediately evaluated, just use % $+ variablename.

Here's another alias for you to dissect:

.. code:: text

    alias _rfpop {
      var %c = $chan($1), %n = $gettok($3,1,33), %m = kick %c %n : $!+ $!input(Enter reason to kick %n from %c ,1,Kick)
      if ($2 == kb) %m = .raw mode %c +b $mask($gettok($3,2,33),2) $!+ $!lf $!+ %m
      else %m = .raw %m
      if ($1 isalpha) return -
      if ($comchan(%n,$1).op) return %c : %m
      if ($chan($1) ischan) return $!style(2) %c :return
    }

Even if you don't understand it, it's just to show that you have to use $!identifiers for things that need to be evaluated later on. One obvious example is the use of $!style(2). This puts a '$style(2)' in the popups, thus disabling the specific item nicely.

Hints and Tips
^^^^^^^^^^^^^^

The 'begin' and 'end' are optional. They signify if the $submenu identifier is just starting to create your submenus or if it's about to end creating them. At that point, you can make $submenu return a separator or the '-' character.
$submenu stops itself once you return a $null value. So be careful when you want to skip items. There are two ways of doing this:

#. You can either disable the item with $style.
#. Or you can skip the command part.

Here's an example:

.. code:: text

    alias _xpopmargin {
      if ((e isin $1) || ($1 == 1)) return -
      if ($1 isnum 2-20) return $1 :msg x@channels.undernet.org set $chr(35) floatmargin $1
    }

The above is an alias that blue-elf used for for setting the floatmargin for channels in Undernet. The floatmargin range is from 2 to 20. Which means that he had to find a way to skip the 1. But he couldn't make $submenu return a $null, otherwise, the popup items will not be created.

That is why he has this line:

.. code:: text

    if ((e isin $1) || ($1 == 1)) return -

This tells $submenu that if $1 is begin or end or 1, just make it return a - or a separator. Luckily for me, the popup appears like this:

.. code:: text

    Undernet
    .Level 450
    ..Set
    ...FloatMargin
    ....$submenu($_xpopmargin($1))
    ; a few more lines here and there

Which means that there will be two separators on top of each other. But the good thing is, they don't show up in this mIRC version. So he now has a clean FloatMargin item that starts with 2 and ends in 20.

Conclusion
~~~~~~~~~~

By now, you should have more ideas from these simple examples. It doesn't matter if you're using variables, ini files, hash tables, or even text files, $submenu can still be used. You just need a little bit of imagination, then you can have tons of fun with this identifier.

If you haven't realized by now, the actual trick with $submenu is not in the $submenu itself, but in the identifier that you supply to it.

Compatibility
-------------

.. compatibility:: 6.0

See also
--------

References
----------

.. [1]
    `Retrieved from blue-elf's tutorial (with minor edits) on submenu at mircscripts.org on webarchive <https://web.archive.org/web/20040906095629/http://www.mircscripts.org/showdoc.php?type=tutorial&id=1286>`__
