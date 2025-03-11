import discord, os, sqlite3

from sqlalchemy import true
import helper_commands as hc
import database_commands as db
import fixture_commands as fc
# import fun_commands as fun
# import fut_commands as fut
# import points_commands as pc
# import prediction_commands as pred
from discord.ext import commands
from dotenv import load_dotenv, set_key


# ~~~~ LOAD ENV VARIABLES ~~~~
load_dotenv()
TOKEN: str | None = os.getenv(key="TOKEN")

UNLOCKED = 0

# ~~~~ CREATE AND CONFIGURE BOT ~~~~
intents: discord.Intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(
    command_prefix=commands.when_mentioned_or("."),
    intents=intents,
)

# ~~~~ CREATE AND CONFIGURE DB ~~~~
database: sqlite3.Connection = sqlite3.connect(database="./data/database.db")
database_cursor: sqlite3.Cursor = database.cursor()

# ~~~~ CREATE TABLES IF NOT EXIST & CHECK ~~~~
db.create_tables(cursor=database_cursor)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~ COMMANDS ~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~ Every Command will call for an embed then reply to the user ~
# ~ Most message should be ephemeral but check args ~
# ~ Going to be a lot of type: ignore due to missing types ~
# ~ These are in camelCase to match the original ones ~

# region ~~~~~~~~~~~~~~~~~~~~~~~~~~~ helpers ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@bot.command() # type: ignore
async def test(ctx: commands.Context) -> None: # type: ignore
    """
    Tests if bot is live
    """
    check_creds: bool = hc.admin_check(ctx=ctx) # type: ignore
    if check_creds == True:
        embed: discord.Embed = hc.test(ctx=ctx) # type: ignore
        await ctx.reply(embed=embed, ephemeral=True)
    else:
        await ctx.reply(content="You are not an admin omegalol") # type: ignore
    
    
@bot.command() # type: ignore
async def cmds(ctx: commands.Context) -> None: # type: ignore
    embed: discord.Embed = hc.cmds(ctx=ctx) # type: ignore
    await ctx.reply(embed=embed, ephemeral=True)


@bot.command() # type: ignore
async def join(ctx: commands.Context) -> None: # type: ignore
    embed: discord.Embed = hc.join(ctx=ctx, cursor=database_cursor) # type: ignore
    database.commit()
    await ctx.reply(embed=embed, ephemeral=True)
    
@bot.command() # type: ignore
async def me(ctx: commands.Context) -> None: # type: ignore
    embed: discord.Embed = hc.my_card(ctx=ctx, cursor=database_cursor) # type: ignore
    await ctx.reply(embed=embed, ephemeral=True)

# endregion
# region ~~~~~~~~~~~~~~~~~~~~~~~~~~~ fixtures ~~~~~~~~~~~~~~~~~~~~~~~~~~~
@bot.command(hidden=True) # type: ignore
async def setFixtures(ctx: commands.Context) -> None: # type: ignore
    check_creds: bool = hc.admin_check(ctx=ctx) # type: ignore
    if check_creds == True:
        embed: discord.Embed = fc.set_fixtures(ctx=ctx, cursor=database_cursor) # type: ignore
        await ctx.reply(embed=embed, ephemeral=True)
        database.commit()
    else:
        await ctx.reply(content="You are not an admin omegalol")


@bot.command(hidden=True) # type: ignore
async def updateFixture(ctx: commands.Context) -> None: # type: ignore
    check_creds: bool = hc.admin_check(ctx=ctx) # type: ignore
    if check_creds == True:
        embed: discord.Embed = fc.update_fixture(ctx=ctx, cursor=database_cursor) # type: ignore
        database.commit()
        await ctx.reply(embed=embed, ephemeral=True)
    else:
        await ctx.reply(content="You are not an admin omegalol")

@bot.command(hidden=True) # type: ignore
async def deleteFixture(ctx: commands.Context) -> None: # type: ignore
    check_creds: bool = hc.admin_check(ctx=ctx) # type: ignore
    if check_creds == True:
        embed: discord.Embed = fc.delete_fixture(ctx=ctx, cursor=database_cursor) # type: ignore
        database.commit()
        await ctx.reply(embed=embed, ephemeral=True)
    else:
        await ctx.reply(content="You are not an admin omegalol")

@bot.command(hidden=True) # type: ignore
async def addFixture(ctx: commands.Context) -> None: # type: ignore
    check_creds: bool = hc.admin_check(ctx=ctx) # type: ignore
    if check_creds == True:
        embed: discord.Embed = fc.add_fixture(ctx=ctx, cursor=database_cursor) # type: ignore
        database.commit()
        await ctx.reply(embed=embed, ephemeral=True)
    else:
        await ctx.reply(content="You are not an admin omegalol")
        
@bot.command() # type: ignore
async def fixtures(ctx: commands.Context) -> None: # type: ignore
    embed: discord.Embed = fc.get_fixtures(ctx=ctx, cursor=database_cursor) # type: ignore
    await ctx.reply(embed=embed, ephemeral=True)


@bot.command(hidden=True) # type: ignore
async def lock(ctx: commands.Context) -> None: # type: ignore
    global UNLOCKED
    print(f"Lock called, current lock state: {UNLOCKED}")
    check_creds: bool = hc.admin_check(ctx=ctx) # type: ignore
    if check_creds == True:
        if UNLOCKED == 0: # type: ignore
            UNLOCKED = 1
            await ctx.reply(content="Fixtures Locked")
        else: # type: ignore
            UNLOCKED = 0
            await ctx.reply(content="Fixtures Unlocked")
    else:
        await ctx.reply(content="You are not an admin omegalol")
        

# endregion
# region ~~~~~~~~~~~~~~~~~~~~~~~~~~~ results ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@bot.command(hidden=True) # type: ignore
async def setResults(ctx: commands.Context) -> None: # type: ignore
    embed: discord.Embed = hc.test(ctx=ctx) # type: ignore
    await ctx.reply(embed=embed, ephemeral=True)


@bot.command(hidden=True) # type: ignore
async def updateResults(ctx: commands.Context) -> None: # type: ignore
    embed: discord.Embed = hc.test(ctx=ctx) # type: ignore
    await ctx.reply(embed=embed, ephemeral=True)


@bot.command(hidden=True) # type: ignore
async def deleteResults(ctx: commands.Context) -> None: # type: ignore
    embed: discord.Embed = hc.test(ctx=ctx) # type: ignore
    await ctx.reply(embed=embed, ephemeral=True)


@bot.command() # type: ignore
async def results(ctx: commands.Context) -> None: # type: ignore
    embed: discord.Embed = hc.test(ctx=ctx) # type: ignore
    await ctx.reply(embed=embed, ephemeral=True)

# endregion
# region ~~~~~~~~~~~~~~~~~~~~~~~~~~~ fun ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@bot.command() # type: ignore
async def eball(ctx: commands.Context) -> None: # type: ignore
    embed: discord.Embed = hc.test(ctx=ctx) # type: ignore
    await ctx.reply(embed=embed, ephemeral=True)

@bot.command() # type: ignore
async def meme(ctx: commands.Context) -> None: # type: ignore
    embed: discord.Embed = hc.test(ctx=ctx) # type: ignore
    await ctx.reply(embed=embed, ephemeral=True)

# endregion
# region ~~~~~~~~~~~~~~~~~~~~~~~~~~~ predictions ~~~~~~~~~~~~~~~~~~~~~~~~
@bot.command() # type: ignore
async def predict(ctx: commands.Context) -> None: # type: ignore
    embed: discord.Embed = hc.test(ctx=ctx) # type: ignore
    await ctx.reply(embed=embed, ephemeral=True)


@bot.command() # type: ignore
async def mypred(ctx: commands.Context) -> None: # type: ignore
    embed: discord.Embed = hc.test(ctx=ctx) # type: ignore
    await ctx.reply(embed=embed, ephemeral=True)


@bot.command() # type: ignore
async def updatePred(ctx: commands.Context) -> None: # type: ignore
    embed: discord.Embed = hc.test(ctx=ctx) # type: ignore
    await ctx.reply(embed=embed, ephemeral=True)


# endregion
# region ~~~~~~~~~~~~~~~~~~~~~~~~~~~ points ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@bot.command() # type: ignore
async def updatePoints(ctx: commands.Context) -> None: # type: ignore
    embed: discord.Embed = hc.test(ctx=ctx) # type: ignore
    await ctx.reply(embed=embed, ephemeral=True)


@bot.command() # type: ignore
async def addPoints(ctx: commands.Context) -> None: # type: ignore
    embed: discord.Embed = hc.test(ctx=ctx) # type: ignore
    await ctx.reply(embed=embed, ephemeral=True)


@bot.command() # type: ignore
async def removePoints(ctx: commands.Context) -> None: # type: ignore
    embed: discord.Embed = hc.test(ctx=ctx) # type: ignore
    await ctx.reply(embed=embed, ephemeral=True)


@bot.command() # type: ignore
async def standings(ctx: commands.Context) -> None: # type: ignore
    embed: discord.Embed = hc.test(ctx=ctx) # type: ignore
    await ctx.reply(embed=embed, ephemeral=True)

# endregion
# region ~~~~~~~~~~~~~~~~~~~~~~~~~~~ fut ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@bot.command() # type: ignore
async def goldpack(ctx: commands.Context) -> None: # type: ignore
    embed: discord.Embed = hc.test(ctx=ctx) # type: ignore
    await ctx.reply(embed=embed, ephemeral=True)


@bot.command() # type: ignore
async def silverpack(ctx: commands.Context) -> None: # type: ignore
    embed: discord.Embed = hc.test(ctx=ctx) # type: ignore
    await ctx.reply(embed=embed, ephemeral=True)


@bot.command() # type: ignore
async def bronzepack(ctx: commands.Context) -> None: # type: ignore
    embed: discord.Embed = hc.test(ctx=ctx) # type: ignore
    await ctx.reply(embed=embed, ephemeral=True)


@bot.command() # type: ignore
async def sellCard(ctx: commands.Context) -> None: # type: ignore
    embed: discord.Embed = hc.test(ctx=ctx) # type: ignore
    await ctx.reply(embed=embed, ephemeral=True)


@bot.command() # type: ignore
async def sellAll(ctx: commands.Context) -> None: # type: ignore
    embed: discord.Embed = hc.test(ctx=ctx) # type: ignore
    await ctx.reply(embed=embed, ephemeral=True)


@bot.command() # type: ignore
async def myCards(ctx: commands.Context) -> None: # type: ignore
    embed: discord.Embed = hc.test(ctx=ctx) # type: ignore
    await ctx.reply(embed=embed, ephemeral=True)


@bot.command() # type: ignore
async def cards(ctx: commands.Context) -> None: # type: ignore
    embed: discord.Embed = hc.test(ctx=ctx) # type: ignore
    await ctx.reply(embed=embed, ephemeral=True)

# endregion
# region ~~~~~~~~~~~~~~~~~~~~~~~~~~~ money ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@bot.command() # type: ignore
async def myMoney(ctx: commands.Context) -> None: # type: ignore
    embed: discord.Embed = hc.test(ctx=ctx) # type: ignore
    await ctx.reply(embed=embed, ephemeral=True)


@bot.command() # type: ignore
async def addMoney(ctx: commands.Context) -> None: # type: ignore
    embed: discord.Embed = hc.test(ctx=ctx) # type: ignore
    await ctx.reply(embed=embed, ephemeral=True)


@bot.command() # type: ignore
async def removeMoney(ctx: commands.Context) -> None: # type: ignore
    embed: discord.Embed = hc.test(ctx=ctx) # type: ignore
    await ctx.reply(embed=embed, ephemeral=True)


@bot.command() # type: ignore
async def money(ctx: commands.Context) -> None: # type: ignore
    embed: discord.Embed = hc.test(ctx=ctx) # type: ignore
    await ctx.reply(embed=embed, ephemeral=True)

for command in bot.commands:
        print(f"COMMAND LOADED: {command.name}")

# endregion

# ~~~~ BOT START EVENT MESSAGE ~~~~
@bot.event
async def on_ready() -> None:
    print(f"Logged in as {bot.user}")
    print("------------------------")

# ~~~~ BOT START ~~~~
if TOKEN:
    bot.run(token=TOKEN)