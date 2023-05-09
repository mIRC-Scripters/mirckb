$show
=====

$show returns :doc:`$true </identifiers/true>` if the alias is called silently with the dot '.' prefix, :doc:`$false </identifiers/false>` otherwise.

.. note:: custom aliases called inside a silenced custom alias will be silenced as well with no way to make them non silenced, see second example

Synopsis
--------

.. code:: text

    $show

Parameters
----------

None

Properties
----------

None

Example
-------

1.

.. code:: text

    alias test {
      echo -a test $1- $ $+ show== $+ $show
    }
    alias script_test {
      test Called from a script without a dot:
      .test Called from a script with a dot:
    }

Type /script_test

2.

.. code:: text

    alias test {
      echo -ag test show $show
      test1
    }
    alias test1 {
      echo -ag test1 show $show
    }

Type /test vs. /.test, notice how /test1 will say that $show is $false when you use /.test, despite the /test1 call not being silenced inside the alias test.

Compatibility
-------------

.. compatibility:: 5.3

See also
--------

.. hlist::
    :columns: 4

