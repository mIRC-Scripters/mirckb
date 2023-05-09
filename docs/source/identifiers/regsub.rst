$regsub
=======

$regsub performs a regular expression match and then substitute/replace, returns the number of match found and store the result in a %var or &binvar, more information about regex in mIRC :ref:`matching_tools-regex`

Synopsis
--------

.. code:: text

    $regsub([name],input,regex,subtext,%var|&binvar)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - name
      - The optional name of the regex, to be used later to retrieve captured group with :doc:`$regml </identifiers/regml>` or :doc:`$regmlex </identifiers/regmlex>`
    * - input
      - The input text
    * - regex
      - The regular expression for :ref:`matching_tools-regex`
    * - subtext
      - The text to use to replace the match, this parameter is evaluated once prior the regex call, you can use backreferences \1 \2 etc, but it doesn't support the markers of :doc:`$regsubex </identifiers/regsubex>` such as \t \n \A etc. , you cannot use :doc:`$regml </identifiers/regml>` or :doc:`$regmlex </identifiers/regmlex>` inside the subtext parameter since it's evaluated prior the regex call.

Properties
----------

None

Example
-------

.. code:: text

    //var %a | echo -a $regsub(abcd,/[a-z]/g,1,%a)

Compatibility
-------------

.. compatibility:: 5.9

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$regml </identifiers/regml>`
    * :doc:`$regsubex </identifiers/regsubex>`
    * :doc:`$regex </identifiers/regex>`

