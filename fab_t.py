#!/usr/bin/python3

from fabric.api import *
from fabric import *
def do_send(path):
    c = connection("100.27.10.204@ubuntu")

    c.put(path, "~/sends")

