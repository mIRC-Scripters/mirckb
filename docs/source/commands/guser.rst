/guser
======

The **/guser** command looks up the address of the specified nick and adds it to the user list. It does this by doing a **/userhost** on the given nickname, and returning an address in the format specified by [type]. If [type] is not specified then a default address format is selected.

Synopsis
--------

.. code:: text

    /guser [-a] <levels> <nick> [type] [info]

Switches
--------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - -a
      - if the user already exists, the specified levels are added to the current levels the user has

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - <levels>
      - a list of levels seperated by commas
    * - <nick>
      - the nickname you want to add the address from
    * - [type]
      - if not specified, mIRC uses a default type: 6
    * - [info]
      - append text to the entry that is added to the users list

Example
-------

.. code:: text

    alias F12 {
      ; Adds $1 to Users - Level 20
      guser 20 $$1 2 $1
      ; Toggles nick color to Yellow in the Users List
      cline -hlm 8 $chan $1
    }

Compatibility
-------------

Added: 3.3 - 3.4

.. note:: Unless otherwise stated, this was the date of original functionality. Further enhancements may have been made in later versions.

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$ulevel </aliases/ulevel>`
    * :doc:`/auser <auser>`
    * :doc:`/flush <flush>`
    * :doc:`/iuser <iuser>`
    * :doc:`/rlevel <rlevel>`
    * :doc:`/ruser <ruser>`
    * :doc:`/ulist <ulist>`
