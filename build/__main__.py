
import os
import sys

parent_dir = os.path.dirname(__file__)
sys.path.insert(0, parent_dir)

import build
build.main()
