#!/usr/bin/env python
from __future__ import with_statement
from fabric.api import local, settings, abort, run, cd, env
from fabric.contrib.console import confirm
import os

# glogal env
env.warn_only = True

def clean():
    local("find . -name '*.DS_Store' -type f -delete")
    local("find . -name '*.pyc' -type f -delete")

"""
Definition instances
"""
def docs():
    env.hosts = ['wdd311.anorg.net']
    env.path = 'www/docs'
    env.local_path = 'docs/_build/html/'
    env.username = 'wdd311.anorg.net'
    

def upload():
    
    # build the docs
    try:
        local('cd docs; make html')
    except Exception, e:
        print e
        pass

    # upload to ftp
    try:
        local('lftp -u %s -e "mirror --reverse --delete --only-newer %s %s;quit" %s' % \
              (env.username, env.local_path, env.path, env.host))
    except Exception, e:
        print e
        pass
