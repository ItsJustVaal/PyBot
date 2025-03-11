# Set Fixtures
# Add Fixture
# Update Fixture
# Remove Fixture
# Fixtures for Game Week X

# Set Results
# Update Results
# Current Results
# Results for Game Week X

# Set Game Week
# Lock and Unlock

import discord
import sqlite3
from discord.ext import commands
from helper_commands import get_timestamp


def set_fixtures(ctx: commands.Context, cursor: sqlite3.Cursor) -> discord.Embed: # type: ignore
    # NOTE: Make a fixture cache so I dont have to call teh DB everytime 
    # and so I can keep a structured format for the embeds when people call commands
    # against the fixture list. If the list is updated in anyway make sure to update
    # the cache as well.
    print(f"USER: {ctx.author} CALLED COMMAND: {ctx.invoked_subcommand}")
    
    embed = discord.Embed()
    fixtures_list: list[str] = ctx.message.content.split(sep=" ")[1:]
    gameweek: str = fixtures_list[0]
    for fixture in fixtures_list[1:]:
        home, away = fixture.split(sep="-")
        time: str = get_timestamp()
        print(f"FIXTURE SET - GAMEWEEK: {gameweek}, HOME: {home}, AWAY: {away}")
        try:
            cursor.execute(f"INSERT INTO fixtures VALUES('{home}', '{away}', 0, 0, {gameweek},'{time}','{time}')")
        except Exception as e:
            print(f"FAILED TO ADD FIXTURES WITH ERROR: {e}")
    
    embed_fixture: str = '\n'.join(fixtures_list[1:])
    embed.add_field(name="FIXTURES SET", value=f"""GAMEWEEK: {gameweek}
                    HOME-AWAY:
                    {embed_fixture}""")
    return embed
    
    
def get_fixtures(ctx: commands.Context, cursor: sqlite3.Cursor) -> discord.Embed: # type: ignore
    print(f"USER: {ctx.author} CALLED COMMAND: {ctx.command}")
    
    message: list[str] = ctx.message.content.split(sep=" ")
    gameweek = cursor.execute("SELECT gameweek FROM fixtures ORDER BY gameweek DESC;").fetchone()[0]
    embed = discord.Embed()
    fixture_list: list[str] = []
    
    if len(message) > 1:
        if int(message[1]) <= gameweek:
            gameweek = int(message[1])
        else:
            embed.add_field(name="FIXTURES", value="You passed in a gameweek that is in the future")
            return embed
    else:
        print(f"No gameweek was passed in, leave as: {gameweek}")
    
    try:
        fixtures = cursor.execute(f"SELECT home_team, away_team FROM fixtures WHERE gameweek = {gameweek};").fetchall()
        if fixtures == []:
            embed.add_field(name="FIXTURES", value="You passed in a gameweek that doesn't exist")
            return embed
        
        for fixture in fixtures:
            fixture_list.append(f"{fixture[0]} - {fixture[1]}")
    except Exception as e:
        print(e)
        
    
    fixture_string: str = '\n'.join(fixture_list)
    embed.add_field(name=f"FIXTURES FOR GAMEWEEK {gameweek}", value=f"""HOME - AWAY:
                    {fixture_string}""")
    return embed

def update_fixture(ctx: commands.Context, cursor: sqlite3.Cursor) -> discord.Embed: # type: ignore
    print(f"USER: {ctx.author} CALLED COMMAND: {ctx.command}")
    
    message: list[str] = ctx.message.content.split(sep=" ")
    gameweek = cursor.execute("SELECT gameweek FROM fixtures ORDER BY gameweek DESC;").fetchone()[0]
    embed = discord.Embed()
    
    if len(message) > 1:
        if int(message[1]) <= gameweek:
            gameweek = int(message[1])
        else:
            embed.add_field(name="FIXTURES", value="You passed in a gameweek that is in the future")
            return embed
    else:
        print(f"No gameweek was passed in, leave as: {gameweek}")
    
    #Message2 = home or away
    #Message1 = gameweek
    #Message3 = current entry
    #Message4 = fixed entry 
    print(f"UDPATE fixtures SET {message[2]} = {message[4]} WHERE gameweek = {message[1]} AND {message[2]} = {message[3]};")
    cursor.execute(f"UPDATE fixtures SET {message[2]} = '{message[4]}' WHERE gameweek = {message[1]} AND {message[2]} = '{message[3]}';")
    embed: discord.Embed = get_fixtures(ctx=ctx, cursor=cursor)
    return embed

def delete_fixture(ctx: commands.Context, cursor: sqlite3.Cursor) -> discord.Embed: # type: ignore
    print(f"USER: {ctx.author} CALLED COMMAND: {ctx.command}")
    
    message: list[str] = ctx.message.content.split(sep=" ")
    gameweek = cursor.execute("SELECT gameweek FROM fixtures ORDER BY gameweek DESC;").fetchone()[0]
    embed = discord.Embed()
    
    if len(message) > 1:
        if int(message[1]) <= gameweek:
            gameweek = int(message[1])
        else:
            embed.add_field(name="FIXTURES", value="You passed in a gameweek that is in the future")
            return embed
    else:
        print(f"No gameweek was passed in, leave as: {gameweek}")
        
    print(f"DELETE FROM fixtures WHERE gameweek = {message[1]} AND home_team = {message[2]} AND away_team = {message[3]}")
    cursor.execute(f"DELETE FROM fixtures WHERE gameweek = {message[1]} AND home_team = '{message[2]}' AND away_team = '{message[3]}';")
    embed: discord.Embed = get_fixtures(ctx=ctx, cursor=cursor)
    return embed

def add_fixture(ctx: commands.Context, cursor: sqlite3.Cursor) -> discord.Embed: # type: ignore
    print(f"USER: {ctx.author} CALLED COMMAND: {ctx.command}")
    
    message: list[str] = ctx.message.content.split(sep=" ")
    gameweek = cursor.execute("SELECT gameweek FROM fixtures ORDER BY gameweek DESC;").fetchone()[0]
    embed = discord.Embed()
    
    if len(message) > 1:
        if int(message[1]) <= gameweek:
            gameweek = int(message[1])
        else:
            embed.add_field(name="FIXTURES", value="You passed in a gameweek that is in the future")
            return embed
    else:
        print(f"No gameweek was passed in, leave as: {gameweek}")
        
    print(f"INSERT INTO fixtures (gameweek, home_team, away_team) VALUES ({message[1]}, {message[2]}, {message[3]})")
    cursor.execute(f"INSERT INTO fixtures (gameweek, home_team, away_team) VALUES ({message[1]}, '{message[2]}', '{message[3]}');")
    embed: discord.Embed = get_fixtures(ctx=ctx, cursor=cursor)
    return embed