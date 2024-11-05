import sqlite3
import discord
import datetime
import zoneinfo
from discord.ext import commands


# Returns embed to test if bot is functional
def test(ctx: commands.Context) -> discord.Embed: # type: ignore
    # Log Command Call
    print(f"USER: {ctx.author} CALLED COMMAND: {ctx.invoked_subcommand}")

    # Make and return Embed
    embed = discord.Embed()
    embed.add_field(name="TEST", value=f"YOU CALLED TEST WITH ARGS {ctx.message.content.split(sep=" ")[1:]}")
    return embed

def cmds(ctx: commands.Context) -> discord.Embed: # type: ignore
    print(f"USER: {ctx.author} CALLED COMMAND: {ctx.invoked_subcommand}")
    
    embed = discord.Embed()
    embed.add_field(name="A LIST OF AVAILABLE COMMANDS", 
                    value="""test - Test if bot is working
                            join - Join to use most of the bot commands
                            cmds - See available commands""")

    return embed

def join(ctx: commands.Context, cursor: sqlite3.Cursor) -> discord.Embed: # type: ignore
    print(f"USER: {ctx.author} CALLED COMMAND: {ctx.command}")
    embed = discord.Embed()
    check = True
    
    
    user = user_check(ctx=ctx, cursor=cursor) # type: ignore
    if user:
        embed.add_field(name="JOIN", value="You are already in the system, .cmds for commands")
        return embed
    time: str = get_timestamp()
    print(time)
    try:
        cursor.execute(f"INSERT INTO members VALUES({ctx.author.id}, 0, 0, 0, 2, 0, 0, '{time}', '{time}');")
    except Exception as e:
        print(e)
        check = False
        
    if check:
        embed.add_field(name="JOIN", value="YOU JOINED! Type .cmds to see available commands")
    else:
        embed.add_field(name="JOIN", value="YOU FAILED TO JOINED! FIND AN ADULT")
        
    return embed
        

def my_card(ctx: commands.Context, cursor: sqlite3.Cursor) -> discord.Embed: # type: ignore
    print(f"USER: {ctx.author} CALLED COMMAND: {ctx.command}")
    
    embed = discord.Embed()
    
    try:
        user = user_check(ctx=ctx, cursor=cursor) # type: ignore
        if user == None:
            embed.add_field(name="MY CARD", value="YOU DONT EXIST, TYPE .JOIN")
        else:
            print(user)
            embed.add_field(name="MY CARD", value=f"""
                            Money: {user[1]}
                            Gameweek Points: {user[2]}
                            Overall Points: {user[3]}
                            Daily Free Packs: {user[4]}
                            Scrabble Wins: {user[5]}
                            Fish Caught: {user[6]}
                            """)
    except Exception as e:
        print(f"COMMAND FAILED WITH ERROR: {e}")
        embed.add_field(name="JOIN", value="YOU FAILED TO JOIN! FIND AN ADULT")
        
    return embed
    
    

# ~~~~ HELPER FUNCTIONS ~~~~

def admin_check(ctx: commands.Context) -> bool: # type: ignore
    if ctx.author.id != 123499749696471042:
        return False
    return True

def user_check(ctx: commands.Context, cursor: sqlite3.Cursor): # type: ignore
    try:
        user = cursor.execute(f"SELECT * FROM members WHERE discord_id = {ctx.author.id};").fetchone()
    except Exception as e:
        print(f"USER CHECK FAILED WITH ERROR: {e}")

    return user # type: ignore

def get_timestamp() -> str:
    return datetime.datetime.now(tz=zoneinfo.ZoneInfo(key="US/Pacific")).strftime(format="%Y-%m-%d %H:%M:%S")
