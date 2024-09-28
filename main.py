import discord
from discord.ext import commands, tasks
import mysql.connector


bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())


with open('token.txt') as f:
    TOKEN = f.readline()

bot.run(TOKEN)
