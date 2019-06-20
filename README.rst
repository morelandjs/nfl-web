NFL rankings and predictions
############################

Package to source NFL game data, generate rankings and predictions using the `Margin-dependent Elo (MELO) <https://github.com/morelandjs/melo>`_ model, and post the predictions to a static web page.

Installation
============

First, clone the git repository and cd into the parent directory. ::

   git clone git@github.com:morelandjs/nfl-model.git && cd nfl-model

Next, activate a Python2 virtual environment. ::

    python2 -m virtualenv env
    source env/bin/activate

Finally, install the package using pip. ::

    pip2 install -r requirements.txt

Note, due to the limitations of ``nflgame``, all packages must be installed into a Python2 virtual environment.

Usage
=====

Building the static website requires three actions:

1. Download the NFL game data and store it in a SQL database.
2. Train the Margin-dependent Elo (MELO) model using the contents of the database.
3. Compile the static webpage using the predictions of the model.

Keeping the website current therefore involves iterating over each action as many times as necessary.

The NFL game data is acquired by running the ``update_database.py`` script contained in the package's model folder. ::

   python -m model.update_database

Once the database is populated, compile (or recompile) the static webpage to display the latest model results. ::

   ./build.sh
