# pysctp
SCTP stack for Python3

PySCTP - SCTP bindings for Python3
---------------------------------

Elvis Pfützenreuter 
Instituto Nokia de Tecnologia (http://www.indt.org.br)
epx __AT__ epx.com.br

Philippe Langlois
P1 Security (http://www.p1sec.com)
phil __AT__ p1sec.com

Guiyang Wu
Nokia Qingdao (http://www.nokia.com)

======================================================================
INSTALL for Ubuntu (version >= 14.04)

1) Shell: sudo apt-get install libsctp-dev libsctp1 lksctp-tools
2) download pysctp package and unzip it
3) Shell: sudo python3 setup.py install
4) Python3> import sctp

======================================================================
INSTALL

sudo python3 setup.py install

* to see what this is going to install without actually doing it:
python3 setup.py install --dry-run

* to just build and not install:
python3 setup.py build

======================================================================
DEPENDENCIES:

You can use to automatically install dependencies for Debian/Ubuntu:
make installdeps

For Ubuntu (version >14.04):
You can run the following commands to install the deps:
sudo apt-get install libsctp-dev libsctp1 lksctp-tools

For Mac OSX (Montain lion OSX 10.8):
https://nplab.fh-muenster.de/groups/wiki/wiki/f366c/SCTP_on_Mountain_Lion.html

Mac OSX SCTP Network Kernel Extension (NKE) available at:
http://sctp.fh-muenster.de/sctp-nke.html

======================================================================
INTRODUCTION

PySCTP gives access to the SCTP transport protocol from Python3 language.
It extends the traditional socket interface, allowing
SCTP sockets to be used in most situations where a TCP or UDP socket
would work, while preserving the unique characteristics of the protocol.

For more information about SCTP, go to http://www.sctp.org or RFC 4960.
For discussion, sources, bugs, go to http://github.com/philpraxis/pysctp

In a nutshell, PySCTP can be used as follows:

---------

import socket
import sctp

sk = sctpsocket_tcp(socket.AF_INET)
sk.connect("10.0.1.1")

... most socket operations work for SCTP too ...

sk.close()

---------

The autotest programs (test.py and test_server.py) are actually a good
example of pysctp usage.

The BSD/Sockets SCTP extensions are defined by an IETF draft
(draft-ietf-tsvwg-sctpsocket-10.txt) and PySCTP tries to map those
extensions very closely. So, to really take the most advantage of
SCTP and PySCTP, you must understand how the API works. You can
find advice about it in the the draft itself (not incredibly easy
to understand though), as well the 3rd edition of Unix Network 
Programming.

WARNING: the API of this module is not stable yet. We expect not to
change it too much, but do not base any critical work on it yet :)


======================================================================
DESCRIPTION

1) The "sctp" module

The "sctp" module is the Python3 side of the bindings. The docstrings
of every class and method can give good advice of functions, but the
highlights are:

* sctpsocket is the root class for SCTP sockets, that ought not be used
  directly by the users. It does *not* inherit directly from Python3
  standard socket; instead it *contains* a socket. That design was
  followed mostly because UDP-style sockets can be "peeled off" and 
  return TCP-style sockets. 

  sctpsocket delegates unknown methods to the socket. This ensures that
  methods like close(), bind(), read(), select() etc. will work as expected.
  If the real socket is really needed, it can be obtained with
  sctpsocket.sock().

* As said, "Normal" socket calls like open(), bind(), close() etc. 
  can be used on SCTP sockets because they are delegated to the
  Python3 socket. 

* Users will normally use the sctpsocket_tcp (TCP style) and sctpsocket_udp
  (UDP style) classes. Some calls that are implemented in sctpsocket but 
  do not make sense in a particular style are rendered invalid in each
  class (e.g. peeloff() in TCP-style sockets).

2) The "_sctp" module

This is the C side of the bindings, that provides the "glue" between
Python3 and the C API. The regular PySCTP user should not need to get 
into this, but power users and developers may be interested in it. 

The interface between Python3 and C is designed to be as simple as
possible. In particular, no object is created in C side, just 
simple types (strings, integers, lists, tuples and dictionaries).

The translation to/from complex objects is done entirely in Python.
It avoids that _sctp depends on sctp.

NOTE: it all has been tested agains lksctp-utils 1.0.1 and kernel
2.6.10, that come with Ubuntu Hoary. Some newer calls like connectx()
depend of testing on a newer environment to be implemented.


======================================================================
License

This module is licensed under the LGPL license.

======================================================================
Credits

Elvis Pfützenreuter <elvis.pfutzenreuter __AT__ indt.org.br>
Philippe Langlois <phil __AT__ p1sec.com>
Casimiro Daniel NPRI <CasimiroD  __AT__ npt.nuwc.navy.mil> - patch for new SCTP_* constants
Guiyang Wu <Nokia> - port to Python3
