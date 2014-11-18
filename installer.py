import sys, shutil
from subprocess import call

template = sys.executable[:-10] + 'templates\\'
hooks = template + 'hooks\\'

call('mkdir ' + hooks, shell=True)
shutil.copy('post-commit', hooks)
shutil.copy('post-commit.py', hooks)

call('git config --global init.templatedir "' + template + '"', shell=True)