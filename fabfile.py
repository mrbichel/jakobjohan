from fabric.api import env, run, prefix, cd, sudo, local

env.user = 'johan'
env.hosts = ['tango.johan.cc']
env.directory = '/home/johan/srv/jakobjohan'
env.activate = 'source /home/johan/.virtualenvs/jakobjohan/bin/activate'

def deploy():
    local('git push')
    with cd(env.directory):
        with prefix(env.activate):
            run('git pull')
            run('pip install -r requirements.txt')
            run('python manage.py migrate')
            run('python manage.py cleanup')
            run('touch jakobjohan/wsgi.py') # this triggers a gracefull reload
