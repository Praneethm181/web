from fabric.api import cd, env, local, run

env.hosts = ['pythoncanarias.es']


def deploy():
    local('git push')
    with cd('~/web'):
        run('git pull')
        run('pipenv install')
        run('npm install --no-save')
        run('gulp')
        run('pipenv run python manage.py migrate')
        run('pipenv run python manage.py collectstatic --noinput --clear')
        run('supervisorctl restart web')
        run('supervisorctl restart rq')
