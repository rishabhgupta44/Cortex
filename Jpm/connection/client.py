# ---------------------------------------------------------------------------
# Copyright (c) 2019 Rishabh Gupta
# This file is part of the Rule-Based Cognitive Architecture project.
# Distributed under the MIT License. See the LICENSE file for details.
# ---------------------------------------------------------------------------

import socket

s=socket.socket('192.068.0.101',socket.SOCK_STREAM)
host = str(input("Enter: "))
s.connect((host,9909))
msg = s.recv(1024)
print(msg)