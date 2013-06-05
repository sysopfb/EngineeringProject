#!/usr/bin/env python
from mtg import *
from mtg.models import *
from flask import *

try:
    from IPython import embed
    embed()
except ImportError:
    import os
    import readline
    from pprint import pprint
    os.environ['PYTHONINSPECT'] = 'True'
