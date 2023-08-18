from glob import glob
from keyword import iskeyword
from os.path import dirname, join, splitext, split

from ._factory import DataBaseFactory

__all__ = ['DataBaseFactory']

basedir = dirname(__file__)

for name in glob(join(basedir, '*.py')):
    module = splitext(split(name)[-1])[0]
    if module.startswith('_') and module.isidentifier() and not iskeyword(module):
        try:
            __import__(__name__ + '.' + module)
            print(f"import {__name__ + '.' + module} success.")
        except Exception as e:
            pass
