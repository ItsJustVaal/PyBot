import discord, os
import helper_commands as hc
from discord.ext import commands
from dotenv import load_dotenv


# ~~~~ LOAD ENV VARIABLES ~~~~
load_dotenv()
TOKEN: str | None = os.getenv(key="TOKEN")


# ~~~~ CREATE AND CONFIGURE BOT ~~~~
intents: discord.Intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(
    command_prefix=commands.when_mentioned_or("."),
    intents=intents,
)


# ~~~~ BOT START EVENT MESSAGE ~~~~
@bot.event
async def on_ready() -> None:
    for command in bot.commands:
        print(f"COMMAND LOADED: {command.name}")
    print(f"Logged in as {bot.user}")
    print("------------------------")
    


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~ COMMANDS ~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~ Every Command will call for an embed then reply to the user ~
# ~ Most message should be ephemeral but check args ~
# ~ Going to be a lot of type: ignore due to missing types ~
# ~ These are in camelCase to match the original ones ~

@bot.command() # type: ignore
async def test(ctx: commands.Context) -> None: # type: ignore
    embed: discord.Embed = hc.test(ctx=ctx) # type: ignore
    await ctx.reply(embed=embed, ephemeral=True)
    
    
@bot.command() # type: ignore
async def commandsList(ctx: commands.Context) -> None: # type: ignore
    pass


@bot.command() # type: ignore
async def join(ctx: commands.Context) -> None: # type: ignore
    pass

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~ fixtures ~~~~~~~~~~~~~~~~~~~~~~~~~~~
@bot.command() # type: ignore
async def setFixtures(ctx: commands.Context) -> None: # type: ignore
    pass


@bot.command() # type: ignore
async def updateFixture(ctx: commands.Context) -> None: # type: ignore
    pass


@bot.command() # type: ignore
async def deleteFixture(ctx: commands.Context) -> None: # type: ignore
    pass


@bot.command() # type: ignore
async def addFixture(ctx: commands.Context) -> None: # type: ignore
    pass


@bot.command() # type: ignore
async def fixtures(ctx: commands.Context) -> None: # type: ignore
    pass


@bot.command() # type: ignore
async def setGameweek(ctx: commands.Context) -> None: # type: ignore
    pass


@bot.command() # type: ignore
async def toggle(ctx: commands.Context) -> None: # type: ignore
    pass

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~ results ~~~~~~~~~~~~~~~~~~~~~~~~~~~
@bot.command() # type: ignore
async def setResults(ctx: commands.Context) -> None: # type: ignore
    pass


@bot.command() # type: ignore
async def updateResults(ctx: commands.Context) -> None: # type: ignore
    pass


@bot.command() # type: ignore
async def deleteResults(ctx: commands.Context) -> None: # type: ignore
    pass


@bot.command() # type: ignore
async def results(ctx: commands.Context) -> None: # type: ignore
    pass

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~ fun ~~~~~~~~~~~~~~~~~~~~~~~~~~~
@bot.command() # type: ignore
async def eball(ctx: commands.Context) -> None: # type: ignore
    pass

@bot.command() # type: ignore
async def meme(ctx: commands.Context) -> None: # type: ignore
    pass


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~ predictions ~~~~~~~~~~~~~~~~~~~~~~~~~~~
@bot.command() # type: ignore
async def predict(ctx: commands.Context) -> None: # type: ignore
    pass


@bot.command() # type: ignore
async def mypred(ctx: commands.Context) -> None: # type: ignore
    pass


@bot.command() # type: ignore
async def updatePred(ctx: commands.Context) -> None: # type: ignore
    pass


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~ points ~~~~~~~~~~~~~~~~~~~~~~~~~~~
@bot.command() # type: ignore
async def updatePoints(ctx: commands.Context) -> None: # type: ignore
    pass


@bot.command() # type: ignore
async def addPoints(ctx: commands.Context) -> None: # type: ignore
    pass


@bot.command() # type: ignore
async def removePoints(ctx: commands.Context) -> None: # type: ignore
    pass


@bot.command() # type: ignore
async def standings(ctx: commands.Context) -> None: # type: ignore
    pass


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~ fut ~~~~~~~~~~~~~~~~~~~~~~~~~~~
@bot.command() # type: ignore
async def goldpack(ctx: commands.Context) -> None: # type: ignore
    pass


@bot.command() # type: ignore
async def silverpack(ctx: commands.Context) -> None: # type: ignore
    pass


@bot.command() # type: ignore
async def bronzepack(ctx: commands.Context) -> None: # type: ignore
    pass


@bot.command() # type: ignore
async def sellCard(ctx: commands.Context) -> None: # type: ignore
    pass


@bot.command() # type: ignore
async def sellAll(ctx: commands.Context) -> None: # type: ignore
    pass


@bot.command() # type: ignore
async def myCards(ctx: commands.Context) -> None: # type: ignore
    pass


@bot.command() # type: ignore
async def cards(ctx: commands.Context) -> None: # type: ignore
    pass


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~ money ~~~~~~~~~~~~~~~~~~~~~~~~~~~
@bot.command() # type: ignore
async def myMoney(ctx: commands.Context) -> None: # type: ignore
    pass


@bot.command() # type: ignore
async def addMoney(ctx: commands.Context) -> None: # type: ignore
    pass


@bot.command() # type: ignore
async def removeMoney(ctx: commands.Context) -> None: # type: ignore
    pass


@bot.command() # type: ignore
async def money(ctx: commands.Context) -> None: # type: ignore
    pass





# ~~~~ BOT START ~~~~
if TOKEN:
    bot.run(token=TOKEN)