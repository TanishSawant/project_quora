#!C:\Users\tanis\PycharmProjects\Quizlets\project_quora\myenv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'pipp==0.0.1','console_scripts','pipp'
__requires__ = 'pipp==0.0.1'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('pipp==0.0.1', 'console_scripts', 'pipp')()
    )
