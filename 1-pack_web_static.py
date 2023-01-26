#!/usr/bin/python3
"""generates a .tgz archive from the contents of the web_static"""
from fabric.api import local
import time

def do_pack():
    """generates a .tgz archive from the contents of the web_static"""
    try:
        local("mkdir -p versions")
        local("tar -cvzf versions/web_static_{}.tgz web_static/".
                format(time.strftime("%Y%m%d%H%M%S")))
        return ("version/web_static_{}.tgz".format(time.
            strftime("%Y%m%d%H%M%S")))
    except:
        return None
