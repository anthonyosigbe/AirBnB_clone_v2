#!/usr/bin/python3
# Fabric file for removing obsolete archives.
import os
from fabric.api import *

env.hosts = ["54.208.91.86", "54.173.66.23"]


def do_clean(number=0):
    """Remove outdated archives.
    Arguments:
    number (int): The number of archives to retain.
    If the number is 0 or 1, only the most recent archive is kept.
    If the number is 2, both the most recent and second-most
    recent archives are kept, and so on.
    """
    number = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]
