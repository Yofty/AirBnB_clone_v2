#!/usr/bin/python3
"""generates a .tgz archive from the contents of the web_static"""
from fabric.api import local
from datetime import datetime


@runs_once
def do_pack():
    """generates a .tgz archive from the contents of the web_static"""
    local("mkdir -p version")
    path = ("versions/web_static_{}.tgz".
            format(datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")))
    result = local("tar -cvzf {} web_static".fortmat(path))

    if result.failed:
        return None
    return path
