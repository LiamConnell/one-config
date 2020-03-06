import os
import sys

# Allows to be run from command prompt ($ pytest) or with pycharm
if sys.argv[0].split('/')[-1] == 'pytest':
    os.chdir('tests')