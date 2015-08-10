import os
import shutil
from subprocess import call

git_global = os.path.expanduser('~') + '/git_global/'
hooks = git_global + 'hooks/'
if not os.path.exists(hooks):
	os.makedirs(hooks)

shutil.copy('post-commit', hooks)
shutil.copy('post-commit.py', hooks)

call('git config --global init.templatedir "' + git_global + '"', shell=True)