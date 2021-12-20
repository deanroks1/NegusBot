import discord
from discord.ext import commands


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











bot.run("OTIyNjIwMTc1NjMzNzY4NDY4.YcEG_w.t8SuFPeeuLewD2YPLqC-Pptf67c")
