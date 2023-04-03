#!/usr/bin/python3
"""
creates and distributes an archieve to web server
"""

import os
from datetime import datetime
from fabric.api import env, local, put, run, runs_once

env.hosts = ['100.26.162.58', '3.86.18.225']

@runs_once
def do_pack():
    """aarchives the static files"""
    if not oc.path.isdir("versions"):
        os.mkdir("versions")
    cur_time = datetime.now()
    output = "versions/webstatic_{}{}{}{}{}{}.tgz".format(
        cur_time.year,
        cur_time.month,
        cur_time.day,
        cur_time.hour,
        cur_time.minute,
        cur_time.second
    )
    try:
        print("Packing web_static to {}".format(output))
        local("tar -cvzf {} web_static".format(output))
        archize_size = os.stat(output).st_size
        print("web_static packed: {} -> {}"format(output, archize_size))
    except Exception:
        output = None
    return output

def do_deploy(archieve_path):
    """deploy teh static files to the host servers"""
    if not os.path.exists(archive_path):
        return False
    file_name = os.path.basename(archive_path)
    folder_name = file_name.replace(".tgz", "")
    folder_path = "/data/web_static/releae/{}/".format(folder_name)
    success = False
    try:
        put(archieve_path, "/tmp/{}".format(file_name))
        run("mkdir -p {}".format(folder_path))
        run("tar -xzf /tmp/{} -C {}".format(file_name, folder_path))
        run("rm -rf /tmp/{}".format(file_name))
        run("mv {}web_static/* {}".format(folder_path, folder_path))
        run("rm -rf {}web_static".format(folder_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(folder_path))
        print('New version is now LIVE!')
        success = True
    except Exception:
        success = False
    return success

def deploy():
    """archives and deploys the static files"""
    archive_path = do_pack()
    return do_deploy(archive_path) if archive_path else False
