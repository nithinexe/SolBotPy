# ping_command.py

from discord.ext import commands



@commands.command()
async def ping(ctx):
    await ctx.send('Pong!')



