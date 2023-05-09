$com
====

$com calls a member of an open COM connection with the specified method and parameter, or returns informations about a currently opened COM or returns the value of the specified variable name

Synopsis
--------

.. code:: text

    $com(name,member,method,type1,value1,...,typeN,valueN) - calls a member of an open COM connection with the specified method and parameters, returns 1 if the call succeeds, 0 = fail.
    
    $com(name/N,varname) - returns the value of the specified variable name
    
    $com(name/N) - returns the name of the Nth open COM connection or the name of that connection if it's open

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - name/N
      - The name of the connection or the Nth connection
    * - varname
      - The name of a variable previously saved
    * - member
      - The name of the function of the object
    * - method
      - A combination of the following value added together:

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Value
      - Method
    * - 1
      - DISPATCH_METHOD - Call a member of an object
    * - 2
      - DISPATCH_PROPERTYGET - Return a value
    * - 3
      - (1+2) Call a member and return a value *
    * - 4
      - DISPATCH_PROPERTYPUT - Set a property
    * - 5
      - (1+4) Set a property with a member call *
    * - 6
      - (2+4) Set a property and return a value *
    * - 7
      - (1+2+4) Set a property and return a value with a member call *
    * - 8
      - DISPATCH_PROPERTYPUTREF - Set a property by reference
    * - 9
      - (1+8) Set a property by reference with a member call *
    * - 10
      - (2+8) Set a property by reference and return a value *

* type1 - The variable type, can be:

.. list-table::
    :widths: 15 30 55
    :header-rows: 1

    * - Type
      - Description
      - Value
    * - i1
      - single byte signed integer
      - 0 to 225
    * - ui1
      - single byte unsigned integer
      - 0 to 255
    * - i2
      - two byte signed integer
      - -32768 to 32767
    * - ui2
      - two byte unsigned integer
      - 0 to 65535
    * - i4
      - four byte signed integer
      - +/- 2147483647
    * - ui4
      - Holds unsigned 32-bit (4-byte) integers
      - 0 through 4,294,967,295
    * - int
      - integer
      - -2147483648 to 2147483647
    * - uint
      - unsigned integer
      - 0 to 4294967295
    * - r4
      - real, 4-byte floating point number
      - 1.17549435E-38 to 3.40282347E+38 
    * - r8
      - double real, 8-byte floating point number
      - 2.2250738585072014E-308 - 1.7976931348623157E+308 
    * - cy
      - eight byte curreny number
      - -922337203685477.5625 to 922337203685477.5625
    * - date
      - contains date and time, stored as an 8-byte floating-point number
      - +/-79,228,162,514,264,337,593,543,950,335
    * - decimal
      - Holds signed 128-bit (16-byte) values representing 96-bit (12-byte) integer numbers.
      - +/-79,228,162,514,264,337,593,543,950,335
    * - bool
      - contain any string or numeric representation.
      - n/a
    * - bstr
      - null-terminated unicode character string value.
      - A string can contain from 0 to approximately 2 billion (2^31) Unicode characters.
    * - variant
      - can contain string, date, time, boolean, or numeric values. When used, a data type must follow it
      - variant int 5	 
    * - dispatch
      - This data type indicates a pointer to an IDispatch interface on an OLE object (DBTYPE_IDISPATCH).
      - n/a
    * - unknown
      - This data type indicates a pointer to an IUnknown interface on an OLE object (DBTYPE_IUNKNOWN).
      - n/a
    * - error
      - This data type indicates a 32-bit error code (DBTYPE_ERROR)
      - n/a

You can pass a binary variable by prefixing the type of the variable with an '&' sign eg. $com(name,member,method,&bstr &binvar)

To make a variable by reference, postfix the data type with an asterisk and a variable name, for example: ``int* pIntOfBeer``.

* value1 - the value assigned to the variable type

Properties
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Property
      - Description
    * - .progid
      - returns the object name
    * - .result
      - returns the value returned by the COM object member call, you can save this result to a binary variable with $com(name/N,&binvar).result
    * - .error
      - returns the error value, if there were any error
    * - .errortext
      - returns the error description associated with the .error value
    * - .argerr
      - returns the Nth argument that caused the error, if the error were due to an invalid variable type.
    * - .dispatch
      - returns the name of the dispatched pointer if it exist
    * - .unknown
      - returns the name of the unknown pointer if it exist
    * - .inuse
      - returns $true if the current com connection is in use

When only one parameter is passed to $com (name/N), you can use the above properties.
In the case of retrieving an unknown pointer, mIRC will extend it to a dispatch pointer if it can, allowing you to call it directly via $com().

Example
-------

Compatibility
-------------

.. compatibility:: 5.9

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$comval </identifiers/comval>`
    * :doc:`$comerr </identifiers/comerr>`
    * :doc:`/comopen </commands/comopen>`
    * :doc:`/comclose </commands/comclose>`

