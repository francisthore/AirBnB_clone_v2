#!/usr/bin/python3
""" Fabric script that distributes
an archive to the web servers
"""

from fabric.api import put, run, env, local
import os

env.hosts = ['100.26.229.162', '54.174.85.129']


def do_deploy(archive_path):
    """
    Distributes an archive to the web servers
    """
    if not os.path.exists(archive_path):
        return False
    try:
        archive = os.path.basename(archive_path).split('.')[0]
        dest_path = "/data/web_static/releases/{}/".format(archive)
        put(archive_path, "/tmp/")
        run("mkdir -p {}".format(dest_path))
        run("tar -xzf /tmp/{}.tgz -C {}".format(archive, dest_path))
        run("rm /tmp/{}.tgz".format(archive))
        run("mv {}web_static/* {}".format(dest_path, dest_path))
        run("rm -rf {}web_static".format(dest_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(dest_path))
        print("New version deployed!")
        return True
    except Exception as e:
        return False
