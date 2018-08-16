#!/usr/bin/python3
'''
Write a Fabric script that
generates a .tgz archive
from the contents of the web_static
'''
from fabric.api import *
import datetime
import os.path



env.hosts = ['104.196.182.229', '35.196.48.12']
env.user = "ubuntu"
env.key_filename = "~/.ssh/holberton"

def do_pack():
    ''' generates a .tgz archive '''
    try:
        now = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        local('sudo mkdir -p ./versions')
        local("sudo tar -cvzf versions/web_static_{}.tgz web_static/"
              .format(now))
        return "versions/web_static_{}.tgz".format(now)
    except:
        return None

def do_deploy(archive_path):
    ''' distributes an archive to web server '''

    filename = archive_path.split('/')[-1]
    archivefile = filename.split('.')[0]
    archivefolder = ("/data/web_static/releases/{}".format(archivefile))




    put(archive_path, "/tmp/{}".format(filename))
    run("mkdir -p {}".format(archivefolder))
    run("tar -xzf /tmp/{} -C {}".format(filename, archivefolder))
    run('rm /tmp/{}'.format(filename))
    run('mv {}/web_static/* {}'.format(archivefolder, archivefolder))
    run('rm -rf {}/web_static/'.format(archivefolder))
    run('rm -rf /data/web_static/current')
    run('ln -s {} /data/web_static/current'.format(archivefolder))
    print('works')
    return True
'''
    except:
        print('fail')
        return False
'''
