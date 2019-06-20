#!/usr/bin/env python2

from datetime import datetime
import json
import sqlite3

from melo import Melo
import numpy as np

from . import dbpath


def read_table(conn):
  """
  Returns the contents of the games table.

  """
  c = conn.cursor()
  c.execute("SELECT * FROM games ORDER BY date")

  dtype = [
      ('date',       'S10'),
      ('season',     '<i4'),
      ('week',       '<i4'),
      ('team_home',  'S10'),
      ('score_home', '<i4'),
      ('team_away',  'S10'),
      ('score_away', '<i4'),
  ]

  return np.rec.array(c.fetchall(), dtype=dtype)


def get_rankings():
  # read nfl game data from sql table
  conn = sqlite3.connect(str(dbpath))
  gamedata = read_table(conn)

  # melo model training inputs
  dates = gamedata.date
  teams_home = gamedata.team_home
  scores_home = gamedata.score_home
  teams_away = gamedata.team_away
  scores_away = gamedata.score_away

  # define a binary comparison statistic
  spreads = [int(h) - int(a) for h, a
             in zip(scores_home, scores_away)]

  # initialize the estimator
  nfl_spreads = Melo(.245, lines=np.arange(-50.5, 51.5), commutes=False,
                     regress=lambda months: .413 if months > 3 else 0,
                     regress_unit='month')

  # fit the estimator to the training data
  nfl_spreads.fit(dates, teams_home, teams_away, spreads, biases=.166)

  # rank nfl teams at end of 2018 regular season
  rankings = nfl_spreads.rank(datetime.now(), statistic='mean')
  return rankings


if __name__ == '__main__':

  rankings = get_rankings()
  # save rankings to json file
  with open('website/static/rankings.json', 'w') as f:
    json.dump(rankings, f)
