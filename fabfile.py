from __future__ import print_function
from datetime import datetime

from fabric.api import local, run, env, cd, sudo

env.hosts = ['mark@striemer.ca']

options = {
    'app_name': 'zoe',
    'branch_name': 'master',
}

def compute(template, *args, **kwargs):
    kwargs.update(options)
    return template.format(*args, **kwargs)

def option(name):
    if name in options:
        return options[name]
    else:
        return None

def archive(branch=option('branch_name')):
    with cd(compute("~/{app_name}")):
        run("git pull")
        run("git archive --format zip --output archive.zip {0}".format(branch))

def expand(target=compute('/var/apps/{app_name}/')):
    folder = datetime.now().strftime('%Y%m%d%H%M%S')
    sudo(compute("mkdir -p {0}releases/{1}/", target, folder))
    sudo(compute("unzip ~/{app_name}/archive.zip -d {0}releases/{1}/",
            target, folder))
    run(compute("rm ~/{app_name}/archive.zip"))
    update_symlinks(target, folder)

def update_symlinks(target, folder):
    current = target + 'releases/' + folder
    previous = target + 'current'
    sudo(compute("mkdir -p {0}/{app_name}/media/admin", current))
    sudo(compute("ln -s /lib/django-trunk/django/contrib/admin/static/admin "
        "{0}/{app_name}/media/admin", current))
    sudo("rm -f {0}".format(previous))
    sudo("ln -s {0} {1}".format(current, previous))


def reload_apache():
    sudo("/etc/init.d/apache2 reload")

def deploy(branch=None, expand_target=None):
    if branch is None:
        archive()
    else:
        archive(branch)
    if expand_target is None:
        expand()
    else:
        expand(expand_target)
