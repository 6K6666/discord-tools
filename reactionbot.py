from discord.ext        import commands
from discord.ext.commands    import Bot
import asyncio
import discord
import time

bot = commands.Bot(command_prefix = "$")

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.dnd, activity=discord.Game("Starting...")) 
    print(("I am running on " + bot.user.name))
    print(("With the ID: " + str(bot.user.id)))
    guilds=list(bot.guilds)
    print("connected on " + str(len(bot.guilds)) + " servers:")
    for x in range(len(guilds)):
        print('  '+ guilds[x-1].name)
    time.sleep(5)
    await bot.change_presence(activity=discord.Streaming(name="i react to things", url="https://www.youtube.com/watch?v=iU9V4FEG_D4"))


async def react(message):
    custom_emojis = [
    "<:emoji:emoji-id:>",
    "<:emoji:emoji-id:>",
    "<:emoji:emoji-id:>"
    ]
    guild_emoji_names = [str(guild_emoji) for guild_emoji in message.guild.emojis]
    for emoji in custom_emojis:
        if emoji in guild_emoji_names:
            await message.add_reaction(emoji)

@bot.event
async def on_message(message):
    if message.channel.id == channel-id:
            await react(message)
 
bot.run("bot-token")