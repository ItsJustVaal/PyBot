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
async def on_ready():
    for command in bot.commands:
        print(f"COMMAND LOADED: {command.name}")
    print(f"Logged in as {bot.user}")
    print("------------------------")
    



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~ COMMANDS ~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~ Every Command will call for an embed then reply to the user ~
# ~ Most message should be ephemeral but check args ~
# ~ Going to be a lot of type: ignore due to missing types ~

@bot.command() # type: ignore
async def test(ctx: commands.Context): # type: ignore
    embed: discord.Embed = hc.test(ctx=ctx) # type: ignore
    await ctx.reply(embed=embed, ephemeral=True)
    








# ~~~~ BOT START ~~~~
if TOKEN:
    bot.run(token=TOKEN)