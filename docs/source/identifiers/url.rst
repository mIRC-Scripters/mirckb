$url
====

$url returns the current url in your main browser, or returns information about URL in the URL list window.

Synopsis
--------

.. code:: text

    $url

.. code:: text

    $url(<N>)[.properties]

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - N 
      - The Nth URL in the list or return the total number of URL if N = 0.

Properties
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Property
      - Description
    * - desc
      - Returns the description of the URL.
    * - group
      - Returns the group of the URL.

Example
-------

.. code:: text

    //echo -a $url

Compatibility
-------------

.. compatibility:: 4.7

See also
--------

.. hlist::
    :columns: 4

    * :doc:`/url </commands/url>`

