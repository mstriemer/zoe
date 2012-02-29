import os
from datetime import datetime

from fabric.api import run, env, cd, sudo, settings

env.hosts = ['mark@striemer.ca']
env.app_name = 'zoe'
env.repo_name = 'repo'
env.root_dir = '/var/apps/zoe'
env.repo_dir = os.path.join(env.root_dir, env.repo_name)
env.shared_settings = os.path.join(env.root_dir, 'shared/settings/local.py')
env.local_settings = os.path.join(env.repo_dir, env.app_name,
        'settings/local.py')
env.branch_name = 'master'

def update_repo():
    with settings(warn_only=True):
        if run('test -d {repo_dir}'.format(**env)).failed:
            run('git clone git://github.com/mstriemer/zoe.git '
                '{repo_dir}'.format(**env))
    with cd(env.repo_dir):
        run('git fetch origin')
        sha = run('git ls-remote origin {branch_name}'.format(**env)).split()[0]
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        run('git checkout -b deploy_{timestamp} {sha}'.format(
                timestamp=timestamp, sha=sha))

def update_symlinks():
    with settings(warn_only=True):
        symlink_settings = run('test -e {local_settings}'.format(**env)).failed
    if symlink_settings:
        with cd(os.path.dirname(env.local_settings)):
            run('ln -s {shared_settings}'.format(**env))

def deploy(branch='master'):
    env.branch_name = branch
    update_repo()
    update_symlinks()
    restart_app()

def restart_app():
    sudo('service zoe restart')
