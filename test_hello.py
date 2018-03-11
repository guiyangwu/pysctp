#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 
# Copyright (C) 2018 Guiyang WU - all rights reserved
#
# This library is free software; you can redistribute it and/or modify it
# under the terms of the GNU Lesser General Public License as published by the
# Free Software Foundation; either version 2.1 of the License, or (at your
# option) any later version.
#
# This library is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this library; If not, see <http://www.gnu.org/licenses/>.

'''
This is simple test with sctpsocket() on Python3. The test procedure is:
    1) sctp_test -H 127.0.0.1 -P 10000 -l
    2) use python3 to run this script
    3) verify if sctp_test receives "hello"
'''

import sctp

server_addr = ("127.0.0.1", 10000)
print("SCTP server:", server_addr) 

sk = sctp.sctpsocket(sctp.socket.AF_INET, sctp.socket.SOCK_STREAM, None)
sk.initparams.max_instreams = 3
sk.initparams.num_ostreams = 3
sk.events.clear()
sk.events.data_io = 1

sk.connect(server_addr)

msg = "hello"
sk.sctp_send(msg)
print("Sent:", msg)
#fromaddr, flags, msg, notif = sk.sctp_recv(1024)
#print("Received:", msg)

sk.close()
