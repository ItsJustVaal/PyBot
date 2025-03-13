import discord
import sqlite3
from discord.ext import commands
from helper_commands import get_timestamp, user_check
# Predict
# My Pred
# Update specific
# My pred for game week x

def predict(ctx: commands.Context, cursor: sqlite3.Cursor) -> discord.Embed: # type: ignore
    embed = discord.Embed()
    user = user_check(ctx=ctx, cursor=cursor) # type: ignore
    if user == None:
        return embed.add_field(name="MY CARD", value="YOU DONT EXIST, TYPE .JOIN")
    
    
    time: str = get_timestamp()
    predictions: list[str] = ctx.message.content.split(sep=" ")[1:]
    gameweek = cursor.execute("SELECT gameweek FROM fixtures ORDER BY gameweek DESC;").fetchone()[0]
    fixtures = cursor.execute(f"SELECT * FROM fixtures WHERE gameweek = {gameweek}").fetchall()
    matches = [(fixture[0], fixture[1]) for fixture in fixtures]
    
    check = cursor.execute(f"SELECT * FROM predictions WHERE discord_id = {ctx.author.id};").fetchall()
    if len(check) > 0:
        return embed.add_field(name="Error", value="""You already have predictions made, use the .updatepred command. 
                               Type .help updatepred for more info""")
    
    
    if not all("-" in pred for pred in predictions):
        return embed.add_field(name="Error", value=f"""You didnt enter in your predictions correctly. 
                               Please enter each prediction with a - inbetween the scores""")
    
    preds = [pred.split("-") for pred in predictions]
    if len(matches) != len(preds):
        return embed.add_field(name="Error", value=f"""You didnt enter in enough predictions. 
                               Please enter {len(matches)} different predictions""")

    for (home_team, away_team), (score1, score2) in zip(matches, preds):
        cursor.execute("INSERT INTO predictions (discord_id, home_team, away_team, home_score, away_score, gameweek, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?, ?, ?);",
                       (int(ctx.author.id), home_team, away_team, int(score1), int(score2), gameweek, time, time))
    

    return my_pred(ctx=ctx, cursor=cursor)

def my_pred(ctx: commands.Context, cursor: sqlite3.Cursor) -> discord.Embed: # type: ignore
    embed = discord.Embed()
    user = user_check(ctx=ctx, cursor=cursor) # type: ignore
    if user == None:
        return embed.add_field(name="MY CARD", value="YOU DONT EXIST, TYPE .JOIN")
    
    gameweek = cursor.execute("SELECT gameweek FROM fixtures ORDER BY gameweek DESC;").fetchone()[0]
    predictions = cursor.execute(f"SELECT * FROM predictions WHERE gameweek = {gameweek} AND discord_id = {ctx.author.id};").fetchall()
    
    if len(predictions) == 0:
        return embed.add_field(name="Error", value="You haven't made any predictions for this gameweek.")
    
    prediction_list: list[str] = [f"{pred[1]}:{pred[3]} - {pred[4]}:{pred[2]}" for pred in predictions]
    embed.add_field(name='MY PREDICTIONS',value='\n'.join(prediction_list))
    
    return embed

# Will need to check both home and away
# teams along with gameweek to update preds
def update_pred(ctx: commands.Context, cursor: sqlite3.Cursor) -> discord.Embed: # type: ignore
    embed = discord.Embed()
    user = user_check(ctx=ctx, cursor=cursor) # type: ignore
    if user == None:
        embed.add_field(name="MY CARD", value="YOU DONT EXIST, TYPE .JOIN")
    pass