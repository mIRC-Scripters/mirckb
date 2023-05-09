$didwm
======

The $didwm identifier return the number of the line that matched the :ref:`matching_tools-wildcard` expression in dialog's control.

Synopsis
--------

.. code:: text

    $didwm(name,id,wildcard,N)

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
    * - wildcard
      - the :ref:`matching_tools-wildcard` expression.

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
    * :doc:`$didreg </identifiers/didreg>`
    * :doc:`/dialog </commands/dialog>`
    * :doc:`/did </commands/did>`
    * :doc:`/didtok </commands/didtok>`

