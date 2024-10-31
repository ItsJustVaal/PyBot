import sqlite3


def create_members_table(cursor: sqlite3.Cursor) -> None:
    cursor.execute(""" CREATE TABLE IF NOT EXISTS members 
                   (id INTEGER, discord_id INTEGER PRIMARY KEY, money INTEGER, gameweek_points INTEGER, overall_points INTEGER, free_packs INTEGER) """)
    # ID
    # USERID = Discord ID
    # Money
    # Gameweek Points
    # Overall Points
    # Free Packs

def create_fixtures_table(cursor: sqlite3.Cursor) -> None:
    cursor.execute(""" CREATE TABLE IF NOT EXISTS fixtures 
                   (id INTEGER PRIMARY KEY, home_team TEXT, away_team TEXT, home_score INTEGER, away_score INTEGER, gameweek INTEGER) """)
    # ID
    # Home Team
    # Home Score
    # Away Team
    # Away Score
    # Game Week
    pass

def create_predictions_table(cursor: sqlite3.Cursor) -> None:
    cursor.execute(""" CREATE TABLE IF NOT EXISTS predictions 
                   (id INTEGER, discord_id INTEGER PRIMARY KEY, prediction_string TEXT, gameweek INTEGER) """)
    # ID
    # USERID
    # Prediction String
    # Game Week
    pass

def create_fut_table(cursor: sqlite3.Cursor) -> None:
    cursor.execute(""" CREATE TABLE IF NOT EXISTS fut 
                   (id INTEGER, discord_id INTEGER PRIMARY KEY, cards TEXT, costs TEXT, pack_type TEXT) """)
    # ID
    # USERID
    # Players
    # Costs
    # Pack Type
    pass

def check_if_table_exists(cursor: sqlite3.Cursor) -> None:
    listOfTables = cursor.execute(
        """SELECT * FROM sqlite_master WHERE type='table'; """).fetchall()
    
    if listOfTables == []:
        print('No tables found!')
    else:
        for table in listOfTables:
            print(table[1])