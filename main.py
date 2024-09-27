import discord
from discord.ext import commands, tasks
import mysql.connector


bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())


bot.run('')
