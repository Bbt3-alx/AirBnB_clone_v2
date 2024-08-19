#!/usr/bin/python3
"""A script that distributes an archive to a web server"""


from fabric import *
from fabric.api import *
import os


web_servers = ['100.27.10.204', '54.146.90.82']
env_user = 'ubuntu'


@task
def do_deploy(archive_path):
    """Distributes an archive to the web server"""

    # check if the archive_path exists
    if not os.path.exists(archive_path):
        return False

    try:
        # Loop through each host
        for host in web_server:
            # Create a connection for each host
            connection = Connection(host=host, user=env_user)


            # Upload the archive to the /tmp/ directory on the we server
            archive_name = os.path.basename(archive_path)
            connection.put(archive_path, f'/tmp/{archive_name}')

            # Create the release folder
            archive_base = os.path.splitext(archive_name)[0]
            release_folder = f'/data/web_static/releases/{archive_base}/'
            connection.sudo(f'mkdir -p {release_folder}')


            # Uncompress the archive
            connection.sudo(f'tar -xzf /tmp/{archive_name} -C {release_folder}')


            # Delete the archive from the web server
            connection.sudo(f'rm /tmp/{archive_name}')


            # Delete the old symbolic link
            connection.sudo('rm -rf /data/web_static/current')


            # Create a new symbolique link
            connection.sudo('ln -s {release_folder} /data/web_static/current')

        return True

    except Exception as e:
        return False
