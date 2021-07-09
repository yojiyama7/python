import discord
import csv
import datetime
import random

from discord import channel

# print(discord.__version__)

# from discord.emoji import Emoji
# import discord.utils as utils

CHANNEL_NAME = "command"
LOG_FILE = "log.csv"
TIME_FORMAT = "%Y/%m/%d %H:%M:%S"
DONE_MSG_LIST = """
おつかれー
おつー
いいねー
よくがんばった。
きゅーけー。
ないす
^^b
いいじゃん
""".split()

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

# intents = discord.Intents(reactions=True)
bot = discord.Client()

@bot.event
async def on_ready():
    print('loggined')

def add_log_inner(row):
    with open(LOG_FILE, 'a', encoding="utf=8") as f:
        writer = csv.writer(f, lineterminator='\n')
        # row = [datetime.datetime.now().strftime(TIME_FORMAT)] + ['_'.join(args)]
        # print(row)
        writer.writerow(row)

def add_log(msg: discord.Message):
    args = msg.content.split()
    row = [datetime.datetime.now().strftime(TIME_FORMAT)] + ['_'.join(args)]
    add_log_inner(row)

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
@bot.event
async def on_reaction_add(reaction: discord.Reaction, user: discord.User):
    # print("add", reaction)
    channel = reaction.message.channel
    # print(reaction, user)
    if user.bot:
        return
    if reaction.emoji == "✅":
        row = [datetime.datetime.now().strftime(TIME_FORMAT)] + ["-"]
        add_log_inner(row)
        msg = random.choice(DONE_MSG_LIST)
        # print(msg)
        await channel.send(msg)

@bot.event
async def on_reaction_remove(reaction: discord.Reaction, user: discord.User):
    # channel = reaction.message.channel
    print("remove", reaction)
    # print(reaction, user)
    # if user.bot:
    #     print('ret')
    #     return
    # # print("non-bot-reaction")
    # if reaction.emoji == "✅":
    #     row = [datetime.datetime.now().strftime(TIME_FORMAT)] + ["-"]
    #     add_log_inner(row)


bot.run(token)
