import os
from pathlib import Path


workdir = Path(os.getcwd())

datadir = workdir / 'data'
if not datadir.exists():
    datadir.mkdir(parents=True)

dbpath = datadir / 'nfldb.sqlite'
