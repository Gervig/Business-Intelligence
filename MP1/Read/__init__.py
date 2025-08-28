# Python libraries
import pandas as pd
import numpy as np
import json, os

# allows all imports (*) from this package
__all__ = ['readfile', 'readweb']

from . import readfile, readweb
from . readfile import jsonio
from . readweb import api

# prints a successful import message
print("package imported")