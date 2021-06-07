import discord
import csv
import datetime

# from discord.emoji import Emoji
# import discord.utils as utils

CHANNEL_NAME = "command"
LOG_FILE = "log.csv"
TIME_FORMAT = "%Y/%m/%d %H:%M:%S"
# class Task:
#     def __init__(self, time, name, *args):
#         self.time = time
#         self.name = name
#         self.args = args

#     def __list__(self):
#         return [self.time, self.name, *self.args]

# logs = None
# with open(LOG_FILE, 'r', encoding="utf-8") as f:
#     reader = csv.reader(f)
#     logs = list(reader)

token = None
with open("token", 'r', encoding="utf-8") as f:
	token = f.read()

bot = discord.Client()

@bot.event
async def on_ready():
    print('loggined')

def add_log(msg: discord.Message):
    args = msg.content.split()
    # task = Task(msg.created_at, *args)
    with open(LOG_FILE, 'a', encoding="utf=8") as f:
        writer = csv.writer(f, lineterminator='\n')
        row = [datetime.datetime.now().strftime(TIME_FORMAT)] + ['_'.join(args)]
        print(row)
        writer.writerow(row)
        # writer.writerow([msg.created_at.strftime(TIME_FORMAT)] + args)

@bot.event
async def on_message(msg: discord.Message):
    if msg.author.bot:
        return
    if not msg.channel.name == CHANNEL_NAME:
        return
    add_log(msg)
    # await msg.channel.send(args)
    await msg.add_reaction("✅")
    # await msg.add_reaction("🔳")
    # await msg.add_reaction("❌")

# 特定のリアクションが送られてきたら
# @bot.event
# async def on_reaction_add(reaction, user):
#     if user.bot:
#         return
#     if reaction.emoji == "❌":

bot.run(token)