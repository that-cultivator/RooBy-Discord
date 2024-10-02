import discord
from discord.ext import commands, tasks

activity=discord.Game(name="That_Cultivator.exe") # Set a custom activity to be displayed on the bot's profile

class MyBot(commands.Bot):
    async def setup_hook(self):
        print("Bot is starting")
        await self.load_extension("feedback") # Load the feedback.py extension (cog) and add it to the bot


bot = MyBot(command_prefix="!", help_command=None, status=discord.Status.online, activity=activity, intents=discord.Intents.all()) # define bot, the prefix for all the commands will be '!'

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}!") 
    
@bot.hybrid_command() # A hybrid command means a command that is both a slash command and a prefix command
@commands.is_owner() # Only the owner of this bot can use this command
async def sync(ctx: commands.Context):
    await bot.tree.sync() # adds all the new hybrid slash commands to the bot so that users can see and use them
    embed = discord.Embed(description="> ```Successfully synced all hybrid commands!```", colour=discord.Color.green()) # Create an embed
    await ctx.send(embed=embed) # Send the embed 

@bot.hybrid_command()
async def hello(ctx: commands.Context):
    embed = discord.Embed(title="**Hello**", description="> ```I am Rooby, a friendly bot who will help you store server feedbacks!```")
    embed.add_field(name="Get Started", value="> ```If you want to get started, then begin by using the '!help' command!```", inline=False)
    await ctx.send(embed=embed)
    
@bot.hybrid_command(with_app_command=True)
async def help(ctx: commands.Context):
    embed = discord.Embed(title="**Help Panel**", description="> Dear user, to get help on a specific category, please type the name of the category along with the help command like this ```!help categoryName``` or ```/help categoryName```") # Create an embed
    embed.add_field(name="**All Categories**", value="", inline=False) # Create a new field for the embed
    embed.add_field(name="", value="> ```Feedbacks```", inline=False) # Create another field for the embed
    embed.add_field(name="", value="> ```Stats```", inline=False) # One more field...
    await ctx.send(embed=embed) # Finally, send the embed
    

with open('token.txt') as f:
    TOKEN = f.readline()

bot.run(TOKEN)
