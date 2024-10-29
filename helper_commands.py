import discord
from discord.ext import commands


# Returns embed to test if bot is functional
def test(ctx: commands.Context) -> discord.Embed: # type: ignore
    
    # Log Command Call
    print(ctx.message.content.split(sep=" ")[1:])

    # Make and return Embed
    embed = discord.Embed()
    embed.add_field(name="TEST", value=f"YOU CALLED TEST WITH ARGS {ctx.message.content.split(sep=" ")[1:]}")
    return embed

def help(ctx: commands.Context): # type: ignore
    pass

def join(ctx: commands.Context): # type: ignore
    pass