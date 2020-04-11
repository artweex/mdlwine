# INSTALLATION
# for python 3.x:   > pip install fabric3
# For python 2.7.x: > pip install fabric
import os
import sys
from fabric.api import (local, run, env, cd, hosts, sudo, put, settings)
from fabric.contrib.files import exists
from fabric.contrib.project import rsync_project
from sys import platform as _platform
from builtins import input

PYTHON_VERSION = sys.version_info
PROJECT_DIR =  os.path.dirname(os.path.abspath(__file__))

server_url = ['', ]

env.user = "root"
# env.key_filename = ['Artem_rsa_sec', ]
env.password = ''


# @hosts(server_url)
# def deploy():
# 	global gitpwd
# 	with settings(warn_only=True, prompts={"Password for 'https://AnKang1@bitbucket.org': ": gitpwd}) as _:
# 		with cd('/home/ds') as _:
# 			run("docker stop $(docker ps -a -q)")
# 			run("git pull origin master")
# 			run("docker-compose -f docker-compose-prod.yml down")
# 			run("docker-compose -f docker-compose-prod.yml build")
# 			run("docker-compose -f docker-compose-prod.yml up -d")


# @hosts('localhost')
# def commit():
# 	with settings(warn_only=True, prompts={"Password for 'https://AnKang1@bitbucket.org': ": gitpwd}) as _:
# 		title = input("Enter app name: ")
# 		local(f"git add . && git commit -m \"{title}\"")
# 		local(f"git push origin master")

@hosts('localhost')
def startapp():
	"""Create new django app"""
	global PROJECT_DIR
	appname = input("Enter app name: ")
	# django_path = os.path.join(PROJECT_DIR, 'src', 'django')
	app_path = './apps/{0}'.format(appname)
	# if not exists(app_path):
	#     local( 'mkdir {0}'.format(app_path) )
	local( 'docker-compose run django python manage.py startapp {0} {1}'.format( appname, app_path ) )

@hosts('localhost')
def migrate():
	local('docker-compose exec django python manage.py makemigrations')
	local('docker-compose exec django python manage.py migrate')

@hosts('localhost')
def start():
	global PROJECT_DIR
	local(f'cd { PROJECT_DIR } && docker-compose up')

@hosts('localhost')
def recreate():
	global PROJECT_DIR
	local(f'cd { PROJECT_DIR } && docker-compose down && docker-compose build && docker-compose up')

@hosts('localhost')
def stop():
	global PROJECT_DIR
	try:
		if _platform == "linux" or _platform == "linux2" or _platform == "darwin":
			local("docker stop $(docker ps -a -q)")
		elif _platform == "win32" or _platform == "win64":
			local('FOR /f "tokens=*" %i IN (\'docker ps -a -q\') DO docker stop %i')  # windows CMD
			#  docker stop @(docker ps -aq) # for windows PowerShell only
	except Exception as e:
		print("Error: {0}".format(e))
	local(f'cd { PROJECT_DIR } && docker-compose down')

@hosts('localhost')
def static():
	local("docker-compose exec django python manage.py collectstatic --noinput")