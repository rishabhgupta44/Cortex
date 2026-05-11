# ---------------------------------------------------------------------------
# Copyright (c) 2019 Rishabh Gupta
# This file is part of the Rule-Based Cognitive Architecture project.
# Distributed under the MIT License. See the LICENSE file for details.
# ---------------------------------------------------------------------------

import socket
#this is a server module

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = socket.gethostname()
s.bind((host,9998))
s.listen(5)
print(f"connection to {host}")
clt,adr = s.accept()
print(f'connected to \x1b[0m {adr}')
clt.send(bytes("Test","utf-8"))
