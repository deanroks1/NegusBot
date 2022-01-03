import discord
import time
import aiohttp
import re
import string
import random
from discord import user
from discord.errors import ClientException
from mimesis import Internet
import sys
import os
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option
from discord.ext import commands
from discord_components import DiscordComponents, Button, ButtonStyle
from economy import *
from hash import *
from mod import *
import random, json, aiohttp, logging, os
from discord.ext import commands
from time import ctime
from os import listdir, name
from os.path import isfile, join




client = commands.Bot(command_prefix=">")
slash = SlashCommand(client, sync_commands=True)
token = "OTIyNjIwMTc1NjMzNzY4NDY4.YcEG_w.t8SuFPeeuLewD2YPLqC-Pptf67c"
botversion = "V1.9.6"









@client.event
async def on_ready():
    print('[C]: Username: {0.user.name}#{0.user.discriminator}\n[C]: UserID: {0.user.id}\n[C]: Date Creation: {0.user.created_at}'.format(client));
    print(f'[C]: Currently in {int(len(client.guilds))} servers!')
    await client.change_presence(activity=discord.Game(name=botversion))


memes = [
    'https://cdn.discordapp.com/attachments/922622740094136332/923019600415830057/qxa3exkuqx681.png',#1
    'https://cdn.discordapp.com/attachments/922622740094136332/923019713557196860/d2sje9ft8w681.png',#2
    'https://cdn.discordapp.com/attachments/922622740094136332/923020095763144744/4nhaafkf6r681.mp4',#3
    'https://cdn.discordapp.com/attachments/922622740094136332/923020356640464987/fecmc4a82z681.png',#4
    'https://cdn.discordapp.com/attachments/922622740094136332/923020411694874695/d64e95601y681.png',#5
    'https://cdn.discordapp.com/attachments/922622740094136332/923020493890658374/np30myksrx681.png',#6
    'https://cdn.discordapp.com/attachments/922622740094136332/923020548282396762/do0vlg2yuy681.png',#7
    'https://cdn.discordapp.com/attachments/922622740094136332/923020753731989505/1nds3dtqfs681.png',#8
    'https://cdn.discordapp.com/attachments/922622740094136332/923020814822043718/iuqsu2owvv681.png',#9
    'https://cdn.discordapp.com/attachments/922622740094136332/923020883000451122/jf1tzdj2iv681.png',#10
    'https://cdn.discordapp.com/attachments/922622740094136332/923020924998021140/ads9uxd8zy681.png',#11
    'https://cdn.discordapp.com/attachments/922622740094136332/923021000558407690/5jgjsp18iz681.png',#12
    'https://www.reddit.com/r/WinStupidPrizes/comments/rjn6ge/climbing_on_top_of_a_tower_of_desks/',#13
    'https://www.reddit.com/r/WinStupidPrizes/comments/rk6c5o/lighting_yourself_on_fire_then_panicking_because/',#14
    'https://www.reddit.com/r/WinStupidPrizes/comments/rkvnqz/goofy_and_his_friends_playing_in_the_woods/',#15
    'https://www.reddit.com/r/WinStupidPrizes/comments/rimys0/dancing_in_the_back_of_a_pickup/',#16
    'https://www.reddit.com/r/WinStupidPrizes/comments/ribigb/wrong_game_with_kids/',#17
    'https://www.reddit.com/r/WinStupidPrizes/comments/rhrciw/tazer_tazer_tazer_aha/',#18
    'https://www.reddit.com/r/WinStupidPrizes/comments/rhkowz/testing_to_see_if_robot_grabbing_own_groin_could/ ',#19
    'https://www.reddit.com/r/WinStupidPrizes/comments/rgj0mu/bicecle/',#20
    'https://www.reddit.com/r/WinStupidPrizes/comments/rgcfmk/opening_a_beer_this_way/',#21
    'https://www.reddit.com/r/WinStupidPrizes/comments/rfzu7w/woman_tries_to_befriend_rat_rat_attempts_friends/',#22
    'https://www.reddit.com/r/WinStupidPrizes/comments/rfycjn/men_launches_fireworks_to_a_hot_hair_balloon/',#23
    'https://www.reddit.com/r/WinStupidPrizes/comments/rfnuy7/sliding_down_the_bowling_alley/',#24
    'https://www.reddit.com/r/WinStupidPrizes/comments/rfv1a5/intention_ball_bonks_ball_reality_ball_bonks_balls/',#25
    'https://www.reddit.com/r/WinStupidPrizes/comments/rdgw6a/professional_backflip/',#26
    'https://www.reddit.com/r/WinStupidPrizes/comments/rcjspi/girl_tries_doing_a_handstand_on_her_bed_with_a/',#26
    'https://www.reddit.com/r/WinStupidPrizes/comments/renf5o/doing_a_wheelie/',#27
    'https://www.reddit.com/r/WinStupidPrizes/comments/rar25a/surprise_stupid_prize_for_wouldbe_thief_merry/',#29
    'https://www.reddit.com/r/WinStupidPrizes/comments/rd6wkw/sometimes_you_want_an_unusual_fireworks_display/',#30
    'https://www.reddit.com/r/WinStupidPrizes/comments/ra8ubs/guy_slips_on_icethen_decides_to_deja_vu_himself/',#31
    'https://img.izismile.com/img/img14/20211206/gifs/morning_gifdump_173_12.gif',#32
    'https://www.reddit.com/r/WinStupidPrizes/comments/ra34ab/guy_tries_to_enter_a_house_forcibly_and_threatens/',#33
    'https://www.reddit.com/r/WinStupidPrizes/comments/r91moq/fireworks_at_the_butt_no/',#34
    'https://www.reddit.com/r/WinStupidPrizes/comments/r8m11s/play_with_fire_while_spraying_flamable_foam_on/',#35
    'https://www.reddit.com/r/WinStupidPrizes/comments/r8bcyq/he_jumped_into_a_ring_of_fire/',#36
    'https://www.reddit.com/r/WinStupidPrizes/comments/r84xsx/fortnight_dancing_on_a_trucks_bed/',#37
    'https://www.reddit.com/r/WinStupidPrizes/comments/r76iqp/this_exercise_looks_legit/',#38
    'https://www.reddit.com/r/WinStupidPrizes/comments/r5usko/douchebag_blocking_traffic_and_hitting_cars_gets/',#39
    'https://www.reddit.com/r/WinStupidPrizes/comments/qz2u1v/pulling_yourself_up_in_a_bucket/',#40
    'https://www.reddit.com/r/WinStupidPrizes/comments/qwdf5t/dora_wakes_up_her_roommate/',#41
    'https://www.reddit.com/r/WinStupidPrizes/comments/qv4nbd/tail_bone_bye/',#42
    'https://www.reddit.com/r/WinStupidPrizes/comments/qr6ccp/harassing_raccoons_inside_a_waste_container/', #43
    'https://www.reddit.com/r/WinStupidPrizes/comments/qlpryk/thats_what_you_get_when_you_stand_on_an_empty_tank/',# 44
    'https://www.reddit.com/r/WinStupidPrizes/comments/qmrbbw/doing_that_cup_thing/', #45
    'https://www.reddit.com/r/WinStupidPrizes/comments/ql02ay/trying_to_grab_a_tomato_through_a_spinning/', #46
    'https://www.reddit.com/r/WinStupidPrizes/comments/qk8j49/what_happens_when_you_jump_on_plastic_bins/', #47
    'https://www.reddit.com/r/WinStupidPrizes/comments/qgb196/dont_make_fun_of_dogs/', #48
    'https://www.reddit.com/r/WinStupidPrizes/comments/qjdazb/girl_releases_graduation_balloons_and_hit_power/', #49
    'https://www.reddit.com/r/WinStupidPrizes/comments/qhtl7a/traffic_light_1_dude_0/', #50
    'https://www.reddit.com/r/WinStupidPrizes/comments/qi7jmp/nut_crushed/', #51
    'https://www.reddit.com/r/WinStupidPrizes/comments/qj2cnz/idiot_fighting_a_snowma/', #52
    'https://www.reddit.com/r/WinStupidPrizes/comments/qez9qz/checking_phone_while_cycling/' #53
]




@slash.slash(
    name="Invite",
    description="Invite link for bot ",
)
async def Invite(ctx:SlashContext):
	await ctx.send("Hello, look at my profile there will be a add to server button press it and enjoy")



@slash.slash(
    name="Help",
    description="Help command",
)
async def help(ctx:SlashContext):
    embed = discord.Embed(color=discord.Color.green())
    embed.title = '️My available commands:'
    embed.description = '️⌨️ Prefix: `/`'
    embed.add_field(name='Invite', value='Bots invite link', inline=True)
    embed.add_field(name='credit', value='Credits to my awesome owners', inline=True)
    embed.add_field(name='Ban', value='Bans a user', inline=True)
    embed.add_field(name='Unban', value="Unbans a user", inline=True)
    embed.add_field(name='Kick', value="Kickes a user", inline=True)
    embed.add_field(name='Meme', value="Sends a random meme from ur list", inline=True)
    embed.add_field(name='For more commands do', value="/help2", inline=True)
    await ctx.send(content="", embeds=[embed])


@slash.slash(
    name="Help2",
    description="Help page #2",
)
async def help2(ctx):
    embed = discord.Embed(color=discord.Color.green())
    embed.title = '️My available commands:'
    embed.description = '️⌨️ Prefix: `/`'
    embed.add_field(name='Poll', value='Creates a poll to vote on', inline=True)
    embed.add_field(name='Permissions', value='Shows permissions of some commands example: ban kick', inline=True)
    embed.add_field(name='Server info', value='Serverinfo gets info about the server', inline=True)
    await ctx.send(content="", embeds=[embed])



@slash.slash(
    name="Credit",
    description="Credits to my awesome owners.",
)
async def Credits(ctx:SlashContext):
    embed = discord.Embed(color=discord.Color.green())
    embed.title = '️Credits to my owner'
    embed.description = '️These awesome people made me'
    embed.add_field(name='Owners:', value='Dean_#6947, HamSmacker#0001, xnb#0001, tncYT#6749.', inline=True)
    embed.add_field(name='Partners:', value='zrk community https://discord.gg/tUQ55bTYez fun gaming server, https://discord.gg/97Ner5DZRc Blues world fun community.', inline=True)
    await ctx.send(content="", embeds=[embed])


@slash.slash(
    name="Ban",
    description="Banneds a user permission: Ban member.",
)
@commands.has_permissions(ban_members = True)
async def ban(ctx:SlashContext, member : discord.Member, *, reason = None):
    await member.ban(reason = reason)
    await ctx.send(content=f'Susesfully banned that user.')


@ban.error
async def ban(ctx, error):
    await ctx.send("Not enough permissions to preform this command")

@slash.slash(
    name="Unban",
    description="Unbans a user ",
)
@commands.has_permissions(administrator = True)
async def unban(ctx:SlashContext, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return

@unban.error
async def unban(ctx, error):
    await ctx.send("Not enough permissions to preform this command")


@slash.slash(
    name="Kick",
    description="Kicks a user",
)
@commands.has_permissions(kick_members=True)
async def kick(ctx:SlashContext, user: discord.Member, *, reason="No reason provided"):
        await user.kick(reason=reason)
        embed = discord.Embed(color=discord.Color.green())
        embed.title = '️Sussesfully kicked that user'
        await ctx.send(content="", embeds=[embed])
        
@slash.slash(
    name="Meme",
    description="Sends a random meme",
)
async def Meme(ctx:SlashContext):
  await ctx.send(random.choice(memes))

import asyncio

@client.command()
@commands.has_permissions(manage_messages=True)
async def poll(ctx:SlashContext,*,message):
    embed=discord.Embed(title="Poll", description=f'{message}', color=discord.Color.blue())
    msg=await ctx.channel.send(embed=embed)
    await msg.add_reaction('👍')
    await msg.add_reaction('👎')


colors=[0xeb4034,0x31e2e8,0x3e32e3,0xe332dd,0xe3e332]

@slash.slash(
    name="Serverinfo",
    description="gets server info",
)
async def serverinfo(ctx:SlashContext):
	"""sends server's info"""
	icon = str(ctx.guild.icon_url)
	name= ctx.guild.name
	verification= ctx.guild.verification_level	
	premiums=ctx.guild.premium_subscription_count
	channelnumber=len(ctx.guild.channels)
	voicenumber=len(ctx.guild.voice_channels)
	memberCount = str(ctx.guild.member_count)
	rolenumber=len(ctx.guild.roles)
	created=str(ctx.guild.created_at).split(".")[0]
	

	embed = discord.Embed(
      title=name + " Server Information",
      color=random.choice(colors)
    )

	embed.set_thumbnail(url=icon)
	embed.add_field(name="name", value=name, inline=True)	
	embed.add_field(name="verification", value=verification, inline=True)
	embed.add_field(name="premiums", value=premiums, inline=True)
	embed.add_field(name="text channels",value=channelnumber,inline=True)
	embed.add_field(name="voice channels",value=voicenumber,inline=True)
	embed.add_field(name="members",value=memberCount,inline=True)
	embed.add_field(name="roles",value=rolenumber,inline=True)
	embed.add_field(name="created at",value=created,inline=True)


	await ctx.send(embed=embed)


@client.command()
async def userinfo(ctx, *, user: discord.Member = None):
	"""sends user's info"""
	if user is None:
		user = ctx.author      
	
	date_format = "%a, %d %b %Y %I:%M %p"
    
	joined_at=user.joined_at.strftime(date_format)
	created_at=user.created_at.strftime(date_format)
	
	embed = discord.Embed(color=random.choice(colors), description=user.mention)
	embed.set_author(name=str(user), icon_url=user.avatar_url)
	embed.set_thumbnail(url=user.avatar_url)
	embed.add_field(name="Joined", value=joined_at)
	members = sorted(ctx.guild.members, key=lambda m: m.joined_at)
	embed.add_field(name="Registered", value=created_at)
	if len(user.roles) > 1:
		role_string = ' '.join([r.mention for r in user.roles][1:])
		embed.add_field(name="Roles [{}]".format(len(user.roles)-1), value=role_string, inline=False)
	perm_string = ', '.join([str(p[0]).replace("_", " ").title() for p in user.guild_permissions if p[1]])
	embed.add_field(name="Guild permissions", value=perm_string, inline=False)
	embed.set_footer(text='ID: ' + str(user.id))
	return await ctx.send(embed=embed)



@slash.slash(
    name="Info",
    description="Sends info about the bot",
)
async def Info(ctx:SlashContext):
    embed = discord.Embed(color=discord.Color.green())
    embed.title = '️Info about this bot'
    embed.add_field(name='Prefix is / or >', value="The prefix is used to do the commands the bot offers", inline=True)
    embed.add_field(name='Memes', value="We have around 60 different memes", inline=True)
    embed.add_field(name='Why did i start on this project', value="Just bored thought of asking my friends to make a bot with me and now its this", inline=True)
    embed.add_field(name='Bot', value=f"The bot current version is {botversion}", inline=True)
    embed.add_field(name='My partners', value="https://discord.gg/tUQ55bTYez Chill gaming server, https://discord.gg/97Ner5DZRc Blues world fun community  ", inline=True)
    await ctx.send(content="", embeds=[embed])



@slash.slash(
    name="Permssions",
    description="Sends permissions for some commands",
)
async def Permissions(ctx:SlashContext):
    embed = discord.Embed(color=discord.Color.dark_blue())
    embed.title = '️Permissions'
    embed.add_field(name='Kick', value="Kick member permission", inline=True)
    embed.add_field(name='Ban', value="Ban memeber permission", inline=True)
    embed.add_field(name='Unban', value="administator permission", inline=True)
    embed.add_field(name='Poll', value="Manage message permission")
    embed.add_field(name='Mute/unmute/clean', value="Manage messages permission", inline=True)
    await ctx.send(content="", embeds=[embed])


@commands.command()#mute
@commands.has_permissions(manage_messages=True)
async def mute(ctx,member: discord.Member,*,reason=None):
    """mutes the user"""
    guild= ctx.guild
    mutedRole= discord.utils.get(guild.roles,name="Muted")
    
    if not mutedRole:
        mutedRole= await guild.create_role(name="Muted")
        
        for channel in guild.channels:
            await channel.set_permissions(mutedRole, speak=False , send_messages=False, read_message_history=True, read_messages=True)
    
    await member.add_roles(mutedRole,reason=reason)
    await ctx.send(f"{member.mention} is Muted for {reason}")        
    await member.send(f"you were muted in this server {guild.name} for {reason} ")

@commands.command()#unmute
@commands.has_permissions(manage_messages=True)
async def unmute(ctx,member: discord.Member,*,reason=None, guild):
    """unmutes the user"""
    mutedRole = discord.utils.get(ctx.guild.roles,name="Muted")

    await member.remove_roles(mutedRole)
    await ctx.send(f"{member.mention} is Unmuted ") 
    await member.send(f"you were Unmuted in this server {guild.name} for {reason}")



client.add_command(beg)
client.add_command(deposit)
client.add_command(withdraw)
client.add_command(rob)
client.add_command(slot)
client.add_command(clean)
client.add_command(send)
client.add_command(shop)
client.add_command(bag)
client.add_command(buy)
client.add_command(sell)
client.add_command(encode_md5)
client.add_command(encode_sha256)
client.run(token)
















##   a     fffff  k  k
##  a  a   f      kkk
## a    a  fffff  k  k
##a      a f      k    k