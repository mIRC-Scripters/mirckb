$urlget
=======

$urlget sends a HEAD/GET/POST/PUT/PATCH/DELETE to an http server. Returns an ID. Can also be used to get infos about current running $urlget.

Synopsis
--------

.. code:: text

    $urlget(url,hgpuadfbtik,<target>,<alias>,[&headers],[&body])
    $urlget(N/ID,cr)
    $urlget(N/ID)[.prop]

Parameters
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Parameter
      - Description
    * - url
      - the url to access, must be prefixed with http:// or https:// (maximum url characters are <b>2000</b>)
    * - hgpuadfbrtic
      - switches to indicate how to proceed. See next table.
    * - target
      - the output: the filename if you used f, or a &binvar for b
    * - alias
      - the name of the alias that is called at the end, this alias is called as a command with one parameter passed to it: the ID
    * - headers
      - optional, a &binvar containing the headers to be sent, separated by $crlf
    * - body
      - optional, a &binvar containing the data to be sent when you are POSTing
    * - ID/N
      - the Nth urlget or the urlget referenced by the ID

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Switch
      - Description
    * - hgpuad
      - h for HEAD, g for GET, p for POST, u for PUT, a for PATCH, d for DELETE
    * - fb
      - f to output the answer (without the responses headers) to a file, b to ouput to a binvar
    * - r
      - resumes the processing, 
    * - t
      - uses .part file if necessary
    * - i
      - ignores SSL errors
    * - c
      - cancel the processing
    * - k
      - prevent redirection

Properties
----------

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Property
      - Description
    * - .url
      - returns the url used
    * - .redirect
      - returns the value of the location header if available
    * - .method
      - returns the method used (GET/POST)
    * - .type
      - returns the type of output, (binvar/file)
    * - .target
      - returns the value of target (name of the binvar or filename)
    * - .alias
      - returns the name of the alias used
    * - .id
      - returns the ID.
    * - .state
      - returns the state (ok, connect, download, fail)
    * - .size
      - returns the value of the content-lenght header
    * - .resume
      - returns 0 or 1 depending on if you are resumed/paused?
    * - .rcvd
      - returns the number of bytes received after the header, could be different from .size after a failed download.
    * - .time
      - returns the time taken to complete the processing, in millisecond
    * - .reply
      - returns the response headers

Example
-------

Usage: /download https://www.mirc.com/versions.txt

.. code:: text

    alias download {
      if (!$1) { return }
    
      if ($1 isnum) { 
        if ($urlget($1).state == fail) { echo 4 -at Error: Connection issues! | return }
    
        .run notepad.exe $qt($urlget($1).target)
      }
      else {
        var %file = source.txt
    
        write -c $qt(%file)
    
        return $urlget($1,gfi,%file,download)
      }
    }

----------

Type /urlget.test

.. code:: text

    ; > POST / HTTP/1.1
    ; > Accept: */*
    ; > Test: Header
    ; > Accept-Encoding: gzip, deflate
    ; > User-Agent: mIRC
    ; > Host: localhost
    ; > Content-Length: 19
    ; > Connection: Keep-Alive
    ; > Cache-Control: no-cache
    ; > foo1=bar1&foo2=bar2
    ; < HTTP/1.1 200 OK
    ; < Connection: close
    ; < Content-Length: 5
    ; < hello
    ; url      http://localhost/
    ; redirect http://localhost/
    ; method   post
    ; type     binvar
    ; target   &target
    ; alias    urlget.callback
    ; id       1027
    ; state    ok
    ; size     5
    ; resume   0
    ; rcvd     5
    ; time     125
    ; reply    HTTP/1.1 200 OKConnection: closeContent-Length: 5
    ; response hello
     
     
     
    alias urlget.test {
      urlget.listen 
      var %url = $iif($1,$1,http://localhost/)
      bset -t &header 1 Test: Header
      bset -t &body 1 foo1=bar1&foo2=bar2
     
      var %id = $urlget(%url,pb,&target,urlget.callback,&header,&body)
    }
     
    alias urlget.callback {
      var %id = $1
     
      echo -agi9 url      $urlget(%id).url
      echo -agi9 redirect $urlget(%id).redirect
      echo -agi9 method   $urlget(%id).method
      echo -agi9 type     $urlget(%id).type
      echo -agi9 target   $urlget(%id).target
      echo -agi9 alias    $urlget(%id).alias
      echo -agi9 id       $urlget(%id).id
      echo -agi9 state    $urlget(%id).state
      echo -agi9 size     $urlget(%id).size
      echo -agi9 resume   $urlget(%id).resume
      echo -agi9 rcvd     $urlget(%id).rcvd
      echo -agi9 time     $urlget(%id).time
      echo -agi9 reply    $urlget(%id).reply
     
      if ($urlget(%id).type == binvar) {
        echo -agi9 response $bvar($urlget(%id).target,1-3000).text
      }
    }
     
    alias urlget.listen {
      if (!$sock(urlget.listen)) socklisten -d 127.0.0.1 urlget.listen 80
    }
     
    on *:socklisten:urlget.listen:{
      var %sockname = urlget.client. $+ $ticks
      if ($sock(%sockname)) return
     
      sockaccept %sockname
    }
     
    on *:sockread:urlget.client.*:{
      var %header
     
      if (!$sock($sockname).mark) {
        sockread %header
        while (%header != $null) {
          echo 3 -ag > %header
          if ($regex(%header,Content-Length: (\d+))) {
            hadd -m $sockname content-length $regml(1)
          }
          sockread %header
        }
        if ($sockbr) sockmark $sockname $true
      }
     
      if ($sock($sockname).mark) && ($sock($sockname).rq) {
        sockread &read
     
        while ($sockbr) {
          hinc $sockname content-read $sockbr
          echo 6 -agi2 > $bvar(&read,1-3000).text
     
          sockread &read
        }
      }
     
      if ($hget($sockname,content-length) == 0) || ($v1 == $hget($sockname,content-read)) {
        socket.respond $sockname hello
        hfree -w $sockname
      }
    }
     
    alias -l sockwrite {
      echo 12 -ag < $3-
      sockwrite $1-
    }
     
    alias -l socket.respond {
      var %sockname = $$1, %data = $2-
      sockwrite -n %sockname HTTP/1.1 200 OK
      sockwrite -n %sockname Connection: close
      sockwrite -n %sockname Content-Length: $len(%data)
      sockwrite -n %sockname $+($crlf,%data)
    }
    

cancelling and resuming

.. code:: text

    ;cancel the first $urlget request currently running
    $urlget(1,c)
    
    ;resume the request identified by the id <id>
    $urlget(<id>,r)

Compatibility
-------------

.. compatibility:: 7.56

See also
--------

.. hlist::
    :columns: 4

    * :doc:`/url </commands/url>`
    * :doc:`$url </identifiers/url>`

