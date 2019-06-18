NFL rankings and predictions
############################

Python package to source NFL game data and generate rankings and predictions using the `Margin-dependent Elo (MELO) <https://github.com/morelandjs/melo>`_ model.

Installation
============
.. code-block:: Bash

    git clone git@github.com:morelandjs/nflrank.git && cd nflrank
    pip install -r requirements.txt

Usage
=====

This package contains two modules in the ``src`` directory.
The first ``update_database.py`` initializes and syncs the NFL game data SQL database, and the second ``train_model.py`` pulls game stats from the database to generate model predictions.
Each module is intended to be run as a script from the parent directory, e.g. ::

    python -m src.update_database
    python -m src.train_model

Running the ``train_model.py`` module generates a json file containing a ranked list of all NFL teams based on the current state of the SQL database.
