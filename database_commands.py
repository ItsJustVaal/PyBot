import sqlite3
from typing import Any

def create_tables(cursor: sqlite3.Cursor) -> None:
    create_members_table(cursor=cursor)
    create_fixtures_table(cursor=cursor)
    create_fut_table(cursor=cursor)
    create_predictions_table(cursor=cursor)
    check_if_table_exists(cursor=cursor)

    
def create_members_table(cursor: sqlite3.Cursor) -> None:
    cursor.execute("""CREATE TABLE IF NOT EXISTS members
                   (discord_id INTEGER, money INTEGER, gameweek_points INTEGER, overall_points INTEGER, free_packs INTEGER, scrabble INTEGER, fish INTEGER, created_at TEXT, updated_at TEXT);""")

def create_fixtures_table(cursor: sqlite3.Cursor) -> None:
    cursor.execute("""CREATE TABLE IF NOT EXISTS fixtures
                   (home_team TEXT, away_team TEXT, home_score INTEGER, away_score INTEGER, gameweek INTEGER, created_at TEXT, updated_at TEXT);""")

def create_predictions_table(cursor: sqlite3.Cursor) -> None:
    cursor.execute("""CREATE TABLE IF NOT EXISTS predictions
                   (discord_id INTEGER, home_team TEXT, away_team TEXT, home_score INTEGER, away_score INTEGER, gameweek INTEGER, created_at TEXT, updated_at TEXT);""")

def create_fut_table(cursor: sqlite3.Cursor) -> None:
    cursor.execute("""CREATE TABLE IF NOT EXISTS fut
                   (discord_id INTEGER, cards TEXT, costs TEXT, pack_type TEXT, created_at TEXT, updated_at TEXT);""")


def check_if_table_exists(cursor: sqlite3.Cursor) -> None:
    listOfTables: list[Any] = cursor.execute(
        """SELECT * FROM sqlite_master WHERE type='table'; """).fetchall()
    
    if listOfTables == []:
        print('No tables found!')
    else:
        for table in listOfTables:
            print(f"TABLE FOUND: {table[1]}")

            