$&
==

$& is a construct which allows you to break up long, single script lines in order to make editing and reading them much easier.

.. note:: $& can touch the end of your line and still be valid, see the example

Synopsis
--------

.. code:: text

    $&

Parameters
----------

None

Examples
--------

An alias that breaks up a long echo into multiple lines

.. code:: text

    alias testit {
      echo -a This is a really long$&
        line that is broken up because $&
        mIRC supports it! The cool thing is $&
        that mIRC will also format these $&
        indentations within the script editor!
    }

Create an alias that has a code block similar to a programming language

.. code:: text

    alias testit {
      if ($me isin $+(Hello, $me,! How are you?)) $&
        {
        echo -a This code block resembles some popular programming languages.
      }
    }

.. note:: Non-spaces are not permitted following it on the same line, and this reports there is no such identifier (unless you create a custom identifier named '&')

.. code:: text

    //echo -a foo $& bar

Compatibility
-------------

.. compatibility:: 5.5

See also
--------
