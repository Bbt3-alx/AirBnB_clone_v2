#!/usr/bin/python3
"""
A Fabric script that generates a .tgz archive from the contents of the
web_static folder of AirBnB Clone repo, using the function do_pack
"""


from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """Compress data"""
    if not os.path.exists('versions'):
        os.makedirs('versions')

    FILENAME = datetime.now().strftime("%Y%m%d%H%M%S")
    ARCHIVE_PATH = f'versions/web_static_{FILENAME}.tgz'


    result = local(f'tar -czf {ARCHIVE_PATH} web_static')

    if result.failed:
        return None
    return ARCHIVE_PATH
