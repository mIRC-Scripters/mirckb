/signal
=======

The **/signal** command is used to send a signal to all loaded script, if one of them has a matching :doc: `on signal </events/on_signal>` event, it triggers. Signals are a simple way of triggering signal events in multiple scripts at the same time.

Synopsis
--------

.. code:: text

    /signal [-n] <name> [parameters]

Switches
--------

**-n**: This flag tells the */signal* command to fire immediately instead of waiting for the end of the whole current script processing, this implies nested call to signal event and also recursion can be made, though the maximum you can get is 24 iterations. If you don't provide the -n switch, mIRC waits for the end of the whole current script processing and then triggers any matching events.

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <name>
      - the name of a signal event
    * - [parameters]
      - the optional parameter passed to the signal event

Examples
--------

Let's check out an example of a signal command below:

.. code:: text

    /signal mysignal Signal information!

Once you've executed this command, it will send a **signal** named *mysignal* to all scripts in your mIRC remotes. Any script files that have signal event listening for that signal will trigger, and perform whatever tasks they have been set to perform.

.. code:: text

    ON *:SIGNAL:mysignal:echo -s rcvd: $signal : $1-

Identifiers
-----------

* **$signal** - Returns the signal name of the signal which triggered the current event.
* **$1-** - Returns any optional parameters that have been passed along with the signal.

Example Script
--------------

Now that we know some basic data that can be obtained from a signal, as well as how to trigger a signal and listen for a signal, let's create a signal and an event that puts these signals to good use!

Useful Scenario
^^^^^^^^^^^^^^^

First, we need to think of something that would make a signal useful. Although signals are useful in simple scenarios, more difficult scenarios can truly pinpoint just how useful these signals can be. How about delaying an auto join script until after your auto identifier script has identified you to a network's NickServ? Let's get into some details.

Some networks allow users to have their own, personalized virtual hosts, which change their host masks to any vanity they would like. Host masks are in the form *username@their.isp.address.net*. If you've ever performed a */whois* on a nickname on an IRC network, this will look familiar. What a vHost will do, when a network offers and or provides you with one, is they mask your true host, and usually they can be vanity, meaning you can make them anything you desire. For example, you could make yours *username@ILOVEmIRCScripting.net*. It can really be any combination of letters and numbers you'd like.

The personalized vHosts will only activate once you have properly identified yourself to NickServ. Once you're identified, your host becomes a vHost mask/vanity, and then your true connection ID is hidden. Well, what if your auto join triggers before you've properly identifed to NickServ services? The vHost would be useless, as your true identity would already have been exposed to the channel upon joining.

This is where a signal can truly shine, and next we are going to show you how :)

Code
^^^^

First, what should we name our signal? How about *delayAutoJoin*? That works, and it identifies the purpose of the signal. Next, which script should perform the */signal* command, the auto join, or the auto identifier? Well, just remember that we don't want to join channels until the auto identifier has completed. In this case, we can ascertain that the auto identifier should be the one to trigger the command, the auto join should listen for the signal.

Let's go to our auto identifier and setup our script:

.. code:: text

    ON *:NOTICE:*This nickname is registered*:?:{
    ; Check to make sure NickServ issued this notice,
    ; and then identify our nickname with our password

    .. note:: mypassword is an example password; you would insert

    ; your real password here)
    if ($nick == NickServ) { ns identify mypassword }
    }

Alright, so what have we done? This event listens for NickServ to send you a notice requesting that you identify yourself to this registered nickname. If that event triggers, next thing we do is check to make sure the nickname who sent us the notice was actually NickServ (security purposes, optional but recommended). Finally, if the nickname was NickServ, send the identification command which includes our password.

.. note:: For the most part, most NickServ requests like this are defaulted for cross-platform compatibility. Using this example is most-likely fine, but do some research for your own NickServ's requests to properly utilize the above event.

Next, let's check for when NickServ acknowledges that we've properly been identified by letting us know our vHost is now applied:

.. code:: text

    ON *:NOTICE:*Your vhost*activated*:?: {
    ; Send the delayAutoJoin signal to all listening scripts
    signal delayAutoJoin
    }

This event waits for the NickServ notice letting us know our vHost has been activated, and then sends a signal with the name *delayAutoJoin* to all currently loaded scripts. The auto identifier portion of our example is finished. Now we will move on to the auto join, where we will create our signal listener, and perform the auto join function. Remember, this portion of code belongs in the auto join, not the auto identifier:

.. code:: text

    ON *:SIGNAL:delayAutoJoin: {
    join #mychannel
    }

So, now our auto join script will listen for the signal, which will be triggered once our vHost has been successfully activated, and then join the channel(s) it has been coded to join. For all intense purposes, this event has been trimmed to the simplest possible explanation. It could be made much more extravagant, with an auto join list read from a hash table or an INI file.

Compatibility
-------------

Added: mIRC v6.0 (16 Aug 2002)

See also
--------

.. hlist::
    :columns: 4

    * :doc: `ON Events </intermediate/events.html>`
