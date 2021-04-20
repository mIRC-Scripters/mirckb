COM
===

Component Object Model (COM) is a specification for applications (like exe and dll files) to make their functionality available to any COM-compliant application. The applications interact with each other through a collection of functions called interfaces. The advantages of COM objects are that they are object-oriented, customizable, modular, upgradeable, and language-independent. Regardless of in which language they were programmed, any other language/script that supports the COM specification will be able to use it. mSL offers a variety of commands and identifiers to handle COM objects.

Com objects
-----------

A COM object is a component that exposes the application's properties, methods, and events. COM objects are identified by a unique string called a Programmatic IDentifier or ProgID.

Some examples of COM object with their ProgIDs:

  - iTunes.Application - an interface that lets you interact with the iTunes application
  - WScript.Shell - an interface that provides access to the native windows shell
  - Shell.Application - an interface that provides methods to control the shell and execute commands within the shell, as well as methods to obtain other shell-related objects.
  - MSScriptControl.ScriptControl - an interface that provides methods to evaluate and execut scripts (The MSScript control supports VBScript and JavaScript scripting languages)
  - Word.Application - an interface that provides methods and properties associated with the Word application.
  - WMPlayer.ocx - An interface that provides methods and properties associated with the windows media player program

.. note:: A single computer might have thousands of COM objects available.

Opening and closing a COM connection
------------------------------------

To open a COM connection to a specific object, we use the following syntax:

.. code:: text

  /comopen <hName> <progid>

The ``<hName>`` is the handle name of the COM connection to which we will need to refer to at a later time to call methods from this object. It is wise to name it something meaningful. The ``<progid>`` is the programmatic identifier we discussed earlier.

To close the COM connection, we need to use the handle name we used to create that connection.

.. code:: text

  /comclose <hName>

Before we can go on to use the COM object, we have to confirm a successful connection has been established. The $comerr will return 1 if the connection has failed, 0 otherwise.

Connecting/Disconnecting Example
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Below is a simple example of connecting to the windows script shell and disconnecting.

.. code:: text

  alias example {
    .comopen shellCOM WScript.Shell
    if ($comerr) {
      echo $color(info) -aet * Error connection to the Windows Script Host
    }
    else {
      ;no errors, continue here
      .comclose shellCOM 
    }
  }

Object interaction
------------------

Before we can talk about how to interact with the COM object we have connected to, we have to discuss a few other things first.

Members
~~~~~~~

Object's Members are all the methods and properties that are provided by the Object. Later on, we will be able invoke these members. For example, The WScript.Shell object has as an Exec method that lets us run an application in a child command-shell. Here is a link to a complete list of properties and methods that the WScript.Shell object has.

Invoke method
~~~~~~~~~~~~~

The invocation method is the way the invocation should be applied. Some members of the object require that they just be called, others might return a value. Sometimes we might need to set some kind of a property by either a value or by reference. Below is a list of possible methods:

.. list-table::
  :widths: 15 85
  :header-rows: 1

  * - Value	
    - Method
  * - 1	
    - Call a member of an object
  * - 2
    - Return a value
  * - 3	
    - (1+2) Call a member and return a value *
  * - 4	
    - Set a property
  * - 5	
    - (1+4) Set a property with a member call *
  * - 6	
    - (2+4) Set a property and return a value *
  * - 7	
    - (1+2+4) Set a property and return a value with a member call *
  * - 8	
    - Set a property by reference
  * - 9	
    - (1+8) Set a property by reference with a member call *
  * - 10	
    - (2+8) Set a property by reference and return a value *

.. note:: These methods with an * are the result of a combination of multiple methods using the four basic methods (1, 2, 4, and 8). For example 5 = 1 + 4, set a property with a member call. Other combinations not included in the table above are possible.

Variable Type
~~~~~~~~~~~~~

Unlike mSL, COM objects must have a data type for every value. For example, if we want to invoke a method that takes an integer value, we have to use the int data type. Below is a list of possible variable data types.

.. list-table::
  :widths: 10 30 20
  :header-rows: 1

  * - Type 
    - Description
    - Values
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
    - 
  * - bstr
    - null-terminated unicode character string value.
    - A string can contain from 0 to approximately 2 billion (2^31) Unicode characters.
  * - variant
    - can contain string, date, time, boolean, or numeric values. When used, a data type must follow it: for example: variant int 5
    - 
  * - dispatch
    - This data type indicates a pointer to an IDispatch interface on an OLE object (DBTYPE_IDISPATCH).
    - 
  * - unknown
    - This data type indicates a pointer to an IUnknown interface on an OLE object (DBTYPE_IUNKNOWN).
    - 
  * - error
    - This data type indicates a 32-bit error code (DBTYPE_ERROR)
    -

To make a variable by reference, postfix the data type with an asterisk and a variable name, for example: ``int* pIntOfBeer``.

Invoking members
----------------

To invoke a member of a COM object, we use the $com identifier using the following sytax:

.. code:: text

  ;member with no arguments
  $com(<hName>, <member>, <Invoke Method>)
  ;member with one argument
  $com(<hName>, <member>, <Invoke Method>, <type>, <value>)
  ;member with N amount of arguments
  $com(<hName>, <member>, <Invoke Method>, <type1>, <value1>, ..., <typeN>, <valueN>)

Invoking example
~~~~~~~~~~~~~~~~

For example, if we go back to the WScript.Shell object. Let's say we wanted to open calc using the exec method we saw earlier. First, let's revisit the MSDN page of the Exec Method.

We see the syntax is:

.. code:: text

  object.Exec(strCommand)

where object is the WshShell object and strCommand is the string value indicating the command line used to run the script. From this information we know the following things:

1. This is a member call - the invoke method is 1
2. The Exec method accepts 1 argument
3. The argument is a string - data type is bstr

Using the information above we can write our $com identifier to invoke that method:

.. code:: text

  ;Exec is the Object's member we are invoking
  ;1 = Call a member of an object
  ;bstr is the string data type of "calc"
  ;calc is what we are trying to execute
  $com(shellCOM, Exec, 1, bstr, calc)

$com will return either 1 if the invocation of the Object's member was successful, 0 otherwise. It is a good practice to check if the invocation was a success. Below is the complete script:

.. code:: text

  alias openCalc {
    .comopen shellCOM WScript.Shell
    if ($comerr) {
      echo $color(info) -aet * Error connection to the Windows Script Host
    }
    else {
      var %result = $com(shellCOM, Exec, 1, bstr, calc)
      if (!%result) {
        echo $color(info) -aet * Error executing the Exec method.
      }
      .comclose shellCOM 
    }
  }

Value of A Property / Enumerated Collection
-------------------------------------------

Retrieving a value from an enumerated collection or a property (like a variable) can be done using the $comval identifier following this syntax:

.. code:: text

  $comval(<hName>, <N>, <member>)

If the member returns an enumeration of values, you can traverse through them. When n = 0, it will return the total number of values in the enumeration.

Retrieving return values
------------------------

Recall from before, if we use invocation method value 2, we are indicating we want a return value. Well, to retrieve that value we can use the $com identifier in a different way:

.. code:: text

  var %value = $com(<hName>).result

Object dispatching
------------------

In many cases, you might need to invoke a member on an object that is nested inside another object (sometimes that object might be nested inside another object as well). In most cases the parent object will have a member method that when called will return an instance of the child object that we could use. This operation is called dispatching. In the process we dispatch the child object onto its own COM connection with its own handle name. This will allow us to conveniently access this object's members (and perhaps access more child objects).

.. Note:: When dispatching an object, the parent object will still remain open. If not used anymore, it's recommended that you close the connection right after the dispatching occurs.

Dispatching takes this general syntax:

.. code:: text

  ;open parent object
  comopen mainObj some.object
  ;dispatch the child's object onto his own com connection, named childObj
  var %result = $com(mainObj, memberName, 3, dispatch* childObj)
  ;close the parent object
  comclose mainObj
  ;do something with the child object
  var %result = $com(childObj, memberName, 1, ...)
  ;close the child object
  comclose childObj

Dispatching example - CPU info
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

One good example of using a dispatch is if you wanted to retrieve some information pertaining to your computer's processor. The processor information will be stored in an instance of the Win32_Processor class. Here is the tricky part: the Win32_Processor is found deep inside the windows API:

- Win32_Processor Class

  - Retrieved using the InstanceOf method

    - SWbemServices Class

      - Retrieved using the ConnectServer method

        - SWbemLocator Class

          - Retrieved using the following ProgID: WbemScripting.SWbemLocator

From the hierarchy tree above you can see we are going to have to dispatch twice to get to our final object we want.

Let's start writing our code: opening a COM connection the SWbemLocator object:

.. code:: text

  alias getProcInfo {
    .comopen SWbemLocator WbemScripting.SWbemLocator
    if ($comerr) echo $color(info) -aet * Error connection to WbemScripting.SWbemLocator
    else {
      ;rest of code here...
      .comopen SWbemLocator 
    }
  }

Now, from the SWbemLocator object, we need to use the ConnectServer method to dispatch and get a SWbemServices object.

.. code:: text

  alias getProcInfo {
    .comopen SWbemLocator WbemScripting.SWbemLocator
    if ($comerr) echo $color(info) -aet * Error connection to WbemScripting.SWbemLocator
    else {
      var %result = $com(SWbemLocator, ConnectServer, 3, dispatch* SWbemServices)
      .comclose SWbemLocator 
      if (!%result) echo $color(info) -aet * Error instantiating SWbemServices object.
      else {
        ;rest of code here ...
        .comclose SWbemServices
      }
    }
  }

At this point we have a COM connection called "SWbemServices" which is an object instance of the SWbemServices Class. Now all we have to do is use the InstanceOf method and dispatch to a new COM connection to get the Win32_Processor Object.

.. code:: text

  alias getProcInfo {
    .comopen SWbemLocator WbemScripting.SWbemLocator
    if ($comerr) echo $color(info) -aet * Error connection to WbemScripting.SWbemLocator
    else {
      var %result = $com(SWbemLocator, ConnectServer, 3, dispatch* SWbemServices)
      .comclose SWbemLocator 
      if (!%result) echo $color(info) -aet * Error instantiating SWbemServices object.
      else {
        var %result = $com(SWbemServices, InstancesOf, 3, string, Win32_Processor, dispatch* Win32_Processor)
        .comclose SWbemServices
        if (!%result) echo $color(info) -aet * Error retrieving an instance of the Win32_Processor class
        else {
          ;get some cool information about the CPU here
          .comclose Win32_Processor
        }
      }
    }
  }

Since we are now at the Win32_Porocessor object, all we have to do is retrieve the values. Recall from above that we can do that using the $comval identifier:

.. code:: text

  $comval(Win32_Processor, 1, <property>)

Where <property> can be any of the members of the Win32_Processor class that can be found here.

Let's get the "name" property, which usually holds a string of interesting things.

.. code:: text

  alias getProcInfo {
    .comopen SWbemLocator WbemScripting.SWbemLocator
    if ($comerr) echo $color(info) -aet * Error connection to WbemScripting.SWbemLocator
    else {
      var %result = $com(SWbemLocator, ConnectServer, 3, dispatch* SWbemServices)
      .comclose SWbemLocator 
      if (!%result) echo $color(info) -aet * Error instantiating SWbemServices object.
      else {
        var %result = $com(SWbemServices, InstancesOf, 3, string, Win32_Processor,dispatch* Win32_Processor)
        .comclose SWbemServices
        if (!%result) echo $color(info) -aet * Error retrieving an instance of the Win32_Processor class
        else {
          ;get the CPU's name
          echo -a * CPU Info: $comval(Win32_Processor, 1, Name)
          .comclose Win32_Processor
        }
      }
    }
  }

Which can be invoked by just typing:

.. code:: text

  /getProcInfo

Returns something like:

.. code:: text

  * CPU Info: Intel(R) Core(TM) i7 CPU 980x @ 3.33GHz

Other useful properties
-----------------------

The $com identifier has a few other useful properties:

.. list-table::
  :widths: 50 50
  :header-rows: 1

  * - Property
    - Description
  * - argerr
    - the argument that has caused the error
  * - error
    - error value, when applicable
  * - errortext
    - error description
  * - progid
    - object's name
  * - dispatch/unknown
    - return $true or $null if a pointer to this object exists

Limitations of COM
------------------

Currently mIRC/mSL's COM implantation has a few limitations that other languages may not encounter.

COM Passing
~~~~~~~~~~~

There is no way to pass the raw result or object from one COM instance to another. For results that mIRC can interpret, such as strings or integers, this isn't an issue(unless the result is excessively long) but for a returned object there is currently no way to pass it to another com.

COM Events
~~~~~~~~~~

mIRC/mSL does not support events that a COM instance may issue. The implantation works on a ask-receive programa, where mIRC requests the COM instance for data or to do something, and the instance is to return an immediate result.

Examples
--------

$file_get_contents(<website>)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ProgID: Msxml2.ServerXMLHTTP.3.0

Object's Members: XMLHTTPRequest Members

Example
^^^^^^^

.. code:: text

  /*
  ############################################################
  #              Get source of a file/website                #
  #                                                          #
  # Syntax:                                                  #
  #    var %source = $file_get_contents(<website>)           #
  # Example:                                                 #
  #    //echo -a $file_get_contents(http://www.example.com/) #
  ############################################################
  */
  Alias file_get_contents {
    if (!$1) {
      echo $color(info) -est * Too few parameters: $!file_get_contents
      halt
    }
    ;make sure it wasn't left open from last time
    if ($com(tcpCom)) .comclose $v1
    ;connect to the COM object
    .comopen tcpCom Msxml2.ServerXMLHTTP.3.0
    if ($comerr) echo $color(info) -est $!file_get_contents failed opening com
    else {
      ;initializes the object
      ;oXMLHttpRequest.open(bstrMethod, bstrUrl, varAsync, bstrUser, bstrPassword);
      noop $com(tcpCom, open, 2, bstr, GET, bstr, $1)
      ;sent to the server, get response
      noop $com(tcpCom, send, 1) $com(tcpCom, responseText, 2)
      if ($comerr) echo $color(info) -est $!file_get_contents failed opening connection
      else {
        ;get the result of the response, and return it
        var %r = $com(tcpCom).result
        .comclose tcpCom
        return %r
      }
    }
  }


Queue example
~~~~~~~~~~~~~

ProID: System.Collections.Queue

Object's Members: Queue Class Members

Example
^^^^^^^

.. code:: text

  /*
  #########################################################################
  #                           Queue                                       #
  #                                                                       #
  # Represents a first-in, first-out collection of elements               #
  #                                                                       #
  # Syntax:                                                               #
  #    /enqueue <queue_name> <value>                                      #
  #    /freeQueue <queue_name>                                            #
  #    var %value = $queue(<queue_name>).dequeue                          #
  #    var %value = $queue(<queue_name).peek                              #
  #    var %count = $queue(<queue_name).count                             #
  #                                                                       #
  # Example:                                                              #
  #  /enqueue example a                                                   #
  #  /enqueue example b                                                   #
  #  /enqueue example c                                                   #
  #  //while ($queue(example).count) { echo -a $queue(example).dequeue }  #
  #  /freequeue example                                                   #
  #########################################################################
  */
  alias enqueue {
    if ($0 < 2) {
      echo $color(info) -aet /enqueue: insufficient parameters
      halt
    }
    ;if there is no connection, open one
    if (!$com($1)) .comopen $1 System.Collections.Queue
    ;enqueu
    noop $com($1, enqueue, 1, bstr, $2-)
    if ($comerr) {
      echo $color(info) -aet /enqueue: queue error
      halt
    }
  }

  alias queue {
    ;check if its an ident, com exists, and the proprty is either dequeue/peek
    if (($isid) && ($istok(dequeue peek count, $prop, 32)) && ($com($1))) {
      ;call the peek() or dequeue() method, get the return value
      noop $com($1, $prop, 2)
      ;get the return value
      return $com($1).result
    }
  }

  alias freeQueue {
    ;close the com connection, if exists
    if ($com($1)) .comclose $1
  }


Sendkeys example
~~~~~~~~~~~~~~~~

ProID: WScript.Shell

Object's Members: WshShellObject Properties and Methods

Example
^^^^^^^

.. code:: text

  ;sends "Hello there!" to the editbox and presses enter
  alias sendkeys {
    ;open a com connection
    .comopen x WScript.Shell
    ;excute the sendkeys() method and close the com connection
    .comclose x $com(x, sendkeys, 1, bstr, Hello there!{ENTER})
  }

RAM information
~~~~~~~~~~~~~~~

ProID: WbemScripting.SWbemLocator

Object's Members: Win32_PhysicalMemory Class

Hierarchy Tree:

- Win32_PhysicalMemory Class

  - Retrieved using the InstanceOf method

    - SWbemServices Class

      - Retrieved using the ConnectServer method

        - SWbemLocator Class

Retrieved using the its ProgID: WbemScripting.SWbemLocator

Example
^^^^^^^

.. code:: text

  /*
  ####################################
  #              RAM Info            #
  #                                  #
  # Gets some interesting RAM info   #
  #                                  #
  # Syntax:                          #
  #    /getRamSpecs                  #
  ####################################
  */
  alias getRamSpecs {
    ;open COM connection
    .comopen SWbemLocator WbemScripting.SWbemLocator
    if ($comerr) echo $color(info) -aet * Error connection to WbemScripting.SWbemLocator
    else {
      ;dispatch and get an instance of the SWbemServices class
      var %result = $com(SWbemLocator, ConnectServer, 3, dispatch* SWbemServices)
      .comclose SWbemLocator 
      if (!%result) echo $color(info) -aet * Error instantiating SWbemServices object.
      else {
        ;dispatch and get an instance of the Win32_PhysicalMemory class
        var %result = $com(SWbemServices, InstancesOf, 3, string, Win32_PhysicalMemory,dispatch* Win32_PhysicalMemory)
        .comclose SWbemServices
        if (!%result) echo $color(info) -aet * Error retrieving an instance of the Win32_PhysicalMemory class
        else {
          ;0 will return the total number of elements (memory sticks in this case)
          var %memSticks = $comval(Win32_PhysicalMemory, 0, Caption)
          echo -a * RAM: %memSticks Sticks
          while (%memSticks) {
            ;Each of these members returns an enumeration containing
            ;the values for all the physical memory
            var %size = $bytes($comval(Win32_PhysicalMemory, $v1, Capacity)).suf
            var %location = $comval(Win32_PhysicalMemory, $v1, DeviceLocator)
            var %speed = $comval(Win32_PhysicalMemory, $v1, Speed)
            var %type = $getType($comval(Win32_PhysicalMemory, $v1, MemoryType))
            echo -a * Stick $v1 $+ : Size: %size Location: %location Speed: %speed Type: %type
            dec %memSticks
          }
          .comclose Win32_PhysicalMemory
        }
      }
    }
  }

  ;get the actual type from the numeric value
  alias -l getType {
    var %types = Unknown,Other,DRAM,Synchronous DRAM,Cache DRAM,EDO,EDRAM, $&
      VRAM,SRAM,RAM,ROM,Flash,EEPROM,FEPROM,EPROM,CDRAM,3DRAM,SDRAM,SGRAM, $&
      RDRAM,DDR,DDR-2
    return $gettok(%types, $calc($1 +1), 44) 
  }

Finding ProgIDs
---------------

The only thing you might still be wondering about is: how do I find other ProgIDs? The answer is, you need to do a little research. They are all over the place. Below are two great tools you can use to find some of the ProgIDs that nest on your computer:

OLE-COM Object Viewer - Microsoft tool for locating COM Objects
ActiveXHelper - A small utility that allows you to view info about ActiveX components

Point of interest
~~~~~~~~~~~~~~~~~

Win32 Classes - Part of the Windows Management Instrumentation Classes (WMI Classes, Enable you access to monitor and manage system hardware and features.

- Application Objects

  - Word.Application
  - Excel.Application
  - PowerPoint.Application
  - Access.Application
  - InternetExplorer.Application
  - FrontPage.Application*
  - Outlook.Application
  - Photoshop.Application

    - Photoshop.Application.7 (for Photoshop with Support plug-in installed)

- ShockwaveFlash.ShockwaveFlash

- iTunes.Application

- Scripting Objects

  - MSScriptControl.ScriptControl
  - WScript.Shell - Members
  - WScript.Network - Members
  - Shell.UIHelper - Members
  - VBScript.Regexp - Members
  - Scripting.Dictionary
  - Scripting.FileSystemObject

- XML Document Objects

  - MSXML.DOMDocument

    - Msxml2.DOMDocument
    - Msxml2.DOMDocument.3.0
    - Msxml2.DOMDocument.4.0
    - Msxml2.DOMDocument.6.0
    - Microsoft.XMLDOM

  - MSXML2.XMLHTTP

     - MSXML2.XMLHTTP.3.0

  - Microsoft.XMLHTTP
  - MSXML2.DSOControl

    - MSXML2.DSOControl.3.0

  - ADO Database Objects

    - ADODB.Connection - Members
    - ADODB.Stream - Members
    - ADODB.Command - Members
    - DODB.Recordset - Members

This is by no means an exhaustive list but simply a compilation of the most common objects.

\* Discontinued Product