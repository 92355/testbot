import discord
from discord.ext import commands
import os

bot = commands.Bot(command_prefix = '/')


@bot.command()
async def 안녕(ctx):
    await ctx.send("안녕!")


bot.run(os.environ['token'])