$fromeditbox
============

$fromeditbox returns $true or $false depending on if the alias was called from a mIRC editbox

Synopsis
--------

.. code:: text

    $fromeditbox

Parameters
----------

None

Properties
----------

None

Example
-------

define the alias testedit:

.. code:: text

    alias testedit echo -a $fromeditbox

and then:

.. code:: text

    //echo -a $fromeditbox | testedit

Compatibility
-------------

.. compatibility:: 7.52

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$caller </identifiers/caller>`

