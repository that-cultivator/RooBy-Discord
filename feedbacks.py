import discord
from discord.ext import commands
import mysql.connector

conn = mysql.connector.connect(
    database="your database name",
    host="Your MYSQL host",
    password="Your Database Password",
    port=your port,
    user="your MYSQL username",
) # Setup a connection with the mysql database 

cursor = conn.cursor() # SQL cursor object to interact with the database

cursor.execute("""CREATE TABLE IF NOT EXISTS feedbacks (
               id INTEGER AUTO_INCREMENT PRIMARY KEY,
               user_id BIGINT,
               server_id BIGINT,
               rating FLOAT(3, 1),
               review TEXT NULL
);
""") # Create a table called 'feedbacks' to store id, user_id, rating, and review



class Feedback(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command() # A hybrid command means a command that is both a slash command and a prefix command
    async def feedback(self, ctx, rating: float, *, review: str = None):  # Changed rating to float
        user_id = ctx.author.id # ID of the user who's using this command
        server_id = ctx.guild.id # ID of the server 

        valid_ratings = [i / 10 for i in range(10, 51)]  # Create acceptable ratings from 1.0 to 5.0 

        if rating not in valid_ratings:
            await ctx.send("Oops! Your can only provide a rating between 1.0 and 5.0 in increments of 0.1!")
            return

        cursor.execute(
            "INSERT INTO feedbacks (user_id, server_id, rating, review) VALUES(%s, %s, %s, %s)", 
            (user_id, server_id, rating, review if review else None)
        )  # Store the user's id and their feedback in the database

        conn.commit() # Commit the changes to the database
        await ctx.send(f"**Thank you, `{ctx.author.name}`, for submitting feedback! We hope you had a smooth experience using our service!**")


async def setup(bot):
    await bot.add_cog(Feedback(bot)) # Add the cog to the main bot

