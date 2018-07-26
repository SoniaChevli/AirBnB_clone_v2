#!/usr/bin/python3
'''
Write a Fabric script that
generates a .tgz archive
from the contents of the web_static
'''
from fabric.api import local
import datetime


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
