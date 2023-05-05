/didtok
=======

The **/didtok** command adds the tokenized list to the specified control.

Synopsis
--------

.. code:: text

    /didtok <name> <id> <C> <text>

Switches
--------

None

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <name>
      - the name of the dialog
    * - <id>
      - the id of the control
    * - <C>
      - the code point of the character used as a delimiter in your list
    * - <text>
      - the list of token to be displayed

Example
-------

.. code:: text

    ;put in remote:
    dialog colors {
    size -1 -1 100 200
    list 1, 10 10 80 180
    }

    ;then execute in mIRC:
    //dialog -m colors colors | didtok colors 1 32 red blue orange yellow

Add the following list of colors to the list in the dialog

Compatibility
-------------

Added: mIRC v5.7 (07 May 2000)

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$didtok </identifiers/didtok>`
    * :doc:`$did </identifiers/did>`
    * :doc:`$dialog </identifiers/dialog>`
    * :doc:`$didwm </identifiers/didwm>`
    * :doc:`$didreg </identifiers/didreg>`
    * :doc:`/dialog </commands/dialog>`
    * :doc:`/did </commands/did>`
