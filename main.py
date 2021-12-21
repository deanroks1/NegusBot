print("logging into bot")
print("...............")
print(".             .")
print("..           ..")
print("...         ...")
print("....       ....")
print(".....     .....")
print("......   ......")
print("Logged into the bot sucsesfully")
print("prefix = /")



import re
import string
import random
from mimesis import Internet
import sys
import os
import discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option
import time

client = commands.Bot(command_prefix="!")
slash = SlashCommand(client, sync_commands=True)
token = "OTIyNjIwMTc1NjMzNzY4NDY4.YcEG_w.t8SuFPeeuLewD2YPLqC-Pptf67c"





@slash.slash(
    name="hello",
    description="Test",
    guild_ids=[922622739351760966]
)
async def hello(ctx:SlashContext):
	await ctx.send("test")



@slash.slash(
    name="Help",
    description="Help command",
    guild_ids=[922622739351760966]
)
async def help(ctx:SlashContext):
    embed = discord.Embed(color=discord.Color.green())
    embed.title = '️My available commands:'
    embed.description = '️⌨️ Prefix: `/`'
    embed.add_field(name='hello', value='Test command', inline=True)
    await ctx.send(content="", embeds=[embed])


@slash.slash(
    name="Credit",
    description="Credits to my awesome owners.",
    guild_ids=[922622739351760966]
)
async def help(ctx:SlashContext):
    embed = discord.Embed(color=discord.Color.green())
    embed.title = '️Credits to my owner'
    embed.description = '️These awesome people made me'
    embed.add_field(name='Owners:', value='Dean_#6947, HamSmacker#0002, xnb#0001, tncYT#6749.', inline=True)
    await ctx.send(content="", embeds=[embed])





client.run(token)
