NFL rankings and predictions
############################

Package to source NFL data and generate rankings and predictions using the `Margin-dependent Elo (MELO) <https://github.com/morelandjs/melo>`_ model.

Installation
============

.. code-block:: Bash

    git clone git@github.com:morelandjs/nfl-model.git && cd nfl-model
    python2 -m virtualenv env
    source env/bin/activate
    pip2 install -r requirements.txt

Note, due to the limitations of ``nflgame``, all packages should be installed into a Python2 virtual environment.

Usage
=====

This package contains two modules in the ``src`` directory.
The first ``update_database.py`` initializes and syncs the NFL game data SQL database, and the second ``train_model.py`` pulls game stats from the database to generate model predictions.
Each module is intended to be run as a script from the parent directory, e.g.

.. code-block:: Bash

    python -m src.update_database
    python -m src.rank_teams

Running the ``train_model.py`` module generates a json file containing a ranked list of all NFL teams based on the current state of the SQL database.
