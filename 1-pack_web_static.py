#!/usr/bin/python3
"""
Module to handle archiving of the web_static folder using Fabric API.
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """
    Create a compressed archive of the web_static folder,
    return the path of the archive or None if the archiving
    process fails.
    """
    date = datetime.now().strftime('%Y%m%d%H%M%S')
    archive = "versions/web_static_{}.tgz".format(date)
    local('mkdir -p versions')
    res = local('tar -czvf {} web_static'.format(archive), capture=True)

    if res.succeeded:
        return archive
    else:
        return None
