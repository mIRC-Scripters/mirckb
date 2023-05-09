$comcall
========

$comcall calls a member of an open COM connection with the specified method and parameter, it is multithreaded and won't halt the script, an alias is called once the call returns.

If $comcall() fails when calling an object and $com() does not, this means that the object is not compatible with the threading model of mIRC, so $com() must be used. You can check the $comerr value in the alias to determine if a $comcall() failed or not.

Synopsis
--------

.. code:: text

    $comcall(name,alias,member,method,type1,value1,...,typeN,valueN)

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - name
      - The name of the connection or the Nth connection
    * - alias
      - The name of an alias that will be called once the call returns
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
      - -128 to 127
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

To make a variable by reference, postfix the data type with an asterisk and a variable name, for example: int* pIntOfBeer.

* value1 - the value assigned to the variable type

Properties
----------

None

Example
-------

.. code:: text

    alias runVbs {
      var %s = $mircdir $+ foo.vbs
      write -c foo.vbs  Dim c $lf c = 0 $lf Do While c < 10000000 $lf c = c + 1 $lf Loop
      .comopen x WScript.Shell
    
      ;mode 1 = comcall
      if ($1 == 1) noop $comcall(x, cbthread, Run, 1, bstr*, %s, int, 1, bool, 1)
      else {
        noop $com(x,  Run, 1, bstr*, %s, int, 1, bool, 1)
        .comclose x
      }
    }
    alias cbthread echo -a done | .comclose x
    
Compare //var %t $ticks | runvbs 1 | echo -a $calc($ticks - %t) vs //var %t $ticks | runvbs 2 | echo -a $calc($ticks - %t)

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

