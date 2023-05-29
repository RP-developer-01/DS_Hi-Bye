import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
intents.messages = True

bot = commands.Bot(command_prefix='!', intents=intents)

welcome_messages = ["Welcome! ", "Greetings! ", "We are glad to see you! ", "Get ready for an exciting journey through our community! ", "Hey newcomer! Welcome to our team! ", "Welcome to our cozy corner of the internet. We hope you'll feel at home here! "]
goodbye_messages = ["Goodbye! ", "Best of luck to you! ", "Safe travels! ", "Thank you for being with us! Wishing you success in all your endeavors! ", "Farewell! We hope you found something interesting and useful here. Take care! ", "Goodbye! It was great spending time together. Don't forget about us and come back whenever you want! ", "Safe travels! May each step you take lead you to new opportunities and achievements! ", "Goodbye! Remember to preserve your uniqueness and keep seeking inspiration wherever it awaits you! "]

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.channels, name='CHANNEL_NAME_MESSAGE')
    if channel:
        welcome_message = random.choice(welcome_messages)
        await channel.send(f'{welcome_message} {member.mention}!')

@bot.event
async def on_member_remove(member):
    channel = discord.utils.get(member.guild.channels, name='CHANNEL_NAME_MESSAGE')
    if channel:
        goodbye_message = random.choice(goodbye_messages)
        await channel.send(f'{goodbye_message} {member.name}!')


bot.run('YOUR_BOT_TOKEN')
