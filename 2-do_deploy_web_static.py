#!/usr/bin/python3
"""Deploys an archive
"""
from fabric.api import env, put, run, local
import os

env.hosts = ['3.84.239.148', '100.26.243.121']


def do_deploy(archive_path):
    """Distributes an archive to webservers"""
    if not os.path.exists(archive_path):
        return False
    try:
        archive = os.path.basename(archive_path).split('.')[0]
        put(archive_path, "/tmp/")
        run("mkdir -p /data/web_static/releases/{}/".format(archive))
        run("tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}/".format(archive, archive))
        run("rm /tmp/{}.tgz".format(archive))
        run("mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/".format(archive, archive))
        run("rm -rf /data/web_static/releases/{}/web_static".format(archive))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current".format(archive))
        return True
    except:
        return False
