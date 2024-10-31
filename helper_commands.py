import sqlite3
import discord
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
    print(f"USER: {ctx.author} CALLED COMMAND: {ctx.invoked_subcommand}")
    
    embed = discord.Embed()
    check = True
    try:
        cursor.execute(f"INSERT INTO members VALUES({ctx.author.id}, 0, 0, 0, 2)")
    except:
        check = False
        
    if check:
        embed.add_field(name="JOIN", value="YOU JOINED! Type .cmds to see available commands")
    else:
        embed.add_field(name="JOIN", value="YOU FAILED TO JOINED! FIND AN ADULT")
        
    return embed
        
    
    


def admin_check(ctx: commands.Context) -> discord.Embed | bool: # type: ignore
    if ctx.author.id != 123499749696471042:
        return False
    return True