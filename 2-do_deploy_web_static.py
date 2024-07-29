#!/usr/bin/python3
"""A script that distributes an archive to a web server"""


from fabric import Connection, task
import os


env.hosts = ['100.27.10.204', '54.146.90.82']
env_user = 'ubuntu'


@task
def do_deploy(archive_path):
    """Distributes an archive to the web server"""
    if not os.path.exists("archive_path"):
         return False
    
    try:
        c.put(archive_path, '/tmp/')
        
        # Create the release folder
        archive_name = os.path.basename(archive_path)
        archive_base = os.path.splitext(archive_name)[0]
        release_folder = f'/data/web_static/releases/archive_base/'

        for host in env_hosts:
            connection = connection(host=host, user=env_user)
            connection.sudo(f'mkdir -p {release_folder}')

            # Uncompress the archive
            connection.sudo(f'tar -xzf /tmp/{archive_path} -C /data/web_static/releases/')

            # Delete the archive from the web server
            connection.sudo(f'rm /tmp/{archive_path}')

            # Delete the old symbolic link
            connection.sudo('rm -rf /data/web_static/current')

            # Create a new symbolique link
            connection.sudo('ln -s {release_folder} /data/web_static/current')

        return True
    except Exception as e:
        return False
