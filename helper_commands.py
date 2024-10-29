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

def commandsList(ctx: commands.Context): # type: ignore
    pass

def join(ctx: commands.Context): # type: ignore
    pass


def admin_check(ctx: commands.Context) -> discord.Embed | bool: # type: ignore
    embed = discord.Embed()
    if ctx.author != '':
        embed.add_field(name="ADMIN", value=f"YOU ARE NOT AN ADMIN YOU NERD")
        return embed
    else:
        return True