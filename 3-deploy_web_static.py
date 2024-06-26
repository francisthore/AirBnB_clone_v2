#!/usr/bin/python3
""" Fabric script that distributes
an archive to the web servers"""

do_pack = __import__('1-pack_web_static').do_pack
do_deploy = __import__('2-do_deploy_web_static').do_deploy


def deploy():
    """Function to deploy fully"""
    pack = do_pack()
    if pack is None:
        return False
    res = do_deploy(pack)
    return res
