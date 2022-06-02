/haltdef
========

The **/haltdef** command halts the default processing of an event. When mIRC is about to trigger an event, mIRC will first check for events that use the **^** prefix, and then check the regular events. After processing events using the **^** prefix, mIRC will apply the default action for that event, usually displaying text, but it can be highlighting a window etc.. Using /haltdef only have an effect inside an event using the **^** prefix, and will prevent mIRC from performing his default action.

.. note:: Not all events support the **^** prefix, you can find a list of events supporting the **^** prefix :ref:`here <caret-prefix>`.

Synopsis
--------

.. code:: text

    /haltdef

Switches
--------

None

Parameters
----------

None

Example
-------

With **^** prefix on event

.. code:: text

    on ^*:op:#mIRC:{
      haltdef
      echo -t #mIRC OP : $opnick by $nick
    }

And without **^** prefix

.. code:: text

    raw 312:*: {
      haltdef

      echo -at $2 using $3 - ( $+ $4- $+ )
    }

Compatibility
-------------

Added: mIRC v5.4 (23 Jun 1998)

.. note:: Unless otherwise stated, this was the date of original functionality. Further enhancements may have been made in later versions.

See also
--------

.. hlist::
    :columns: 4

    * :doc:`/halt <halt>`
    * :doc:`/return <return>`
