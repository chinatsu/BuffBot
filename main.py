import discord
from discord.ext import commands
import botconfig

client = discord.Client()

bot = commands.Bot(command_prefix=';;')
startup_extensions = ['commands', 'voice']

@bot.event
async def on_ready():
    print('Logged in as')
    print('------')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


if __name__ == '__main__':
    for ext in startup_extensions:
        try:
            bot.load_extension(ext)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(ext, exc))
    bot.run(botconfig.token)
