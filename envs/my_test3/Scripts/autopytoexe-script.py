
# -*- coding: utf-8 -*-
import re
import sys

from auto_py_to_exe.__main__ import run

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(run())
