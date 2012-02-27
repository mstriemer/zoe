import os
from datetime import datetime

from fabric.api import local, run, env, cd, sudo, abort, settings

env.hosts = ['mark@striemer.ca']

def test(location='local'):
    if location == 'local':
        local('./manage.py test')
    elif location == 'remote':
        run('./manage.py test')
    else:
        abort("Don't know how to run tests for the '{0}' location.".format(
                location))

def deploy():
    code_dir = '/var/apps/zoe/newdeploy'
    with settings(warn_only=True):
        if run('test -d {0}'.format(code_dir)).failed:
            run('git clone git://github.com/mstriemer/zoe.git {0}'.format(
                    code_dir))
    with cd(code_dir):
        run('git pull')
        restart_app()

def restart_app():
    sudo('service zoe restart')

# options = {
#     'app_name': 'zoe',
#     'branch_name': 'master',
# }
# 
# def compute(template, *args, **kwargs):
#     kwargs.update(options)
#     return template.format(*args, **kwargs)
# 
# def option(name):
#     if name in options:
#         return options[name]
#     else:
#         return None
# 
# def archive(branch=option('branch_name')):
#     with cd(compute("~/{app_name}")):
#         run("git pull")
#         run("git archive --format zip --output archive.zip {0}".format(branch))
# 
# def expand(target=compute('/var/apps/{app_name}/')):
#     folder = datetime.now().strftime('%Y%m%d%H%M%S')
#     sudo(compute("mkdir -p {0}releases/{1}/", target, folder))
#     sudo(compute("unzip ~/{app_name}/archive.zip -d {0}releases/{1}/",
#             target, folder))
#     run(compute("rm ~/{app_name}/archive.zip"))
#     update_symlinks(target, folder)
# 
# def update_symlinks(target, folder):
#     current = target + 'releases/' + folder
#     previous = target + 'current'
#     sudo('ln -s {0}shared/settings/local.py {1}/zoe/settings/'.format(target, current))
#     sudo("rm -f {0}".format(previous))
#     sudo("ln -s {0} {1}".format(current, previous))
# 
# def restart_app():
#     sudo('service zoe restart')
# 
# def deploy(branch=None, expand_target=None):
#     if branch is None:
#         archive()
#     else:
#         archive(branch)
#     if expand_target is None:
#         expand()
#     else:
#         expand(expand_target)
    # restart_app()
