$didreg
=======

The $didreg identifier return the number of the line that matched the regular expression in dialog's control.

Synopsis
--------

 $didreg(name,id,regex,N)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - name
      - name of the dialog
    * - id
      - id of the control, can be a list, editbox, and combo
    * - N
      - optional, if N is passed, start matching at the Nth line
    * - regex
      - the regular expression.

Properties
----------

None

Example
-------

None

Compatibility
-------------

.. compatibility:: 6.1

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$didtok </identifiers/didtok>`
    * :doc:`$didwm </identifiers/didwm>`
    * :doc:`/dialog </commands/dialog>`
    * :doc:`/did </commands/did>`
    * :doc:`/didtok </commands/didtok>`

