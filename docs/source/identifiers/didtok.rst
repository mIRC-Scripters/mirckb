$didtok
=======

$didtok returns a tokenized list of the item(s) of a dialog's combo, list, or edit box

Synopsis
--------

.. code:: text

    $didtok(name,id,C)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - name
      - Name of the dialog. Must be open
    * - id
      - The number of the dialog control
    * - C
      - ASCII value used to separate the returned tokens. 32 is space, 44 is comma, 9 is tab, 46 is period, etc.
      
Properties
----------

None

Example
-------

.. code:: text

    dialog sample1 {
      size -1 -1 200 200
      option dbu
      combo 987,10 10 50 10, drop
    }
    on *:dialog:sample1:init:*:{
      var %days Sunday Monday Tuesday Wednesday Thursday Friday Saturday
      didtok $dname 987 32 %days
      did -c $dname 987 $findtok(%days,$asctime($ctime,dddd),1,32)
    }

.. code:: text

    /dialog -ma sample1 sample1
    //echo -a The items in the list are $didtok(sample1,987,10004) and the selected item is $did(sample1,987).seltext
      The items in the list are Sunday✔Monday✔Tuesday✔Wednesday✔Thursday✔Friday✔Saturday and the selected item is Monday

Compatibility
-------------

.. compatibility:: 5.7

See also
--------

.. hlist::
    :columns: 4

    * :doc:`/dialog </commands/dialog>`
    * :doc:`/did </commands/did>`
    * :doc:`$did </identifiers/did>`
    * :doc:`/didtok </commands/didtok>`

