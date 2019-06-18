#!/usr/bin/env python2

from datetime import datetime
from pathlib import Path
import sqlite3

import nflgame

from . import dbpath


def initialize_database(conn):
    """
    Initialize the SQL database and create the games table.

    """
    c = conn.cursor()
    c.execute("""
    CREATE TABLE IF NOT EXISTS games(
        date TEXT,
        season INTEGER,
        week INTEGER,
        team_home TEXT,
        score_home INTEGER,
        team_away TEXT,
        score_away INTEGER,
        UNIQUE(date, team_home, team_away));
    """)

    conn.commit()


def increment(year, week):
    """
    Increments the NFL (year, week) tuple.

    """
    if week in range(1, 17):
        return (year, week + 1)
    elif week == 17:
        return (year + 1, 1)
    else:
        raise ValueError('week must be in range 1 to 17 inclusive')


def start_update(conn):
    """
    Return season year and week of the most recent update.

    """
    c = conn.cursor()

    c.execute("SELECT season, week FROM games ORDER BY date DESC LIMIT 1")
    season_week = c.fetchone()

    return (2009, 1) if season_week is None else increment(*season_week)


def update_database(conn):
    """
    Save games to the SQL database.

    """
    now = datetime.now()
    c = conn.cursor()

    start_season, start_week = start_update(conn)
    end_season = now.year - 1 if now.month < 8 else now.year

    # loop over nfl season years 2009-present
    for season in range(start_season, end_season + 1):

        # loop over nfl weeks 1-17
        for week in range(start_week, 18):

            # print progress to stdout
            print('[UPDATING] Season {} Week {}'.format(season, week))

            # loop over games in season and week
            for g in nflgame.games(season, week, kind='REG'):
                year, month, day = [
                    g.schedule[k] for k in ['year', 'month', 'day']]
                date = datetime(year, month, day).strftime('%Y-%m-%d')
                values = (date, season, week,
                          g.home, g.score_home, g.away, g.score_away)

                try:
                    c.execute("""
                        INSERT INTO games(
                            date,
                            season,
                            week,
                            team_home,
                            score_home,
                            team_away,
                            score_away)
                        VALUES (?, ?, ?, ?, ?, ?, ?);
                    """, values)
                except sqlite3.IntegrityError:
                    continue

        # subsequent seasons should start from week 1
        start_week = 1

    conn.commit()


if __name__ == '__main__':

    # establish connection, then initialize and update database
    conn = sqlite3.connect(str(dbpath))
    initialize_database(conn)
    update_database(conn)
    conn.close()
