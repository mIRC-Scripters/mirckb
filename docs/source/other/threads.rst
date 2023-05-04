Threads
=======

This page aims to discuss threads in mIRC, delayed execution and non blocking while loop.

Thread
------

mIRC is single threaded, only :doc:`$comcall </identifiers/comcall>` and :doc:`$dllcall </identifiers/dllcall>` (and multimedia timer) are creating a new thread to execute, and then call a callback alias.

Sometimes it looks like mIRC can do multiple things at the same time without freezing, this is never the case, below we will discuss the different illusions that can occur.

mIRC's message loop
-------------------

mIRC, just like many Windows applications, is based on a loop which processes messages, messages correspond to some kind of event, new data on a socket, a click on a button etc.
For each iteration of the loop, one message only is processed and then the loop repeats.

This approach is what allows mIRC, or scripters to create the thread illusions.

Nested call to the message loop
-------------------------------

The trick is to "call" the message loop yourself (you or mIRC, typically), handling one more message while the current one is running (nested execution) before returning to handling this current message

$input
^^^^^^

mIRC itself, with $input, does this:

.. code:: text

    alias test {
    set %test 1
    noop $input(text,e)
    echo -a %test
    }

When you call /test, the scripting engine has to wait for your input before processing the rest of the code, represented by an infinite while loop.

Just waiting for your input would freeze mirc since no others messages would be processed (how things usually works), so mIRC itself call the message loop once per iteration of that infinite while loop, and process more messages.

This can be demonstrated by running /test above, from a desktop window, (possibly with the 'u' switch of $input?) and then going back to mIRC and executing /set %test 2, when $input returns, 2 will be displayed, showing that $input allowed you to click back to mirc and running the scripting engine with /set, all of which are the result of handling the message loop

Whilefix Dll
^^^^^^^^^^^^

For a very long time, a dll called whilefix.dll exists which will 'fix' your while loop in mIRC (pretty catchy isn't it?).

What this dll does is exactly what $input does, it calls the message loop and allow more message to be processed:

.. code:: text

    while (condition) {
      ;call the WhileFix routine
      dll path\to\whilefix.dll WhileFix
      your code here
    }

And this loop will never freeze mIRC.

/pause /sleep COM delayed script
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Since a very long time as well, :doc:`COM </advanced/com>` script to pause the execution of your script exist (pausing can be done with timers, just not as handy):

.. code:: text

    alias pause {
      if ($1 !isnum 1-) return
      var %a = $ticks $+ .vbs
      write %a wscript.sleep $1
      .comopen %a wscript.shell
      if (!$comerr) .comclose %a $com(%a,Run,3,bstr,%a,uint,0,bool,true) 
      .remove %a
    }
    alias mycode {
      do something
      ;wait 5 millisecond before continuing 
      pause 5
      do something else
    }

This time it's Windows which is calling the message loop, mIRC does not know in advance which kind of COM you're using or most likely does not want to deal with this itself.

Critical and non critical events
--------------------------------

Ever wondered why you can't call $input from an on text event? This is related to the message loop.

All messages from the message loop which are related to sockets (mIRC's internal socket used for IRC, not socket created from :doc:`/sockopen </commands/sockopen>` or :doc:`/sockudp </commands/sockudp` can be called critical events whereas any other message (clicking on a nick in the nicklist for example) is considered a non critical event.

Socket related messages are called critical because mIRC cannot handle these messages if they are to be handled from a nested call of the message loop.

Indeed, imagine if mIRC allowed the usage of $input in critical event and allowed the processing of socket messages in nested call:

.. code:: text

    on *:text:!test:#test:noop $input(test,e)
    on *:text:*:#test:do stuff

If someone says !test on the channel, $input is called and as we saw above, mIRC will call the message loop until $input returns, now suppose a new message "test" is sent on the channel while your $input is running, since mIRC is processing the message loop, it would process this channel message and the second on text would trigger, this is not wanted, the first on text has to finish first to guarantee correct order of execution, this is why $input is not allowed in critical event, you can try to use $input inside mIRC's event to see if they are critical (as said only socket related events should return an error).

.. note:: mIRC could totally allow $input to be used from critical events while not allowing the processing of socket messages in nested call, it's a bad idea because it would wait for your reply before processing these socket messages, meaning that a ping messages sent by the IRC server would not be handled until you provide an input, effectively disconnecting you from the IRC server just like an infinite while loop.

Watch out
---------

As we have seen, mIRC prevents you from using $input from critical event, but mIRC can't prevent you from using a dll which call the message loop (whilefix) or from using a COM delaying script, resulting in Windows calling the message loop.

Consider this:

.. code:: text

    on *:text:!mytrigger:#:{
      while (condition) {
        dll whilefix.dll Whilefix
        ;rest of your code here
      }
    }

You are using whilefix because you are doing a loop that is processing a lot of things, or well, because the loop is long enough to freeze your mIRC.
What happens here is that whilefix calls the message loop, but from a critical event: socket messages are not processed, on text won't be processed again while your loop is running.

Note that this is in theory not a problem because your while loop is freezing mIRC to begin with, meaning that, to begin with, the on text event won't ever be triggered again before the loop finishes.

If whilefix isn't much a problem given the nature of situation (you can't get critical event (or non critical event in this case) to be processed if you are in a while loop without whilefix), COM delaying scripts are more problematic:

.. code:: text

    on *:text:!mytrigger:#:{
       ;something
       pause 5 
       ;rest of your code here
    }

If you do that, nested call to the message loop occurs and it's the same idea as above: your on text event is not processed until the pause finishes.

However this time, not using a pause script doesn't create any freeze (compared to a while loop not using whilefix). And pausing event like that is not something you want to do.

Delaying the execution can be done with :doc:`/timer </commands/timer>`, all the time, and this solution does not cause any problem so should be the preferred solution.
That being said /timer are not handy, they make you lose the 'scope':

.. code:: text

    on *:text:!mytrigger:#:{
       noop
       pause 5
       echo -a $nick 
    }

vs

.. code:: text

    on *:text:!mytrigger:#:{
       noop
       .timer 1 5 more
    }
    alias more echo -a $nick

In the second example $nick simply does not have a value, mIRC left the on text event 5 seconds ago, $nick is meaningless, you have to pass $nick to the "more" alias, and timers are problematic that way, see the :doc:`msl injection </beginner/injection>` page about timers.


.. note:: Thanks to Saturn and http://www.xise.nl/mirc/ for the original idea and documentations.
