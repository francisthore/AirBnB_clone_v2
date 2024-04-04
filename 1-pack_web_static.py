#!/usr/bin/python3
"""Compresses web static contents
to a tgz file
"""
from fabric.api import local


def do_pack():
    """Packages webstatic content
    for our deployment"""
    date = "$(date '+%Y%m%d%H%M%S')"
    local("mkdir versions")
    local("tar -cvzf versions/web_static_{}.tgz web_static".format(date))
