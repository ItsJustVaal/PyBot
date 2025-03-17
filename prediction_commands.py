import discord
import sqlite3
from discord.ext import commands
from helper_commands import get_timestamp, user_check

def predict(ctx: commands.Context, cursor: sqlite3.Cursor) -> discord.Embed: # type: ignore
    print(f"USER: {ctx.author} CALLED COMMAND: {ctx.command}")
    
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
    print(f"USER: {ctx.author} CALLED COMMAND: {ctx.command}")
    
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
    print(f"USER: {ctx.author} CALLED COMMAND: {ctx.command}")
    
    embed = discord.Embed()
    message: list[str] = ctx.message.content.split(sep=" ")[1:]
    gameweek = cursor.execute("SELECT gameweek FROM fixtures ORDER BY gameweek DESC;").fetchone()[0]
    user = user_check(ctx=ctx, cursor=cursor) # type: ignore
    scores = message[2].split("-")
    
    if user == None:
        embed.add_field(name="MY CARD", value="YOU DONT EXIST, TYPE .JOIN")
    
    
    fixture_list = []
    fixtures = cursor.execute(f"SELECT * FROM fixtures WHERE gameweek = {gameweek}").fetchall()
    for fixture in fixtures:
            fixture_list.append(f"{fixture[0]} - {fixture[1]}")
    checker = f"{message[0]} - {message[1]}"
    
    if checker in fixture_list:    
        try:
            cursor.execute(f"SELECT * FROM predictions WHERE discord_id = {ctx.author.id} AND home_team = '{message[0]}' AND away_team = '{message[1]}';")
        except Exception as e:
            return embed.add_field(name="ERROR", value=f"Failed to find prediction with error {e}, check your capitalization and format. Use .help updatepred")
    else:
        return embed.add_field(name="ERROR", value="Could not find fixture in fixture list, check your capitalization and format. Use .help updatepred")
    
    try:
        cursor.execute(f"UPDATE predictions SET home_score = {scores[0]}, away_score = {scores[1]} WHERE discord_id = {ctx.author.id} AND home_team = '{message[0]}' AND away_team = '{message[1]}' AND gameweek = {gameweek};")
    except Exception as e:
        return embed.add_field(name="ERROR", value=f"Failed to update prediction with error {e}, check your capitalization and format. Use .help updatepred")     
    
    return my_pred(ctx, cursor)