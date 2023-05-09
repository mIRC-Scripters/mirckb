$unsafe
=======

$unsafe is designed to be used with, for example, external user input in commands that may evaluate text later on, such as /timer commands. It delays evaluation of text for one level of evaluation.

Synopsis
--------

.. code:: text

    $unsafe(text)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - text
      - a string

Properties
----------

None

Example
-------

.. code:: text

    //tokenize 32 $!me | timer -ho 1 0 echo -a $unsafe($1-)

See :doc:`injection </beginner/injection>` for more informations.

Compatibility
-------------

.. compatibility:: 7.44

See also
--------

.. hlist::
    :columns: 4

