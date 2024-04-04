#!/usr/bin/python3
"""Compresses web static contents
to a tgz file
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """Packages webstatic content
    for our deployment"""
    date = datetime.now().strftime('%Y%m%d%H%M%S')
    archive_path = "versions/web_static_{}.tgz".format(date)
    local("mkdir -p versions")
    res = local("tar -cvzf {} web_static".format(archive_path), capture=True)

    if res.succeeded:
        return archive_path
    else:
        return None
