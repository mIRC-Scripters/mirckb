$sslcertsha256
==============

$sslcertsha256 returns the sha256 fingerprint of the client certificate in the currently loaded private key file

Synopsis
--------

.. code:: text

    $sslcertsha256

Parameters
----------

None

Properties
----------

None

Example
-------

.. code:: text

    //echo -a $sslcertsha256

Creating A certificate
----------------------

I'm stashing this here because I'm not sure where else it would belong here

This is an explanation of using both kinds of SASL commonly used by IRC networks. I've tested this at Libera.Chat and SwiftIRC and it works fine. It also works in Win7 and Win10, though if you're using XP then your mileage may vary.

SASL PLAIN is much easier to setup, but doesn't have as high level of security as from using a certificate. However, SASL External won't work unless you're also using an SSL connection at an SSL port, as indicated by mIRC having the port be preceded by '+', as in +6697 not 6667.

The advantage of using SASL, instead of sending the password as a /notice to NickServ, is that NickServ identifies you during CONNECT, which means you should be identified before you auto-join any channels which don't allow any unidentified nicks inside. Which means there's no need for adding delays before entering channels because of that reason.

There's 2 different kinds of SASL: PLAIN and External (CertFP.)

If you're worried about your password being intercepted by your ISP or someone else between you and the IRC server, that's not what this is for, and you can solve that problem by using the IRC network's SSL port, commonly at ports like +6697 +7000 +7001 +7070. For all practical purposes, it's the same as sending your password to NickServ. It is still sent from mIRC without being encrypted other than the SSL connection you're using, with the only difference being that it's sent to the server immediately after the ON CONNECT event, instead of being messaged to NickServ. Later I'll show how you can see the unencrypted password being sent in a @debug window.

If you're intimidated by the complexity of certificates, don't worry since mIRC makes it pretty simple to set up your certificate. Or, you can choose to create your own certificate yourself if you've installed OpenSSL.

There are a couple of limitation in how mIRC handles certificates, which might change your decision of how to proceed.

a. mIRC only allows you to have 1 certificate loaded at a time, which forces you to use the same certificate at all networks that you're using SASL External. The fingerprint of your certificate is virtually guaranteed to be unique, so using the same certificate at 2 servers makes it possible to link both of your server presences as coming from the same copy of mIRC, even if you're using different nicks and have changed the identd userid.

b. Unless there's a setting I've not found, the only key length of RSA key which mIRC will create is 2048-bit. Using OpenSSL to create the certificate allows you to create the 4096-bit RSA that Libera.Chat suggests, though they do accept the 2048-bit that mIRC creates.

--

The simpler version of SASL is PLAIN, and can be quickly setup with these steps:

https://libera.chat/guides/mirc

This type of SASL works by simply sending your NickServ password to the server as you're connecting, without waiting for NickServ to ask for it. If you're not connecting using an SSL port, then this sends your password across the internet without being encrypted, which could include being visible to your ISP or someone within your LAN. However it's better than sending your password to NickServ because it gets you authenticated before trying to autojoin channels who ban unidentified nicks.

To use SASL PLAIN, simply edit the serverlist entry for that server, change the login method to "SASL (/CAP)", and put your password in the password box BELOW that dropdown. Click 'OK' and you're done.

Here's a couple of tips for entering your password there:

1. The password box only shows the bullet symbols while typing, so it's easy to make a mistake. You can type the password into an editbox or into NOTEPAD, then cut-and-paste it into this password box, so you know you got it right.

2. Instead of putting only the password in the box, you should instead input string1:string2 where string1 is the accountname under which you registered your NickServ account, and string2 is the password. This allows SASL to authenticate you even if you happen to join as a Guest12345 nick.

If the server tells mIRC that authentication failed, mIRC checks to see if the password looked like string1:string2, and if string1 isn't the nick you're connecting with, it will try again using your $me current nick in place of string1. But that doesn't help if you're using an _away nick or something else that isn't registered.

You can see how SASL PLAIN works if you've used the /debug command to see the raw server messages between you and the server, and then connect to the server to see the connection handshake. A simplified version of the way this SASL PLAIN handshake is supposed to work is:

*1. mIRC sends to server: AUTHENTICATE PLAIN
*2. the server replies: AUTHENTICATE +
*3. mIRC replies: AUTHENTICATE bWFyb29uAG1hcm9vbgBuaWNrc2VydnBhc3N3b3Jk

The mime string will be different for you, and is not encrypted, it's simply encoding the string as mime because it cannot be sent as plaintext due to containing a couple of 0x00 bytes. You should NOT paste that base64 string into any channel, because it is simple for anyone to extract your password from it, by pasting the string to replace the mime into the command below.

.. code:: text

    //bset -tc &v 1 bWFyb29uAG1hcm9vbgBuaWNrc2VydnBhc3N3b3Jk | noop $decode(&v,bm) | breplace &v 0 32 | echo -a $bvar(&v,1-).text

It needed to replace 0x00's with spaces so the entire string could be visible. If you entered your password as string1:string2 the decoding of that mime would be:

string1:string1:string2

If you didn't have a colon in your password, mIRC replaces both of those string1's with the current nick.

--

The other kind of SASL is sometimes called either "CertFP" or "SASL External". Instead of sending the plaintext password when connecting, there's a handshake between mIRC and the server. The "EXTERNAL" means that the authentication takes place within external communication, so you can't see that handshake in the @debug window.

SASL External doesn't transmit any password when you're connecting. It instead authenticates you by sending your public certificate to the server, and then mIRC proves to the server that it has the private key which was used to create that public certificate.

There's several ways to make the certificate.

While the simplest way is to let mIRC create the certificate for you, some users may want the extra strength and flexibility from using OpenSSL to make their own certificate. For example, mIRC creates a 2048-bit RSA certificate with no apparent way to change this. However, Libera.Chat is suggesting users create a 4096-bit certificate, which is something that OpenSSL can do easily. Also, when creating a certificate in OpenSSL, there are 7 different types of information about the certificate owner (you) which you can use when creating the certificate, while mIRC's input form only lists 4 of the 7. mIRC forces you to put something in all 4 of those items, while OpenSSL only requires that at least 1 of them be non-blank.

Note that the information you input when creating the certificate is contained inside the public certificate, so mIRC sends it to each server once you've setup a private key.

To the best of my knowledge, 2048-bit RSA is 'good enough', so if you're willing to have a 2048-bit RSA key, then there's only a few quick steps and the certificate is created. To allow mIRC to create your certificate, skip down to Method#2.

Method#1 - creating the CertFP certificate using OpenSSL
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This is a supplement to the Libera.Chat guide for setting up SASL External using an RSA certificate: https://libera.chat/guides/certfp

If you don't want to, or can't, install a full/large OpenSSL, there are pre-compiled binaries from sources that should be 'trustworthy-ish', and are relatively small.

https://wiki.openssl.org/index.php/Binaries

If you already have a version of OpenSSL in the 1.1.* series, that should probably be good enough for making this certificate, though there is a 3.0 version of OpenSSL version available. Other than a slightly different method of choosing primes, the certificates in these OpenSSL versions are created the same way.

OpenSSL is a command-line program which can be a little hard to get used to, but these instructions will walk you through it, and you can use commands that you can paste into an mIRC editbox. If worried about the chance of errors causing unwanted messages sent to the server or even into a #channel window, you can open a new status window to an unconnected network and do your typing/pasting there:

.. code:: text

    /server -n

Some of these commands keep the console window open so you can see error messages. So, when done with these windows, you can click them closed.

First thing we'll do is create a .pem file that contains BOTH your public certificate and the private key. While you can share the certificate with anyone, you MUST NOT let anyone have the private key, because this would be similar to revealing your NickServ password, allowing anyone to login to your NickServ account as long as NickServ thinks that certificate belongs to you.

Each of the following commands has a variable named %prog which contains "openssl.exe", which will work if that program is in a folder mentioned in the PATH variable of your Windows environment. If OpenSSL is not in there, you can simply edit that string in each of these commands, to include the whole path, like "c:\Program Files\OpenSSL\bin\openssl.exe"

If you have OpenSSL installed, but aren't sure exactly where, this next command shows you the name of all folders on your entire C: drive who have 'openssl' in the foldername. THIS WILL TAKE A LONG TIME. OpenSSL.exe is usually in a \bin\ subfolder beneath the folder you installed the program into.

.. code:: text

    //noop $finddir(c:\,*openssl*,0,echo -s $1-)

These commands use libera.pem as the name for the certificate being created. You can use a different name, by either renaming libera.pem after you created it, or editing the name everywhere it appears in these commands.

Since OpenSSL allows these commands to overwrite an existing file, be careful about repeating these commands later, or you risk overwriting the only copy of the certificate, forcing you to give NickServ the new fingerprint again. You may wish to keep a backup copy of your certificate.pem file

(#A)

The OpenSSL command will create/overwrite the certificate/private-key file using the name libera.pem located in the same folder where your mirc.ini is located. This 1st command pasted into any editbox informs if the filename already exists in that folder:

.. code:: text

    //echo -ag $isfile(libera.pem)

If you change the name, be sure to leave the .pem alone.

OpenSSL will prompt you to enter 7 kinds of personal information. It doesn't matter what you input, if anything. Some of these have a default string that's used if you just press <enter>, but you can force each item to be blank by just inputting a '.' period character.

None of the information is validated for truthfulness, though it can be limited as to length. The country code doesn't check to see if it's a real country, but it does require it be either blank or be 2 characters. The 'common name' and 'email address' fields are probably limited to be no longer than 64.

Just to be on the safe side, it might be a good idea to put something in one of these fields to indicate that this key is only for use with IRC, and you may want to input your nick as the 'common name'.

Create your certificate by pasting this command into a Status Window editbox:

.. code:: text

    //var %prog "openssl.exe" | /run cmd /k %prog req -x509 -new -newkey rsa:4096 -sha256 -days 1096 -nodes -out libera.pem -keyout libera.pem

There's 2 kinds of error messages you might have seen, but they're either harmless or easily avoided.

"Error, no objects specified in config file"

If you use '.' to force all fields to be blank, you'll get this error because OpenSSL wants there to be at least 1 of the 7 inputs to contain something. Simply repeat the command to create a brand new certificate.

"Can't load ./.rnd into RNG"

This is mostly harmless. Whenever creating a certificate, OpenSSL needs to have randomness to help make sure the primes are not guessable. Unless you've configured OpenSSL differently, it looks to open this filename in the output folder each time you make a certificate, in order to grab randomness from prior keys you generated. Since the .rnd filename didn't already exist in your AdiIRC folder, that's what this message means, even though it did create that filename. If you repeat the above command to make a new certificate, it overwrites the existing certificate and makes a new one, and this time the error message won't be there, and it grabs the old entropy from .rnd to combine with the new entropy it has.

The above command syntax is the same as suggested by Libera.Chat, and you may have trouble if you change some of the options.

	 -days 1096

This sets the expiration date to be in 3 years. As that future time approaches, you can do this all over again, at which point certificates might also be using longer keys.

	rsa:4096 -sha256

This sets RSA to use a 4096-bit modulus. The larger you use, the longer it takes to generate the certificate, and it takes slightly longer during the SASL handshake. Using larger keys might also limit which servers will accept such a key length, and mIRC only supports using 1 certificate to be shared by all servers where you're using SASL External.

The -sha256 defines which hash is used when creating the authentication signature. This is NOT the same string as the certificate's fingerprint that you're supposed to feed to NickServ later.

(#B)

This next part is optional, but it's good to take a look at an overview of your certificate, to make sure it looks like you want it to. It will also show the fingerprint, but we can avoid the need to manually type/paste that string to NickServ. The file being opened in notepad contains ONLY information about your public certificate, so this libera.txt is safe to send to someone, unlike libera.pem which also contains your private key.

.. code:: text

    //var %prog "openssl.exe" | /run cmd /k %prog x509 -in libera.pem -fingerprint -sha512 -text -out libera.txt & notepad libera.txt

This should create libera.txt as a summary file of your certificate, then load it into notepad for you. The 1st line is the sha512 fingerprint, which is simply the sha512 hash of the entire certificate that's underneath the mime encoding you see there. See that near the top, just below the fingerprint, are lines labeled "Issuer:" and "Subject:". These have the identifier information you entered while creating the certificate. If there's something there that you didn't put there, it's one of the defaults resulting from just pressing <enter> at a prompt, instead of the '.' character. If you want, you can go back and re-do the certificate until you get it right.

The reason both "Issuer:" and "Subject:" lines of information are identical is because this is a 'self signed certificate', which means it was signed by whoever has the matching private key (you), instead of being signed by a 'Certificate Authority' who has verified the identity of the person claiming to control this certificate.

The "Not Before:" shows that you just now created the certificate, and the "Not After" shows when it expires.

I won't describe any of the math involved in using RSA, other than to mention the hex bytes in the section labeled "Signature Algorithm:". This is a signature that 'should' only be possible to create by someone who has the private key belonging to the CA (you).

(#C) Now you're ready to make mIRC use your certificate. Go into mIRC options and find the topic for Connect/Options and click on the "SSL" button.

(#D) Click on the button "private key file" and browse to choose the certificate you just now created. If you were already using a certificate, the filename containing the private key is already showing on that button, so the 1st click just makes it blank, and you need to click a 2nd time to browse for finding it.

.. note:: Use the file's TIMESTAMP to verify that this is the correct certificate that you've just now created in the last few minutes.

Note that if you let mIRC create the certificate instead, the default filename the 1st time you create the certificate is client.pem, but each time you create a new certificate, mIRC creates a new filename by adding a number like client1.pem - while OpenSSL keeps overwriting the same filename without warning.

(#E)

<b>Welcome people who let mIRC create the 2048-bit RSA key, here is where they continue with installing their certificate.</b>

Now "OK" your way out of the options menu, and mIRC is now using the certificate. You can confirm that you now have a certificate loaded, by using this command:

.. code:: text

    //echo -a fingerprint: $sslcertsha256

If you go back into the menu and browse for a different filename.pem, the fingerprint returned by this identifier immediately changes.

This is the fingerprint that SwiftIRC wants, but isn't the sha512 fingerprint that Libera.Chat needs. However it does let you confirm that you are using a certificate, since the identifier returns a blank if it's not currently using a certificate.

(#F) Now you need to tell NickServ your certificate's fingerprint. It's not enough that you've loaded the certificate into mIRC, it needs to be the certificate broadcast to the IRC network at the time you connected to the server, even if you're not setup to use SASL External yet.

It's possible to avoid this reconnect, but it would require you to message the sha512 fingerprint to NickServ while logged in, and without all those extra colons.

So you need to disconnect from that IRC network and reconnect while mIRC's options menu shows you are using the certificate's private key. You do NOT need to restart mIRC.

As you reconnect, you'll need to login the same way you've done previously, or else manually message your password to NickServ, because SASL External can't work until the network can trust that the certificate being used to login actually belongs to the owner of your NickServ account.

If you perform "//whois $me" while being identified to NickServ, the reply tells you that you've connected to the network while using a certificate, but that's not good enough to authenticate you for the future visits.

If you do not see your certificate listed in the /whois reply, make sure you connected using an SSL port where the number is preceded by the + sign. If not, reconnect to the network and try again.

(#G) Now that you've reconnected and have identified to NickServ, send this command to NickServ telling it to add the fingerprint of whatever certificate you used to connect to the server:

	<pre>/msg NickServ CERT ADD</pre>

If this fails, then NickServ doesn't see you currently using any certificate.

The only other fail should be if NickServ tells you that this fingerprint is already attached to a different account. So either you did it, someone else stole your certificate and did it, or you're about to become famous for being the 1st person to create an sha512 collision between 2 different files.

If successful, you'll receive a reply showing the fingerprint added. At Libera.Chat it's the 128 digits of the certificate's sha512 fingerprint. At SwiftIRC, it's currently the shorter 64 digits of the sha256 fingerprint, which is the same value seen from the $sslcertsha256 identifier. There may be some networks still using sha1 or even md5 fingerprints. Don't be confused by the certificate info in the Status Window's system menu, which is all about the SERVER's certificate, not yours.

(#H) Now you're almost done, you just need to configure mIRC to use SASL External the next times you connect to that server. Simply go to the serverlist and edit the serverlist entry you used when connecting to this network. At the dropdown menu for "Login Method", choose "SASL External (CAP)" and then click OK. Even though there's a password box below it, leave that alone, because that's used only for the "SASL (CAP)" aka "SASL PLAIN" method.

If you have several servers in that serverlist 'group', and some of them don't use an SSL port, then this authentication fails if you happen to connect using a non-SSL port.

(#I) Now reconnect to the server, and somewhere among the Status Window messages from the server while connecting should be a message similar to:

	SASL authentication successful

And you're done! Except to remember to guard the .PEM file the same way you guard your NickServ password. The private key .pem file does not contain any NickServ password, but it can be used to login your NickServ account at that server, and if they can login as you, they could alter the settings inside the NickServ account

METHOD#2 Creating the SASL EXTERNAL certificate inside mIRC
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A) Go to mIRC options and find the item for connect/options/SSL

B) Click on the button "create new certificate"

C) That brings up a dialog prompting you to input a few pieces of information. It doesn't matter what you put in it, but you may want to put your nick in one of the boxes, and maybe something to indicate that this certificate is used only for IRC. OpenSSL's interface has 3 additional pieces of information to enter when creating a certificate, and requires only 1 of the 7 items be non-blank. However, mIRC offers only 4 of the 7 items, and forces you to put something in all of them. You don't need to put real information there, it doesn't even check whether you've put the 2 letter code for a real country.

D) When you click OK, this creates a new certificate in the same folder as mirc.ini, and the button labeled "Private key file" changes to contain the path\filename of the certificate you just now created. If you formerly were using a different certificate, it's still there, under the old filename, and you can always click on 'browse' to use the old one. Continue clicking your way out of OPTIONS to ensure mIRC remembers that you're using this certificate.

E) Now go up to Step#E in the OpenSSL Method#1 instructions and continue from there.
Compatibility
-------------

.. compatibility:: 7.48

See also
--------

.. hlist::
    :columns: 4

    * :doc:`$sslcertsha1 </identifiers/sslcertsha1>`
    * :doc:`$ssl </identifiers/ssl>`
    * :doc:`$sslready </identifiers/sslready>`
    * :doc:`$sslversion </identifiers/sslversion>`
    * :doc:`$ssldll </identifiers/ssldll>`
    * :doc:`$ssllibdll </identifiers/ssllibdll>`
    * :doc:`/server </commands/server>`
