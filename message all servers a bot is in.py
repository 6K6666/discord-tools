from discord.ext        import commands
from discord.ext.commands    import Bot
import asyncio
import discord
import time

bot = commands.Bot(command_prefix = "$")

@bot.event
async def on_ready():
    print(("I am running on " + bot.user.name))
    print(("With the ID: " + str(bot.user.id)))
    guilds=list(bot.guilds)
    print("connected on " + str(len(bot.guilds)) + " servers:")
    for x in range(len(guilds)):
        print('  '+ guilds[x-1].name)

@bot.command()
@commands.has_permissions(administrator=True)
async def broadcast(ctx,*,message):
    for guild in bot.guilds:
        for channel in guild.text_channels:
            channel = sorted([chan for chan in guild.channels if 
        chan.permissions_for(guild.me).send_messages and isinstance(chan, discord.TextChannel)], key=lambda x: x.position)[0]
            try:
                await channel.send(message)
                print('sent message')
            except:
                print('cant message channel')

bot.run('bot token') 