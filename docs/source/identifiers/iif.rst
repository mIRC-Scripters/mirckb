$iif
====

$iif returns a conditional value depending on whether a conditional statement resolves to $true or $false.

Synopsis
--------

.. code:: text

    $iif(C,T [,F] )

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - C
      - A conditional statement that determines whether this identifier returns the $true or $false conditional.
    * - T
      - The string returned and/or identifier evaluated/executed if the C statement is $true
    * - F
      - Optional string returned and/or identifier evaluated/executed if the C statement is $false

.. note:: If F parameter is not used, $iif returns $null if the C statement is $false

.. note:: If C evaluates to $false or $null or 0 (including 000 or 0.00), it is $false. $true or non-zero or text strings are $true

.. note:: If both T and F conditions contain identifier calls, the T condition's identifier/alias is called/evaluated only if C evaluates as $true, and the F condition's alias is called only if C evaluates as $false

Properties
----------

None

Example
-------

.. code:: text

    //echo -a My IP address $ip is an $iif( $calc($right($ip,1) % 2),odd,even) number

.. code:: text

    //echo -a $iif(0,$custom1(true1),$custom2(false2)) / $v1 $v2
    
    Calls the custom2 identifier and returns any string returned by it.
    $v1 is filled with the 1st term of the C condition. Because the conditional was $false, the $custom1 alias in the T branch is not called.
    
    //echo -a $iif(2 > 1,$custom1(true1),$custom2(false2)) / $v1 $v2
    
    Calls the custom1 identifier and returns any string returned by it.
    $v1 is filled with 2 (the 1st term of the C condition) and $v2 is filled with 1 (the 2nd term of C).
    
    //echo -a today: $iif($asctime($ctime,ddd) isin MonTueWedThuFri,Weekday,Weekend)
    //echo -a today: $iif($asctime($ctime,ddd) isin MonTueWedThuFri,Weekday)
      1st of the pair returns either Weekday or Weekend
      2nd of the pair returns either Weekday or $null because of the missing F parameter.
    
      $iif conditionals can be nested:
    //echo -a Classes on the $iif($asctime($ctime,ddd) isin SatSun,Sat-Sun, $iif(T* iswm $asctime($ctime,ddd),Tue-Thur,Mon-Wed-Fri)) Schedule meet today

.. note:: see the :doc:`injection </beginner/injection>` page for explanation/examples of how malformed $iif syntax can trick users into executing code from the editbox. This next example causes you to perform the /QUIT command if you remove the 'echo -a' from it:

.. code:: text

    //echo -a $iif(($regsubex(dim[int:x];for[x=0:20:3]x*TAN-1<<DEG[]<<SQ[],/[^A1NT]/g,)) echo -a $base($v1, 34, 35) I accidentally math, I math right! )

.. note:: $iif is a relatively slow identifier, and in some situations it can benchmark faster to replace it with a /set and an /if command pair.

.. code:: text

    //var %a $iif($rand(0,1),True,False)
    vs
    var %a False
    if ($rand(0,1)) var %a True

Compatibility
-------------

.. compatibility:: 5.4

See also
--------

.. hlist::
    :columns: 4

    * :doc:`/if </commands/if>`
    * :doc:`$true </identifiers/true>`
    * :doc:`$false </identifiers/false>`
    * :doc:`injection </beginner/injection>`

