import discord
import asyncio
import os


client = commands.Bot(command_prefix = '-')

@client.event
async def on_message(message):
    if message.content == ("빙빙베베 온!"):
        helloembed = discord.Embed(title="빙빙베베 켜짐!",
                                     description=" ", 
                                        color=0xFaaaaF)
        await message.channel.send(embed=helloembed)

client.run(os.environ['token'])
