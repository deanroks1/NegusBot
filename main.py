import discord
from discord.ext import commands
import string
import os
import discord
import random
import transliterate
import re
from mimesis import Internet
from faker import Faker
import sys
import base64 
import time
import asyncio
from os import listdir
from discord import Guild
import json
from discord.ext.commands.context import Context
from discord.ext.commands import has_permissions


bot = commands.Bot(
  command_prefix = commands.when_mentioned_or('>'),
  help_command=None,
  intents=discord.Intents.all(),
  bot=True,
)

# on start-up

@bot.event
async def on_ready():
    print('[C]: Username: {0.user.name}#{0.user.discriminator}\n[C]: UserID: {0.user.id}\n[C]: Date Creation: {0.user.created_at}'.format(bot));
    print(f'[C]: Currently in {int(len(bot.guilds))} servers!')

    await bot.change_presence(activity=discord.Game(name="Negus bot v0.1"))




@bot.command(name='help')
async def help(ctx):
  embed = discord.Embed(color=discord.Color.green())
  embed.title = '️My available commands:'
  embed.description = '️⌨️ Prefix: `>`'
  embed.add_field(name='ping', value='Wanna play ping-pong?',inline=True)
  embed.add_field(name='restart', value='Restarts the bot.',inline=True)
  embed.add_field(name='', value='Restarts the bot.',inline=True)




@bot.command(name='restart')
async def restart(ctx):
  if ctx.message.author.id == 728808714596777994 or ctx.message.author.id == 624861181311451137 or ctx.message.author.id == 886852737944395806 or ctx.message.author.id == 900779153203273779:
    embed = discord.Embed(color=discord.Color.green())
    embed.title = '👋🏼 Restarting!'
    embed.set_footer(text=bot.user.name,icon_url=bot.user.avatar_url)

    await ctx.message.reply(embed=embed, mention_author=True)

    python = sys.executable
    os.execl(python, python, * sys.argv)
  else:
    embed = discord.Embed(color=discord.Color.red())
    embed.title = '👿 Not enough permissions.'
    embed.set_footer(text=bot.user.name,icon_url=bot.user.avatar_url)

    await ctx.message.reply(embed=embed, mention_author=True)
    
@bot.command(name='credits')
async def credit(ctx):
  embed = discord.Embed(color=discord.Color.green())
  embed.title = 'Bot made by Dean_#6947, HamSmacker#8572, tncYT#6749, xnb#0001.'
  embed.set_footer(text=bot.user.name,icon_url=bot.user.avatar_url)
  
  await ctx.message.reply(embed=embed, mention_author=True)

bot.run("OTIyNjIwMTc1NjMzNzY4NDY4.YcEG_w.t8SuFPeeuLewD2YPLqC-Pptf67c")
