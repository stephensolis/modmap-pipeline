#!/usr/bin/env python

# this is the PyInstaller entrypoint

import multiprocessing
multiprocessing.freeze_support()

from modmap_toolkit.__main__ import main  # NOQA
main()
