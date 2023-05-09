$bnick
======

$bnick refers to the nickname of the user either banned, or unbanned, during both an :doc:`on ban </events/on_ban>` Event, and an :doc:`on unban </events/on_unban>` Event.

.. note:: $bnick is not always set, because sometimes nicknames aren't even added to a certain ban/banmask.

Parameters
----------

None

Example
-------

Message any channel when a user has been banned

.. code:: text

    ON *:BAN:#: {
    
      ; We use this check to make sure the $bnick identifier
      ; has been filled, that way there are no unforeseen issues.
      if ($bnick) {
        msg # Looks like $bnick has been banned.
      }
    }

Message any channel when a user has been unbanned

.. code:: text

    ON *:UNBAN:#: {
    
      ; We use this check to make sure the $bnick identifier
      ; has been filled, that way there are no unforeseen issues.
      if ($bnick) {
        msg # Awesome! $bnick is now unbanned :)
      }
    }

Compatibility
-------------

.. compatibility:: 4.6

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$banmask </identifiers/banmask>`
    * :doc:`$ibl </identifiers/ibl>`
    * :doc:`/ban </commands/ban>`
    * :doc:`on ban </events/on_ban>`
    * :doc:`on unban </events/on_unban>`

